import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ContextTypes,
    CallbackQueryHandler,
    MessageHandler,
    CommandHandler,
    filters,
    CallbackContext
)

from keyboards import (
    main_menu,
    to_order_menu,
    injera_menu,
    bread_menu,
    white_bread_menu,
    wheat_bread_menu,
    agelgel_menu,
    doro_wot_menu,
    baltena_menu,
    Shiro_menu,
    keey_shiro_menu,
    nech_shiro_menu,
    quantity_menu,
    pepper_menu,
    chilliPepper_menu
)
from lang_det import detect_language

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text or ""
    lang = detect_language(text)
    context.user_data["lang"] = lang

    if lang == "am":
        await update.message.reply_text(
            "እንኳን ወደ መሲ ባህላዊ ድፎ እና እንጀራ ቦት በደህና መጡ!",
            reply_markup=main_menu("am")
        )
    else:
        await update.message.reply_text(
            "Welcome to Mesi Bakery Bot!",
            reply_markup=main_menu("en")
        )

user_state = {}  # user_id → {"category": "...", "item": "..."}

async def callback_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    data = query.data
    user_id = query.from_user.id
    lang = context.user_data.get("lang", "en")

    # Main categories 
    if data == "to_order":
        await query.edit_message_text(
            "Select a category to order from:" if lang=="en" else "እባክዎ ለትዕዛዝ ምድብ ይምረጡ:",
            reply_markup=to_order_menu(lang)
        )
        return

    if data == "contact":
        await query.edit_message_text(
            "You can contact us using our phone +251 910590715 or visit our bakery at Addis Ababa, Mekanisa Qore, bus station."
            if lang=="en"
            else "እባክዎ በ +251 910590715 ያግኙን ወይም በአዲስ አበባ፣ መካኒሳ ቆሬ 2 ና 5 ቁጥር ባስ ማዞሪያ።"
        )
        return

    # Category selection
    if data in ["bread", "injera", "baltena", "doro_wot", "agelgel"]:
        user_state[user_id] = {"category": data, "item": None}
        menu_map = {
            "bread": bread_menu(lang),
            "injera": injera_menu(lang),
            "baltena": baltena_menu(lang),
            "doro_wot": doro_wot_menu(lang),
            "agelgel": agelgel_menu(lang)
        }
        text_map = {
            "bread": "Choose your bread type:" if lang=="en" else "የዳቦ ዓይነት ይምረጡ:",
            "injera": "Choose type of Injera:" if lang=="en" else "የእንጀራ ዓይነት ይምረጡ:",
            "baltena": "Choose Baltena item:" if lang=="en" else "የባልትና ዓይነት ይምረጡ:",
            "doro_wot": "How many chickens do you want:" if lang=="en" else "የሚፈልጉትን የዶሮ ብዛት ያስገቡ:",
            "agelgel": "How many portions do you want:" if lang=="en" else "እባክዎ የሚፈልጉትን ብዛት ያስገቡ:"
        }
        await query.edit_message_text(text_map[data], reply_markup=menu_map[data])
        return

    # Bread types
    if data.startswith("bread_"):
        bread_type = data.replace("bread_", "")
        user_state[user_id]["item"] = bread_type
        if bread_type == "white":
            await query.edit_message_text(
                "Select KG of bread:" if lang=="en" else "የዳቦ ኪ.ግ ይምረጡ:",
                reply_markup=white_bread_menu(lang)
            )
        elif bread_type == "wheat":
            await query.edit_message_text(
                "Select KG of bread:" if lang=="en" else "የዳቦ ኪ.ግ ይምረጡ:",
                reply_markup=wheat_bread_menu(lang)
            )
        return

    # KG selection
    if data == "kg_other":
        await query.edit_message_text("Enter the amount in KG:" if lang=="en" else "እባክዎ መጠኑን በኪ.ግ ያስገቡ:")
        context.user_data["awaiting_kg"] = True
        return

    if data.startswith("kg_") and data != "kg_other":
        kg = int(data.split("_")[1])
        context.user_data["selected_kg"] = kg
        category = user_state[user_id]["category"]

        if category == "bread":
            await query.edit_message_text(
                f"Selected KG: {kg}\nNow select quantity:",
                reply_markup=quantity_menu(lang)
            )
        else:
            await query.edit_message_text(
                f"Selected KG: {kg}\nYou can now continue with /order or /done"
            )
        return

    if data.startswith("agelgel_") or data.startswith("doro_wot_"):
        item_name = data.split("_", 1)[1]
        user_state[user_id]["item"] = item_name
        await query.edit_message_text(
            "How many do you want?" if lang=="en" else "እባክዎ ብዛት ያስገቡ:"
        )
        context.user_data["awaiting_qty"] = True
        return

    # Baltena items
    if data in ["baltena_pepper", "baltena_chilliPepper", "baltena_shiro"]:
        item_name = data.replace("baltena_", "")
        user_state[user_id]["item"] = item_name
        if data == "baltena_shiro":
            await query.edit_message_text(
                "Choose shiro type:" if lang=="en" else "የሽሮ ዓይነት ይምረጡ:",
                reply_markup=Shiro_menu(lang)
            )
        else:
            await query.edit_message_text(
                "Enter amount in KG (e.g., 5, 6,...):" if lang=="en" else "እባክዎ በኪ.ግ ያስገቡ (ለምሳሌ: 5, 6,...):"
            )
            context.user_data["awaiting_kg"] = True
        return

    if data in ["keey_shiro", "white_shiro"]:
        user_state[user_id]["item"] = data
        await query.edit_message_text(
            "Choose in KG:" if lang=="en" else "እባክዎ በኪ.ግ ይምረጡ"
        )
        context.user_data["awaiting_kg"] = True
        return

    if data == "baletna_pepper":
        user_state[user_id]["item"] = "pepper"
        await query.edit_message_text(
            "Choose in KG:" if lang=="en" else "እባክዎ በኪ.ግ ይምረጡ",
            reply_markup=pepper_menu(lang)
        )
        return

    if data == "baletna_chilliPepper":
        user_state[user_id]["item"] = "peppercorn"
        await query.edit_message_text(
            "Choose in KG:" if lang=="en" else "እባክዎ በኪ.ግ ይምረጡ"
        )
        context.user_data["awaiting_kg"] = True
        return

    if data.startswith("qty_") and user_state.get(user_id):
        if data == "qty_other":
            context.user_data["awaiting_qty"] = True
            await query.edit_message_text(
                f"Enter quantity for {user_state[user_id]['item']} ({context.user_data.get('selected_kg')} kg):"
            )
            return

        qty = int(data.split("_")[1])
        category = user_state[user_id]["category"]
        item = user_state[user_id]["item"]
        kg = context.user_data.get("selected_kg", None)

        await query.edit_message_text(
            f"Added: {category} → {item} → {kg} kg → Qty {qty}\n\nWrite /done to finish or /order to continue."
        )
        context.user_data.pop("selected_kg", None)
        context.user_data.pop("awaiting_qty", None)
        return

