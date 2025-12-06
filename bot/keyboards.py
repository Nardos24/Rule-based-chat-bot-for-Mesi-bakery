from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def main_menu(lang="en"):
    if lang == "am":
        buttons = [
            [InlineKeyboardButton("🛒 ለማዝ", callback_data="to order")],
            [InlineKeyboardButton("📞 ያግኙን", callback_data="contact")]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("🛒 to Order", callback_data="to order")],
            [InlineKeyboardButton("📞 Contact", callback_data="contact")]
        ]
    return InlineKeyboardMarkup(buttons)
def to_order_menu(lang="en"):
    if lang == "am":
        buttons = [
            [InlineKeyboardButton("🥞 እንጀራ", callback_data="injera")],
            [InlineKeyboardButton("🍞 ዳቦ", callback_data="bread")],
            [InlineKeyboardButton("🍲 አገልግል", callback_data="agelgel")],
            [InlineKeyboardButton("🍗 ዶሮ ወጥ", callback_data="doro")],
            [InlineKeyboardButton("🛍️ ባልትና", callback_data="baltena")],
            [InlineKeyboardButton("⬅ ተመለስ", callback_data="back_main")]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("🥞 Injera", callback_data="injera")],
            [InlineKeyboardButton("🍞 Bread", callback_data="bread")],
            [InlineKeyboardButton("🍲 Agelgel", callback_data="agelgel")],
            [InlineKeyboardButton("🍗 Doro Wot", callback_data="doro")],
            [InlineKeyboardButton("🛍️ Baltena", callback_data="baltena")],
            [InlineKeyboardButton("⬅ Back", callback_data="back_main")]
        ]
    return InlineKeyboardMarkup(buttons)
def injera_menu(lang="en"):
    if lang == "am":
        buttons = [
            [InlineKeyboardButton(" ነጭ", callback_data="injera_white")],
            [InlineKeyboardButton("ጥቁር", callback_data="injera_black")],
            [InlineKeyboardButton(" ሁለቱም", callback_data="injera_both")],
            [InlineKeyboardButton("⬅ ተመለስ", callback_data="orders")]
        ]
    else:
        buttons = [
            [InlineKeyboardButton(" White Injera", callback_data="injera_white")],
            [InlineKeyboardButton("Black Injera", callback_data="injera_black")],
            [InlineKeyboardButton(" Both", callback_data="injera_both")],
            [InlineKeyboardButton("⬅ Back", callback_data="orders")]
        ]
    return InlineKeyboardMarkup(buttons)
def bread_menu(lang="en"):
    if lang == "am":
        buttons = [
            [InlineKeyboardButton(" ፍርኖ ዳቦ", callback_data="bread_white")],
            [InlineKeyboardButton(" ስንዴ ዳቦ", callback_data="bread_wheat")],
            [InlineKeyboardButton("⬅ ተመለስ", callback_data="orders")]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("White Bread", callback_data="bread_white")],
            [InlineKeyboardButton(" Wheat Bread", callback_data="bread_wheat")],
            [InlineKeyboardButton("⬅ Back", callback_data="orders")]
        ]
    return InlineKeyboardMarkup(buttons)
def white_bread_menu(lang="en"):
    if lang == "am":
        buttons = [
            [InlineKeyboardButton("1 ኪ.ግ", callback_data="kg_1"),
             InlineKeyboardButton("2 ኪ.ግ", callback_data="kg_2")],
            [InlineKeyboardButton("3 ኪ.ግ", callback_data="kg_3"),
             InlineKeyboardButton("4 ኪ.ግ", callback_data="kg_4")],
            [InlineKeyboardButton("5 ኪ.ግ", callback_data="kg_5"),
             InlineKeyboardButton("6 ኪ.ግ", callback_data="kg_6")],
            [InlineKeyboardButton("⬅ ተመለስ", callback_data="bread")]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("1 kg", callback_data="kg_1"),
             InlineKeyboardButton("2 kg", callback_data="kg_2")],
            [InlineKeyboardButton("3 kg", callback_data="kg_3"),
             InlineKeyboardButton("4 kg", callback_data="kg_4")],
            [InlineKeyboardButton("5 kg", callback_data="kg_5"),
             InlineKeyboardButton("6 kg", callback_data="kg_6")],
            [InlineKeyboardButton("⬅ Back", callback_data="bread")]
        ]
    return InlineKeyboardMarkup(buttons)
