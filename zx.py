import telebot
import time
import threading
import random

# 🔹 এখানে আপনার টোকেন বসান
TOKEN = "আপনার_টেলিগ্রাম_বট_টোকেন"
bot = telebot.TeleBot(TOKEN)

# ✅ র্যান্ডম রিপ্লাই লিস্ট (৫০+ মজার উত্তর)
RANDOM_REPLIES = [
    "আমি কিছু জানি না! 😆",
    "তুমি কি সিরিয়াস? 🤔",
    "ভাই, একটু ভাবো তো! 😜",
    "জানি না, কিন্তু মজার প্রশ্ন! 😂",
    "আমি কি উত্তর দেবো? 🧐",
    "দেখি, একটু ভেবে দেখি! 😁",
    "হুমম... ভালো প্রশ্ন! 🔥",
    "এটা জানতে হলে NASA-তে চাকরি নাও! 🚀",
    "আমি AI, কিন্তু আমিও কনফিউজড! 😅",
    "তোমার প্রশ্ন শুনে আমার প্রসেসর ওভারলোড! 🧠💥",
    "ভাই, গুগলে সার্চ করে দেখো! 🧐",
    "তুমি আমাকে বোকা ভাবো? 😡",
    "আমি কি গণিতের শিক্ষক নাকি? 😆",
    "এটা আমার ডাটাবেজে নেই! 🔍",
    "হয়তো তুমি নিজেই উত্তর জানো! 🤔",
    "উত্তর পেলে আমাকে জানিও! 😜",
    "তোমার প্রশ্নের উত্তর এখনো তৈরি হয়নি! ⏳",
    "আমার কনফিগারেশন আপডেট করতে হবে! 😅",
    "কফি খেয়ে আসি, তারপর উত্তর দেই! ☕",
    "কেনো, তুমি নিজেই কি জানো না? 🤨",
    "আচ্ছা, আমি গুগলিং করছি... এক মিনিট! ⏳",
    "ভাই, আমি কি জাদুকর? 🧙‍♂️",
    "তুমি কি আমায় টেস্ট করছো? 😏",
    "আমি জানলে Nobel Prize পেয়ে যেতাম! 🏆",
    "আকাশের তারা গণনা করো, উত্তর পেয়ে যাবে! 🌟",
    "তুমি প্রশ্ন করলে, কিন্তু উত্তর কে দেবে? 😝",
    "এটার উত্তর ৪২! (Hitchhiker's Guide 🤣)",
    "আমি কি এত বুদ্ধিমান নাকি? 😜",
    "একটু ব্রেক দাও, CPU গরম হয়ে গেছে! 🔥",
    "জানি না, কিন্তু ভালো প্রশ্ন! 😂",
    "তোমার প্রশ্ন শুনে আমি স্তব্ধ! 😳",
    "আমি জানি, কিন্তু বলবো না! 😏",
    "এটার উত্তর দিতে হলে AI God হতে হবে! 🤖",
    "আমি উত্তর দিতে গিয়ে হার্ডওয়্যার ক্র্যাশ করবো! 💀",
    "উত্তর পেতে হলে আমাকে একটা আইসক্রিম খাওয়াও! 🍦",
    "ভাই, উত্তর দিতে পারলে আমি Elon Musk হয়ে যেতাম! 🚀",
    "আমি কি টাইম মেশিন? ⏳",
    "একটা সুন্দর প্রশ্ন করো, তারপর উত্তর দিবো! 😆",
    "এটা বোঝার জন্য আমাকে Python শিখতে হবে! 🐍",
    "তুমি কি আমার ডেভেলপার? 😏",
    "ভাই, উত্তর দিলেই কি সব সমস্যার সমাধান হবে? 🤣",
    "গুগল স্যার এর কাছে যাও! 🤓",
    "আমার ক্যাশে মেমোরি ফুল হয়ে গেছে! 🧠💥",
    "আমি শুধু ChatGPT-এর ভাই, Google নয়! 😆",
    "ব্রেক দাও ভাই, একটু ঘুমাই! 😴",
    "এটা বুঝতে হলে ক্যালকুলেটর লাগবে! 🧮",
    "তুমি কি সত্যিই উত্তর চাও? নাকি মজা করছো? 😂",
    "ভাই, উত্তর দিতে গেলে বেতন বাড়াতে হবে! 💰",
    "এটা আমার বায়োসে নেই! 🤖",
    "যদি উত্তর জানতাম, তাহলে বিখ্যাত হয়ে যেতাম! 🎉",
    "আমি কি গণিতজ্ঞ নাকি কবি? 🤔",
    "তোমার প্রশ্ন এত কঠিন যে, আমার সার্ভার ডাউন হয়ে যাবে! 💥"
]

# ✅ মেসেজ ডিলিট করার ফাংশন
def delete_message_later(chat_id, message_id, delay):
    time.sleep(delay)
    try:
        bot.delete_message(chat_id, message_id)
    except:
        pass  

# ✅ গ্রুপে কেউ মেসেজ দিলেই বট রিপ্লাই দেবে
@bot.message_handler(func=lambda message: message.chat.type in ["group", "supergroup"])
def auto_reply(message):
    try:
        chat_id = message.chat.id

        # 🔹 বট থেকে র্যান্ডম রিপ্লাই পাঠানো
        random_reply = random.choice(RANDOM_REPLIES)
        sent_msg = bot.send_message(chat_id, f"🤖 **বটের উত্তর:** {random_reply}", parse_mode="Markdown")
        
        # 🔹 ৩০ সেকেন্ড পরে বটের মেসেজ অটো-ডিলিট
        threading.Thread(target=delete_message_later, args=(chat_id, sent_msg.message_id, 30)).start()

    except Exception as e:
        bot.send_message(message.chat.id, f"⚠️ কিছু ভুল হয়েছে: {e}")

# ✅ বট চালু রাখা
bot.polling()