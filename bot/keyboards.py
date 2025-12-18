from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def language_menu():
    buttons = [
        [InlineKeyboardButton("አማርኛ", callback_data="lang_am")],
        [InlineKeyboardButton("English", callback_data="lang_en")]
    ]
    return InlineKeyboardMarkup(buttons)

def main_menu(lang="en"):
    if lang == "am":
        buttons = [
            [InlineKeyboardButton("🛒 ለማዝ", callback_data="to_order")],
            [InlineKeyboardButton("📞 ያግኙን", callback_data="contact")]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("🛒 to Order", callback_data="to_order")],
            [InlineKeyboardButton("📞 Contact", callback_data="contact")]
        ]
    return InlineKeyboardMarkup(buttons)
def to_order_menu(lang="en"):
    if lang == "am":
        buttons = [
            [InlineKeyboardButton("🥞 እንጀራ", callback_data="injera")],
            [InlineKeyboardButton("🍞 ዳቦ", callback_data="bread")],
            [InlineKeyboardButton("🍲 አገልግል", callback_data="agelgel")],
            [InlineKeyboardButton("🍗 ዶሮ ወጥ", callback_data="doro_wot")],
            [InlineKeyboardButton("🛍️ ባልትና", callback_data="baltena")],
            [InlineKeyboardButton("⬅ ተመለስ", callback_data="back_main")]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("🥞 Injera", callback_data="injera")],
            [InlineKeyboardButton("🍞 Bread", callback_data="bread")],
            [InlineKeyboardButton("🍲 Agelgel", callback_data="agelgel")],
            [InlineKeyboardButton("🍗 Doro Wot", callback_data="doro_wot")],
            [InlineKeyboardButton("🛍️ Baltena", callback_data="baltena")],
            [InlineKeyboardButton("⬅ Back", callback_data="back_main")]
        ]
    return InlineKeyboardMarkup(buttons)
def injera_menu(lang="en"):
    if lang == "am":
        buttons = [
            [InlineKeyboardButton(" ነጭ, የአንዱ ዋጋ:35  ", callback_data="injera_white")],
            [InlineKeyboardButton("ጥቁር, የአንዱዋጋ:35", callback_data="injera_black")],
            [InlineKeyboardButton(" ሁለቱም, የአንዱ ዋጋ:35", callback_data="injera_both")],
            [InlineKeyboardButton("⬅ ተመለስ", callback_data="to_order")]
        ]
    else:
        buttons = [
            [InlineKeyboardButton(" White Injera, price: 35 ETB per each", callback_data="injera_white")],
            [InlineKeyboardButton("Black Injera, price: 35 ETB per each", callback_data="injera_black")],
            [InlineKeyboardButton(" Both, price: 35 ETB per each", callback_data="injera_both")],
            [InlineKeyboardButton("⬅ Back", callback_data="to_order")]
        ]
    return InlineKeyboardMarkup(buttons)
def white_injera_menu(lang="en"):
    if lang == "am":
        buttons = [
            [InlineKeyboardButton("ድርቆሽ ያልሆነ", callback_data="normal_injera")],
            [InlineKeyboardButton("ድርቆሽ", callback_data="hay_injera")],
            [InlineKeyboardButton("⬅ ተመለስ", callback_data="injera")]
        ]
             
    else:
        buttons = [
            [InlineKeyboardButton("Normal", callback_data="normal_injera")],
            [InlineKeyboardButton("Hay", callback_data="hay_injera")],
            [InlineKeyboardButton("⬅ Back", callback_data="injera")]
        ]
    return InlineKeyboardMarkup(buttons)
def black_injera_menu(lang="en"):
    if lang == "am":
        buttons = [
            [InlineKeyboardButton("ድርቆሽ ያልሆነ", callback_data="normal_injera")],
            [InlineKeyboardButton("ድርቆሽ", callback_data="hay_injera")],
            [InlineKeyboardButton("⬅ ተመለስ", callback_data="injera")]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("Normal", callback_data="normal_injera")],
            [InlineKeyboardButton("Hay", callback_data="hay_injera")],
            [InlineKeyboardButton("⬅ Back", callback_data="injera")]
        ]
    return InlineKeyboardMarkup(buttons)
