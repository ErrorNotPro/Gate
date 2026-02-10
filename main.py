import requests
from requests.exceptions import RequestException, Timeout
from bs4 import BeautifulSoup
import telebot
import os
import time

# Gateways and platforms list
gateways = [
    "stripe", "paypal", "square", "amazon pay", "braintree",
    "authorize_net", "authorize", "authorize.net", "2checkout", "adyen", "worldpay",
    "google pay", "apple pay", "payza", "merchant account",
    "webhook", "cryptocurrency", "sezzle", "klarna",
    "afterpay", "blue snap", "payoneer", "@ERR0R9", "razorpay",
    "alipay", "paytm", "venmo", "zelle",
    "checkout.com", "mollie", "trustly", "payu",
    "dwolla", "quaderno", "recurly", "judo",
    "wepay", "spree", "rapyd", "paymentwall",
    "bill.com", "fatture in cloud", "epay",
    "linkpoint", "cybersource", "transaction express",
    "yield", "paysafe", "finaro", "go2pay",
    "eway", "verifone", "bluefin", "sagepay", 
    "klarna checkout"
]

platforms = [
    "woocommerce", "shopify", "magento", "bigcommerce",
    "prestashop", "wix", "squarespace", "opencart",
    "zen cart", "oscommerce", "drupal commerce", "@ERR0R9", "jimdo",
    "volusion", "weebly", "shopify plus", "3dcart",
    "ecwid", "kartra", "sellfy", "gumroad",
    "thrivecart", "spree commerce", "sylius", "americommerce",
    "big cartel", "artstorefronts", "woo bookings",
    "x-cart", "1shoppingcart", "solidus"
]

bot = telebot.TeleBot('8128429145:AAHFQP69Y14D765K5TcnpxfvrIk4PSS1ySI')

def detect_payment_gateways_and_captcha(domain):
    try:
        if not domain.startswith("http://") and not domain.startswith("https://"):
            domain = "http://" + domain

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'
        }

        response = requests.get(domain, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')

        payment_gateway_results = []
        detected_platform = "None"
        captcha = False
        cloudflare = False
        graphql = False

        if 'recaptcha' in response.text.lower() or 'hcaptcha' in response.text.lower() or 'captcha' in response.text.lower():
            captcha = True

        if 'cloudflare' in response.text.lower():
            cloudflare = True

        if 'graphql' in response.text.lower():
            graphql = True

        for gateway in gateways:
            if gateway in response.text.lower():
                payment_gateway_results.append(gateway.capitalize())

        for platform in platforms:
            if platform in response.text.lower():
                detected_platform = platform.capitalize()
                break

        error_logs = "None"
        output_status = response.status_code

    except Timeout:
        error_logs = "Timeout error."
        payment_gateway_results = []
        detected_platform = "None"
        captcha = "Unknown"
        cloudflare = "Unknown"
        graphql = "Unknown"
        output_status = "None"
        response = None
    except RequestException as e:
        error_logs = f"Request error: {str(e)}"
        payment_gateway_results = []
        detected_platform = "None"
        captcha = "Unknown"
        cloudflare = "Unknown"
        graphql = "Unknown"
        output_status = "None"
        response = None

    if response is not None and output_status == 200:
        return True, (
            f"🔍 𝐆𝐚𝐭𝐞𝐰𝐚𝐲𝐬 𝐅𝐞𝐭𝐜𝐡𝐞𝐝 ✅\n"
            f"➜ 𝙐𝙍𝙇: {domain}\n"
            f"➜ 𝙋𝙖𝙮𝙢𝙚𝙣𝙩 𝙂𝙖𝙩𝙚𝙬𝙖𝙮𝙨: {', '.join(payment_gateway_results) if payment_gateway_results else 'None'}\n"
            f"➜ 𝘾𝙖𝙥𝙩𝙘𝙝𝙖: {'True 😢' if captcha else 'False 🔥'}\n"
            f"➜ 𝘾𝙡𝙤𝙪𝙙𝙛𝙡𝙖𝙧𝙚: {'True 😢' if cloudflare else 'False 🔥'}\n"
            f"➜ 𝙂𝙧𝙖𝙥𝙝𝙌𝙇: {'True' if graphql else 'False'}\n"
            f"➜ 𝙋𝙡𝙖𝙩𝙛𝙤𝙧𝙢: {detected_platform}\n"
            f"➜ 𝙀𝙧𝙧𝙤𝙧 𝙇𝙤𝙜𝙨: {error_logs}\n"
            f"➜ 𝙎𝙩𝙖𝙩𝙪𝙨: {output_status}\n"
            "𝗕𝗼𝘁 𝗯𝘆: @ERR0R9"
        )
    else:
        return False, (
            f"❌ 𝙁𝙖𝙞𝙡𝙚𝙙 𝙏𝙤 𝘾𝙝𝙚𝙘𝙠\n"
            f"➜ 𝙐𝙍𝙇: {domain}\n"
            f"➜ 𝙀𝙧𝙧𝙤𝙧: {error_logs}\n"
            f"➜ 𝙎𝙩𝙖𝙩𝙪𝙨: {output_status}\n"
            "𝗕𝗼𝘁 𝗯𝘆: @ERR0R9"
        )

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "𝚆𝚎𝚕𝚌𝚘𝚖𝚎! 𝚄𝚜𝚎 /𝚞𝚛𝚕 𝙤𝙧 .𝚞𝚛𝚕 𝙘𝙤𝙢𝙢𝙖𝙣𝙙 𝙩𝙤 𝙘𝙝𝙚𝙘𝙠 𝙙𝙤𝙢𝙖𝙞𝙣𝙨.\n\n📄 Upload .txt file to check multiple.")

