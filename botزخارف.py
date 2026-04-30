
# pip install pyTelegramBotAPI

import telebot
import random

TOKEN = "8667305559:AAF1yLYIHvXs5zUGf0b9Zd0MezIV7mV5jDM"

bot = telebot.TeleBot(TOKEN)

# زخارف البداية والنهاية
prefixes = [
    "꧁", "𖤍", "『", "༺", "★", "么", "彡", "ツ", "✧", "۝"
]

suffixes = [
    "꧂", "𖤍", "』", "༻", "★", "々", "彡", "ツ", "✧", "۝"
]

# حروف مزخرفة
fonts = {
    "a": ["𝓪", "𝐚", "𝔞", "𝕒", "α"],
    "b": ["𝓫", "𝐛", "𝔟", "𝕓", "в"],
    "c": ["𝓬", "𝐜", "𝔠", "𝕔", "¢"],
    "d": ["𝓭", "𝐝", "𝔡", "𝕕", "∂"],
    "e": ["𝓮", "𝐞", "𝔢", "𝕖", "є"],
    "f": ["𝓯", "𝐟", "𝔣", "𝕗", "ƒ"],
    "g": ["𝓰", "𝐠", "𝔤", "𝕘", "ɢ"],
    "h": ["𝓱", "𝐡", "𝔥", "𝕙", "н"],
    "i": ["𝓲", "𝐢", "𝔦", "𝕚", "ɪ"],
    "j": ["𝓳", "𝐣", "𝔧", "𝕛", "נ"],
    "k": ["𝓴", "𝐤", "𝔨", "𝕜", "κ"],
    "l": ["𝓵", "𝐥", "𝔩", "𝕝", "ℓ"],
    "m": ["𝓶", "𝐦", "𝔪", "𝕞", "м"],
    "n": ["𝓷", "𝐧", "𝔫", "𝕟", "и"],
    "o": ["𝓸", "𝐨", "𝔬", "𝕠", "σ"],
    "p": ["𝓹", "𝐩", "𝔭", "𝕡", "ρ"],
    "q": ["𝓺", "𝐪", "𝔮", "𝕢", "զ"],
    "r": ["𝓻", "𝐫", "𝔯", "𝕣", "я"],
    "s": ["𝓼", "𝐬", "𝔰", "𝕤", "ѕ"],
    "t": ["𝓽", "𝐭", "𝔱", "𝕥", "т"],
    "u": ["𝓾", "𝐮", "𝔲", "𝕦", "υ"],
    "v": ["𝓿", "𝐯", "𝔳", "𝕧", "ν"],
    "w": ["𝔀", "𝐰", "𝔴", "𝕨", "ω"],
    "x": ["𝔁", "𝐱", "𝔵", "𝕩", "χ"],
    "y": ["𝔂", "𝐲", "𝔶", "𝕪", "γ"],
    "z": ["𝔃", "𝐳", "𝔷", "𝕫", "z"]
}

def decorate_name(name):
    results = []

    for _ in range(10):
        decorated = ""

        for char in name.lower():
            if char in fonts:
                decorated += random.choice(fonts[char])
            else:
                decorated += char

        pre = random.choice(prefixes)
        suf = random.choice(suffixes)

        final = f"{pre}{decorated}{suf}"
        results.append(final)

    return "\n".join(results)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(
        message,
        "🔥 ارسل اسمك و رح ازخرفه لك بـ 10 اشكال نادرة 👽"
    )

@bot.message_handler(func=lambda message: True)
def handle(message):
    name = message.text
    decorated = decorate_name(name)

    bot.reply_to(message, decorated)

print("BOT IS RUNNING 🔥")
bot.infinity_polling()