def hay_injera_menu(lang="en"):
    if lang == "am":
        buttons = [
            [InlineKeyboardButton("1 ኪ.ግ", callback_data="kg_1"),
             InlineKeyboardButton("2 ኪ.ግ", callback_data="kg_2")],
            [InlineKeyboardButton("3 ኪ.ግ", callback_data="kg_3"),
             InlineKeyboardButton("4 ኪ.ግ", callback_data="kg_4")],
            [InlineKeyboardButton(" ሌላ ብዛት ያስገቡ", callback_data="kg_other")],
            [InlineKeyboardButton("⬅ ተመለስ", callback_data="injera")]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("1 kg", callback_data="kg_1"),
             InlineKeyboardButton("2 kg", callback_data="kg_2")],
            [InlineKeyboardButton("3 kg", callback_data="kg_3"),
             InlineKeyboardButton("4 kg", callback_data="kg_4")],
            [InlineKeyboardButton(" Other amount", callback_data="kg_other")],
            [InlineKeyboardButton("⬅ Back", callback_data="injera")]
        ]
    return InlineKeyboardMarkup(buttons)
def normal_injera_menu(lang="en"):
    if lang == "am":
        buttons = [
            
            [InlineKeyboardButton("ብዛት ያስገቡ", callback_data="other_amount")],
            [InlineKeyboardButton("⬅ ተመለስ", callback_data="injera")]
        ]
    else:
        buttons = [
            [InlineKeyboardButton(" enter amount", callback_data="other_amount")],
            [InlineKeyboardButton("⬅ Back", callback_data="injera")]
        ]
    return InlineKeyboardMarkup(buttons)

def bread_menu(lang="en"):
    if lang == "am":
        buttons = [
            [InlineKeyboardButton(" ፍርኖ ዳቦ", callback_data="bread_white")],
            [InlineKeyboardButton(" ስንዴ ዳቦ", callback_data="bread_wheat")],
            [InlineKeyboardButton("⬅ ተመለስ", callback_data="to_order")]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("White Bread", callback_data="bread_white")],
            [InlineKeyboardButton(" Wheat Bread", callback_data="bread_wheat")],
            [InlineKeyboardButton("⬅ Back", callback_data="to_order")]
        ]
    return InlineKeyboardMarkup(buttons)
def white_bread_menu(lang="en"):
    if lang == "am":
        buttons = [
            [InlineKeyboardButton("1 ኪ.ግ, ዋጋ: 200 ብር", callback_data="kg_1"),
             InlineKeyboardButton("2 ኪ.ግ, ዋጋ: 400 ብር", callback_data="kg_2")],
            [InlineKeyboardButton("3 ኪ.ግ, ዋጋ: 600 ብር", callback_data="kg_3"),
             InlineKeyboardButton("4 ኪ.ግ, ዋጋ: 800 ብር", callback_data="kg_4")],
            [InlineKeyboardButton("5 ኪ.ግ, ዋጋ: 1000 ብር", callback_data="kg_5"),
             InlineKeyboardButton("6 ኪ.ግ, ዋጋ: 1200 ብር", callback_data="kg_6")],
            [InlineKeyboardButton("⬅ ተመለስ", callback_data="bread")]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("1 kg, Price: 200 ETB", callback_data="kg_1"),
             InlineKeyboardButton("2 kg, Price: 400 ETB", callback_data="kg_2")],
            [InlineKeyboardButton("3 kg, Price: 600 ETB", callback_data="kg_3"),
             InlineKeyboardButton("4 kg, Price: 800 ETB", callback_data="kg_4")],
            [InlineKeyboardButton("5 kg, Price: 1000 ETB", callback_data="kg_5"),
             InlineKeyboardButton("6 kg, Price: 1200 ETB", callback_data="kg_6")],
            [InlineKeyboardButton("⬅ Back", callback_data="bread")]
        ]
    return InlineKeyboardMarkup(buttons)