def text_handler(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id

    if context.user_data.get("awaiting_kg"):
        category = user_state[user_id]["category"]
        if category != "bread" and category not in ["baltena", "pepper", "chilliPepper", "shiro", "keey_shiro", "white_shiro"]:
            context.user_data["awaiting_kg"] = False
            return

        try:
            kg = float(update.message.text)
        except ValueError:
            update.message.reply_text("Invalid input. Enter KG like: 1, 1.5, 2")
            return

        context.user_data["awaiting_kg"] = False
        context.user_data["selected_kg"] = str(kg)
        category = user_state[user_id]["category"]
        item = user_state[user_id]["item"]

        if category == "bread":
            update.message.reply_text(
                f"Selected: {category} → {item} → {kg} kg\nNow select quantity:",
                reply_markup=quantity_menu(context.user_data.get("lang", "en"))
            )
        else:
            update.message.reply_text(
                f"Selected: {category} → {item} → {kg} kg\nYou can now continue with /order or /done"
            )
        return

    if context.user_data.get("awaiting_qty"):
        try:
            qty = int(update.message.text)
        except ValueError:
            update.message.reply_text("Invalid input. Enter quantity as numbers only.")
            return

        kg = context.user_data.get("selected_kg")
        category = user_state[user_id]["category"]
        item = user_state[user_id]["item"]

        update.message.reply_text(
            f"Added: {category} → {item} → {kg if kg else '-'} kg → Qty {qty}\n\nWrite /done or continue ordering."
        )

        context.user_data.pop("awaiting_qty")
        context.user_data.pop("selected_kg", None)
        return
