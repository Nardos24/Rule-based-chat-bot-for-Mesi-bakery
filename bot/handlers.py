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
    language_menu,
    main_menu,
    to_order_menu,
    injera_menu,
    white_injera_menu,
    black_injera_menu,
    hay_injera_menu,    
    normal_injera_menu,
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
    chillipepper_menu
)
from lang_det import detect_language

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Please select your language / ቋንቋ ይምረጡ",
        reply_markup=language_menu()
    )

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
    
    if user_id not in user_state:
        user_state[user_id] = {"category": None, "item": None}

    # Main categories 
    if data == "lang_en":
        context.user_data["lang"] = "en"
        await query.edit_message_text(
            "Welcome to Mesi Bakery Bot!",
            reply_markup=main_menu("en")
        )
        return

    if data == "lang_am":
        context.user_data["lang"] = "am"
        await query.edit_message_text(
            "እንኳን ወደ መሲ ባህላዊ ዳቦ እና እንጀራ ቦት በደህና መጡ!",
            reply_markup=main_menu("am")
        )
        return

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
            "bread": bread_menu,
            "injera": injera_menu,
            "baltena": baltena_menu,
            "doro_wot": doro_wot_menu,
            "agelgel": agelgel_menu
}

        text_map = {
            "bread": "Choose your bread type:" if lang=="en" else "የዳቦ ዓይነት ይምረጡ:",
            "injera": "Choose type of Injera:" if lang=="en" else "የእንጀራ ዓይነት ይምረጡ:",
            "baltena": "Choose Baltena item:" if lang=="en" else "የባልትና ዓይነት ይምረጡ:",
            "doro_wot": "🍗 Doro Wot — prepared fresh with traditional Ethiopian spices. enter the amount of chickens you want:" if lang=="en" else "🍗 ዶሮ ወጥ - በባህላዊ ቅመም የተዘጋጀ። እባክዎ የሚፈልጉትን የዶሮ መጠን ያስገቡ",
            "agelgel": "How many agelgel do you want:" if lang=="en" else "እባክዎ የሚፈልጉትን ብዛት ያስገቡ:"
        }    
        menu_text = text_map[data]
        menu_keyboard = menu_map[data](lang)
        await query.edit_message_text(menu_text, reply_markup=menu_keyboard)
        return

    
    if data == "bread_white":
        user_state[user_id]["item"] = "white_bread"
        await query.edit_message_text(
            "Select KG:",
            reply_markup=white_bread_menu(lang)
        )
        return

    if data == "bread_wheat":
        user_state[user_id]["item"] = "wheat_bread"
        await query.edit_message_text(
            "Select KG:",
            reply_markup=wheat_bread_menu(lang)
        )
        return

    if data == "injera_white":
        await query.edit_message_text(
            "Choose Injera type:",
            reply_markup=white_injera_menu(lang)
        )
        return

    if data == "injera_black":
        await query.edit_message_text(
            "Choose Injera type:",
            reply_markup=black_injera_menu(lang)
        )
        return

    if data == "injera_both":
        await query.edit_message_text(
            "Choose Injera type:",
            reply_markup=white_injera_menu(lang)
        )
        return


    # KG selection
    if data == "kg_other":
        await query.edit_message_text("Enter the amount in KG (e.g., 5, 6,...)::" if lang=="en" else "እባክዎ መጠኑን በኪ.ግ ያስገቡ (ለምሳሌ: 5, 6,...):")
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

    if data == "doro_confirm" or data == "other_amount":
        await query.edit_message_text(
            "Please enter the amount you want ?" if lang=="en" else "እባክዎ ብዛት ያስገቡ:"
        )
        context.user_data["awaiting_qty"] = True
        return
    if data.startswith("agelgel_"):
        user_state[user_id]["item"] = data
        await query.edit_message_text("Enter quantity:")
        context.user_data["awaiting_qty"] = True
        return

    # Baltena items
    if data == "shiro":
            await query.edit_message_text(
                "Choose shiro type:" if lang=="en" else "የሽሮ ዓይነት ይምረጡ:",
                reply_markup=Shiro_menu(lang)
            )
            return
    if data in ["keey_shiro", "white_shiro", "hay_injera", "pepper", "chillipepper"]:
        user_state[user_id]["item"] = data
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
    if data == "back_to_main":
        await query.edit_message_text(
            "Main Menu:" if lang=="en" else "ዋና ምድብ:",
            reply_markup=main_menu(lang)
        )
        return
    if data == "back_to_item":
        category = user_state[user_id]["category"]
        menu_map = {
            "bread": bread_menu,
            "injera": injera_menu,
            "baltena": baltena_menu,
            "doro_wot": doro_wot_menu,
            "agelgel": agelgel_menu
        }
        await query.edit_message_text(
            "Select an item:" if lang=="en" else "እባክዎ ንጥል ይምረጡ:",
            reply_markup=menu_map[category](lang)
        )
        return

def text_handler(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id

    if context.user_data.get("awaiting_kg"):
        category = user_state[user_id]["category"]
        if category not in ["bread", "baltena", "injera"]:
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