def wheat_bread_menu(lang="en"):
    if lang == "am":
        buttons = [
            [InlineKeyboardButton("1 ኪ.ግ, ዋጋ: 200 ብር", callback_data="kg_1"),
             InlineKeyboardButton("2 ኪ.ግ, ዋጋ: 500 ብር", callback_data="kg_2")],
            [InlineKeyboardButton("3 ኪ.ግ, ዋጋ: 700 ብር", callback_data="kg_3"),
             InlineKeyboardButton("4 ኪ.ግ, ዋጋ: 900 ብር", callback_data="kg_4")],
            [InlineKeyboardButton("5 ኪ.ግ, ዋጋ: 1000 ብር", callback_data="kg_5"),
             InlineKeyboardButton("6 ኪ.ግ, ዋጋ: 1200 ብር", callback_data="kg_6")],
            [InlineKeyboardButton("⬅ ተመለስ", callback_data="bread")]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("1 kg, Price: 200 ETB", callback_data="kg_1"),
             InlineKeyboardButton("2 kg, Price: 500 ETB", callback_data="kg_2")],
            [InlineKeyboardButton("3 kg, Price: 700 ETB", callback_data="kg_3"),
             InlineKeyboardButton("4 kg, Price: 900 ETB", callback_data="kg_4")],
            [InlineKeyboardButton("5 kg, Price: 1000 ETB", callback_data="kg_5"),
             InlineKeyboardButton("6 kg, Price: 1200 ETB", callback_data="kg_6")],
            [InlineKeyboardButton("⬅ Back", callback_data="bread")]
        ]
    return InlineKeyboardMarkup(buttons)


def agelgel_menu(lang="en"):
    if lang == "am":
        buttons = [
            [InlineKeyboardButton("🥗 ፆም, ዋጋ: 3000 ብር", callback_data="agelgel_fasting")],
            [InlineKeyboardButton("🍛 የፍስግ, ዋጋ: 6000 ብር", callback_data="agelgel_non_fasting")],
            [InlineKeyboardButton("⭐ ልዩ", callback_data="agelgel_special")],
            [InlineKeyboardButton("⬅ ተመለስ", callback_data="to_order")]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("🥗 Fasting, Price: 3000 ETB", callback_data="agelgel_fasting")],
            [InlineKeyboardButton("🍛 Non-Fasting, Price: 6000 ETB", callback_data="agelgel_non_fasting")],
            [InlineKeyboardButton("⭐ Special", callback_data="agelgel_special")],
            [InlineKeyboardButton("⬅ Back", callback_data="to_order")]
        ]

    return InlineKeyboardMarkup(buttons)

def doro_wot_menu(lang="en"):
    if lang == "am":
        buttons = [
            [InlineKeyboardButton("🛒 ይትዕዛዙ, ዋጋ: 4500 ብር", callback_data="doro_confirm")],
            [InlineKeyboardButton("⬅ ተመለስ", callback_data="to_order")]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("🛒 Order, price: 4500 ETB", callback_data="doro_confirm")],
            [InlineKeyboardButton("⬅ Back", callback_data="to_order")]
        ]
    return InlineKeyboardMarkup(buttons)
def baltena_menu(lang="en"):
    if lang == "am":
        buttons = [
            [InlineKeyboardButton("🌶️በርበሬ", callback_data="pepper")],
            [InlineKeyboardButton("🌶️ሚጥሚጣ", callback_data="chillipepper")],
            [InlineKeyboardButton("🍲 ሽሮ", callback_data="shiro")],
            [InlineKeyboardButton("⬅ ተመለስ", callback_data="to_order")]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("🌶️ Pepper", callback_data="pepper")],
            [InlineKeyboardButton("🌶️ chillipepper", callback_data="chillipepper")],
            [InlineKeyboardButton("🍲 Shiro", callback_data="shiro")],
            [InlineKeyboardButton("⬅ Back", callback_data="to_order")]
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
        buttons =[ [InlineKeyboardButton("ቀይ ሽሮ", callback_data="keey_shiro"),],
            [InlineKeyboardButton("ነጭ ሽሮ", callback_data="white_shiro"),],
            [InlineKeyboardButton("⬅ ተመለስ", callback_data="baltena")]]
    else:
        buttons = [[InlineKeyboardButton("keey Shiro", callback_data="keey_shiro"),],
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
def chillipepper_menu(lang="en"):
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