def wheat_bread_menu(lang="en"):
    if lang == "am":
        buttons = [
            [InlineKeyboardButton("1 ኪ.ግ", callback_data="kg_1"),
             InlineKeyboardButton("2 ኪ.ግ", callback_data="kg_2")],
            [InlineKeyboardButton("3 ኪ.ግ", callback_data="kg_3"),
             InlineKeyboardButton("4 ኪ.ግ", callback_data="kg_4")],
            [InlineKeyboardButton("5 ኪ.ግ", callback_data="kg_5"),
             InlineKeyboardButton("6 ኪ.ግ", callback_data="kg_6")],
            [InlineKeyboardButton("⬅ ተመለስ", callback_data="bread")]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("1 kg", callback_data="kg_1"),
             InlineKeyboardButton("2 kg", callback_data="kg_2")],
            [InlineKeyboardButton("3 kg", callback_data="kg_3"),
             InlineKeyboardButton("4 kg", callback_data="kg_4")],
            [InlineKeyboardButton("5 kg", callback_data="kg_5"),
             InlineKeyboardButton("6 kg", callback_data="kg_6")],
            [InlineKeyboardButton("⬅ Back", callback_data="bread")]
        ]
    return InlineKeyboardMarkup(buttons)


def agelgel_menu(lang="en"):
    if lang == "am":
        buttons = [
            [InlineKeyboardButton("🥗 ፆም", callback_data="agelgel_fasting")],
            [InlineKeyboardButton("🍛 የፍስግ", callback_data="agelgel_non_fasting")],
            [InlineKeyboardButton("⭐ ልዩ", callback_data="agelgel_special")],
            [InlineKeyboardButton("⬅ ተመለስ", callback_data="orders")]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("🥗 Fasting", callback_data="agelgel_fasting")],
            [InlineKeyboardButton("🍛 Non-Fasting", callback_data="agelgel_non_fasting")],
            [InlineKeyboardButton("⭐ Special", callback_data="agelgel_special")],
            [InlineKeyboardButton("⬅ Back", callback_data="orders")]
        ]

    return InlineKeyboardMarkup(buttons)

def doro_wot_menu(lang="en"):
    if lang == "am":
        text = "🍗 ዶሮ ወጥ - በባህላዊ ቅመም የተዘጋጀ። እባክዎ የሚፈልጉትን መጠን ያስገቡ?"
        buttons = [
            [InlineKeyboardButton("🛒 ይትዕዛዙ", callback_data="doro_order")],
            [InlineKeyboardButton("⬅ ተመለስ", callback_data="orders")]
        ]
    else:
        text = "🍗 Doro Wot — prepared fresh with traditional Ethiopian spices. How many chickens do you want?"
        buttons = [
            [InlineKeyboardButton("🛒 Order", callback_data="doro_order")],
            [InlineKeyboardButton("⬅ Back", callback_data="orders")]
        ]
    return text, InlineKeyboardMarkup(buttons)
def baltena_menu(lang="en"):
    if lang == "am":
        buttons = [
            [InlineKeyboardButton("🌶️በርበሬ", callback_data="baltena_pepper")],
            [InlineKeyboardButton("🌶️ሚጥሚጣ", callback_data="baltena_chilliPepper")],
            [InlineKeyboardButton("🍲 ሽሮ", callback_data="baltena_shiro")],
            [InlineKeyboardButton("⬅ ተመለስ", callback_data="orders")]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("🌶️ Pepper", callback_data="baltena_pepper")],
            [InlineKeyboardButton("🌶️ chilliPepper", callback_data="baltena_chillipepper")],
            [InlineKeyboardButton("🍲 Shiro", callback_data="baltena_shiro")],
            [InlineKeyboardButton("⬅ Back", callback_data="orders")]
        ]
    return InlineKeyboardMarkup(buttons)

def quantity_menu(lang="en"):
    if lang == "am":
        buttons = [
            [InlineKeyboardButton("1", callback_data="qty_1"),
             InlineKeyboardButton("2", callback_data="qty_2"),
             InlineKeyboardButton("3", callback_data="qty_3")],
            [InlineKeyboardButton("4", callback_data="qty_4"),
             InlineKeyboardButton("5", callback_data="qty_5")],
            [InlineKeyboardButton("ሌላ ብዛት", callback_data="qty_other")],
            [InlineKeyboardButton("⬅️ ተመለስ", callback_data="back_to_item")]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("1", callback_data="qty_1"),
             InlineKeyboardButton("2", callback_data="qty_2"),
             InlineKeyboardButton("3", callback_data="qty_3")],
            [InlineKeyboardButton("4", callback_data="qty_4"),
             InlineKeyboardButton("5", callback_data="qty_5")],
            [InlineKeyboardButton("other amount", callback_data="qty_other")],
            [InlineKeyboardButton("⬅️ Back", callback_data="back_to_item")]
        ]
    return InlineKeyboardMarkup(buttons)

def Shiro_menu(lang="en"):
    if lang == "am":
        buttons =[ [InlineKeyboardButton("ቀይ ሽሮ", callback_data="red_shiro"),],
            [InlineKeyboardButton("ነጭ ሽሮ", callback_data="white_shiro"),],
            [InlineKeyboardButton("⬅ ተመለስ", callback_data="baltena")]]
    else:
        buttons = [[InlineKeyboardButton("keey Shiro", callback_data="red_shiro"),],
            [InlineKeyboardButton("nech Shiro", callback_data="white_shiro"),],
            [InlineKeyboardButton("⬅ Back", callback_data="baltena")]]
    return InlineKeyboardMarkup(buttons)
