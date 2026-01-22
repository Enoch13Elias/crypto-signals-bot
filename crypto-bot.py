#!/usr/bin/env python3
"""
GitHub-hosted Crypto Bot - 100% FREE
Educational content only - Not financial advice
"""
import os
import requests
from datetime import datetime

# Get secrets from GitHub Actions environment
BOT_TOKEN = os.environ.get('BOT_TOKEN', '8436110181:AAH6wBaom_mp53wmt22KBriQPTVWscSf-kY')
CHANNEL_ID = os.environ.get('CHANNEL_ID', '-1003672646767')

def get_crypto_prices():
    """Get crypto prices from free API"""
    try:
        url = "https://api.coingecko.com/api/v3/simple/price"
        params = {
            'ids': 'bitcoin,ethereum,solana',
            'vs_currencies': 'usd',
            'include_24hr_change': 'true'
        }
        response = requests.get(url, params=params, timeout=10)
        return response.json()
    except:
        return None

def send_telegram_message():
    """Send message to Telegram channel"""
    prices = get_crypto_prices()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M UTC")
    
    if prices:
        btc_price = prices['bitcoin']['usd']
        btc_change = prices['bitcoin']['usd_24h_change']
        eth_price = prices['ethereum']['usd']
        eth_change = prices['ethereum']['usd_24h_change']
        
        message = f"""
🚀 *DAILY CRYPTO SIGNAL*
📅 {current_time}

*Hosted on GitHub - 100% FREE*

*₿ BITCOIN*
Price: ${btc_price:,.2f}
24h Change: {btc_change:+.2f}%

*Ξ ETHEREUM*
Price: ${eth_price:,.2f}
24h Change: {eth_change:+.2f}%

*📊 MARKET OVERVIEW*
• Total Cap: ~$1.7T
• BTC Dominance: ~52%
• Sentiment: Neutral

*🎯 KEY LEVELS*
• BTC: $45,000 support
• ETH: $2,500 resistance

*💡 INSIGHT*
Markets consolidating. Good time for research.

⚠️ *DISCLAIMER*
_This is EDUCATIONAL content only._
_NOT financial advice. Always DYOR._

🤖 *Powered by GitHub Actions*
⚡ Running 100% FREE
"""
    else:
        message = f"""
📊 *CRYPTO UPDATE*
📅 {current_time}

Market data temporarily unavailable.
Check back later for full analysis.

⚠️ Educational content only.

🤖 Powered by GitHub Actions (FREE)
"""
    
    # Send to Telegram
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHANNEL_ID,
        "text": message,
        "parse_mode": "Markdown",
        "disable_web_page_preview": True
    }
    
    try:
        response = requests.post(url, json=payload, timeout=10)
        data = response.json()
        
        if data.get("ok"):
            print(f"✅ Message sent successfully!")
            print(f"   Time: {current_time}")
            return True
        else:
            print(f"❌ Telegram error: {data.get('description')}")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    print("🤖 GitHub Crypto Bot Starting...")
    success = send_telegram_message()
    
    if success:
        print("\n🎉 SUCCESS! Check your Telegram channel.")
        print("🤖 Bot is running 100% FREE on GitHub!")
    else:
        print("\n❌ Failed to send message")
        print("💡 Check your bot token and channel ID")