@bot.message_handler(commands=['url'])
def url_command(message):
    parts = message.text.split(' ', 1)
    if len(parts) > 1:
        domain = parts[1].strip()
        _, result = detect_payment_gateways_and_captcha(domain)
        bot.reply_to(message, result)
    else:
        bot.reply_to(message, "⚠️ 𝙐𝙨𝙚 𝙡𝙞𝙠𝙚: /url example.com")

@bot.message_handler(func=lambda message: message.text.startswith('.url'))
def dot_url_handler(message):
    domain = message.text[4:].strip()
    if domain:
        _, result = detect_payment_gateways_and_captcha(domain)
        bot.reply_to(message, result)
    else:
        bot.reply_to(message, "⚠️ 𝘼𝙙𝙙 𝙙𝙤𝙢𝙖𝙞𝙣 𝙖𝙛𝙩𝙚𝙧 .url")

@bot.message_handler(content_types=['document'])
def handle_txt_file(message):
    if message.document.mime_type == 'text/plain' and message.document.file_name.endswith('.txt'):
        try:
            file_info = bot.get_file(message.document.file_id)
            downloaded_file = bot.download_file(file_info.file_path)

            file_path = f"{message.chat.id}_temp.txt"
            with open(file_path, 'wb') as f:
                f.write(downloaded_file)

            with open(file_path, 'r') as f:
                lines = [line.strip() for line in f if line.strip()]
                domains = list(dict.fromkeys(lines))  # Remove duplicates

            approved = 0
            declined = 0
            bot.reply_to(message, f"📄 File received. Total unique domains: {len(domains)}. Checking...")

            for domain in domains:
                success, result = detect_payment_gateways_and_captcha(domain)

                if (
                    "➜ 𝘾𝙖𝙥𝙩𝙘𝙝𝙖: False 🔥" in result and
                    "➜ 𝘾𝙡𝙤𝙪𝙙𝙛𝙡𝙖𝙧𝙚: False 🔥" in result
                ):
                    if success:
                        approved += 1
                    else:
                        declined += 1
                    bot.send_message(message.chat.id, result)
                    time.sleep(1.2)
                else:
                    declined += 1  # Count filtered sites as declined

            summary = (
                "📊 𝐌𝐚𝐬𝐬 𝐂𝐡𝐞𝐜𝐤 𝐒𝐮𝐦𝐦𝐚𝐫𝐲\n"
                "━━━━━━━━━━━━━━\n"
                f"➜ 𝙏𝙤𝙩𝙖𝙡: {len(domains)}\n"
                f"➜ 𝘼𝙥𝙥𝙧𝙤𝙫𝙚𝙙 (Clean only): {approved}\n"
                f"➜ 𝘿𝙚𝙘𝙡𝙞𝙣𝙚𝙙 / Skipped: {declined}\n"
                "𝗕𝗼𝘁 𝗯𝘆: @ERR0R9"
            )
            bot.send_message(message.chat.id, summary)

            os.remove(file_path)

        except Exception as e:
            bot.reply_to(message, f"⚠️ Error: {e}")
    else:
        bot.reply_to(message, "❌ Please upload a valid `.txt` file with domains line by line.")

bot.polling()