def keey_shiro_menu(lang="en"):
    if lang == "am":
        buttons = [
            [InlineKeyboardButton("1 ኪ.ግ", callback_data="kg_1"),
             InlineKeyboardButton("2 ኪ.ግ", callback_data="kg_2")],
            [InlineKeyboardButton("3 ኪ.ግ", callback_data="kg_3"),
             InlineKeyboardButton("4 ኪ.ግ", callback_data="kg_4")],
            [InlineKeyboardButton(" ሌላ ብዛት ያስገቡ", callback_data="kg_other")],
            [InlineKeyboardButton("⬅ ተመለስ", callback_data="baltena")]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("1 kg", callback_data="kg_1"),
             InlineKeyboardButton("2 kg", callback_data="kg_2")],
            [InlineKeyboardButton("3 kg", callback_data="kg_3"),
             InlineKeyboardButton("4 kg", callback_data="kg_4")],
            [InlineKeyboardButton(" Other amount", callback_data="kg_other")],
            [InlineKeyboardButton("⬅ Back", callback_data="baltena")]
        ]
    return InlineKeyboardMarkup(buttons)
def nech_shiro_menu(lang="en"):
    if lang == "am":
        buttons = [
            [InlineKeyboardButton("1 ኪ.ግ", callback_data="kg_1"),
             InlineKeyboardButton("2 ኪ.ግ", callback_data="kg_2")],
            [InlineKeyboardButton("3 ኪ.ግ", callback_data="kg_3"),
             InlineKeyboardButton("4 ኪ.ግ", callback_data="kg_4")],
            [InlineKeyboardButton(" ሌላ ብዛት ያስገቡ", callback_data="kg_other")],
            [InlineKeyboardButton("⬅ ተመለስ", callback_data="baltena")]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("1 kg", callback_data="kg_1"),
             InlineKeyboardButton("2 kg", callback_data="kg_2")],
            [InlineKeyboardButton("3 kg", callback_data="kg_3"),
             InlineKeyboardButton("4 kg", callback_data="kg_4")],
            [InlineKeyboardButton(" Other amount", callback_data="kg_other")],
            [InlineKeyboardButton("⬅ Back", callback_data="baltena")]
        ]
    return InlineKeyboardMarkup(buttons)
def pepper_menu(lang="en"):
    if lang == "am":
        buttons = [
            [InlineKeyboardButton("1 ኪ.ግ", callback_data="kg_1"),
             InlineKeyboardButton("2 ኪ.ግ", callback_data="kg_2")],
            [InlineKeyboardButton("3 ኪ.ግ", callback_data="kg_3"),
             InlineKeyboardButton("4 ኪ.ግ", callback_data="kg_4")],
            [InlineKeyboardButton(" ሌላ ብዛት ያስገቡ", callback_data="kg_other")],
            [InlineKeyboardButton("⬅ ተመለስ", callback_data="bread")]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("1 kg", callback_data="kg_1"),
             InlineKeyboardButton("2 kg", callback_data="kg_2")],
            [InlineKeyboardButton("3 kg", callback_data="kg_3"),
             InlineKeyboardButton("4 kg", callback_data="kg_4")],
            [InlineKeyboardButton(" Other amount", callback_data="kg_other")],
            [InlineKeyboardButton("⬅ Back", callback_data="bread")]
        ]
    return InlineKeyboardMarkup(buttons)
def chilliPepper_menu(lang="en"):
    if lang == "am":
        buttons = [
            [InlineKeyboardButton("1 ኪ.ግ", callback_data="kg_1"),
             InlineKeyboardButton("2 ኪ.ግ", callback_data="kg_2")],
            [InlineKeyboardButton("3 ኪ.ግ", callback_data="kg_3"),
             InlineKeyboardButton("4 ኪ.ግ", callback_data="kg_4")],
            [InlineKeyboardButton(" ሌላ ብዛት ያስገቡ", callback_data="kg_other")],
            [InlineKeyboardButton("⬅ ተመለስ", callback_data="baltena")]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("1 kg", callback_data="kg_1"),
             InlineKeyboardButton("2 kg", callback_data="kg_2")],
            [InlineKeyboardButton("3 kg", callback_data="kg_3"),
             InlineKeyboardButton("4 kg", callback_data="kg_4")],
            [InlineKeyboardButton(" Other amount", callback_data="kg_other")],
            [InlineKeyboardButton("⬅ Back", callback_data="baltena")]
        ]
    return InlineKeyboardMarkup(buttons)

def contact_menu(lang="en"):
    if lang == "am":
        buttons = [
            [InlineKeyboardButton("📞 ይደዉሉ", url="tel:+251910590715")],
            [InlineKeyboardButton("⬅ ተመለስ", callback_data="back_main")]]
    else:
        buttons = [
            [InlineKeyboardButton("📞 Call Us", url="tel:+251910590715")],
            [InlineKeyboardButton("⬅ Back", callback_data="back_main")]]
    return InlineKeyboardMarkup(buttons)