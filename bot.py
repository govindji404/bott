# bottdef get_result(last_two):
    rules = {
        "05": "SMALL",
        "50": "SMALL",
        "56": "BIG",
        "65": "BIG",
        "00": "SMALL",
        "11": "BIG",
        "22": "SMALL",
        "33": "BIG",
        "44": "BIG",
        "66": "BIG",
        "77": "SMALL",
        "88": "BIG",
        "99": "BIG",
        "01": "SMALL",
        "10": "SMALL",
        "79": "SMALL",
        "97": "SMALL",
        "46": "BIG",
        "64": "BIG",
        "12": "BIG",
        "21": "BIG",
        "83": "SMALL",
        "38": "SMALL",
    }

    # 55 = random
    if last_two == "55":
        return random.choice(["BIG", "SMALL"])

    # Fixed rules
    if last_two in rules:
        return rules[last_two]

    # Baaki combinations = random
    return random.choice(["BIG", "SMALL"])


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎮 Practice Period Bot\n\n"
        "Is format me bhejo:\n"
        "235 7,3\n\n"
        "235 = Period Number\n"
        "7,3 = Tumhare diye hue 2 digits\n\n"
        "Bot 73 ko rules se check karega."
    )


async def period(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    parts = text.split()

    if len(parts) != 2:
        await update.message.reply_text(
            "❌ Galat format.\n\n"
            "Example:\n"
            "235 7,3"
        )
        return

    period_number = parts[0]
    digits = parts[1].replace(",", "")

    # Period exactly 3 digits
    if not period_number.isdigit() or len(period_number) != 3:
        await update.message.reply_text(
            "❌ Period number 3 digit ka hona chahiye.\n\n"
            "Example: 235"
        )
        return

    # Exactly 2 digits
    if not digits.isdigit() or len(digits) != 2:
        await update.message.reply_text(
            "❌ Last two digits sahi format me bhejo.\n\n"
            "Example: 7,3"
        )
        return

    result = get_result(digits)

    await update.message.reply_text(
        f"🎯 Practice Result\n\n"
        f"Period: {period_number}\n"
        f"Your digits: {digits[0]}, {digits[1]}\n"
        f"Checked number: {digits}\n\n"
        f"Result: {result}\n\n"
        f"⚠️ Practice mode — virtual game only."
    )


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, period))

print("Bot started...")
app.run_polling()
