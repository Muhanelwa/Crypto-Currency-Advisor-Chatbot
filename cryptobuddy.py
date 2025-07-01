#!/usr/bin/env python3
"""
CryptoBuddy - Your AI-Powered Cryptocurrency Advisor
A rule-based chatbot that provides investment advice based on profitability and sustainability
"""

import re
import random
from datetime import datetime

class CryptoBuddy:
    def __init__(self):
        self.name = "CryptoBuddy"
        self.crypto_db = {
            "Bitcoin": {
                "symbol": "BTC",
                "price_trend": "rising",
                "market_cap": "high",
                "energy_use": "high",
                "sustainability_score": 3,
                "current_price": "$45,000",
                "description": "The original cryptocurrency with massive adoption"
            },
            "Ethereum": {
                "symbol": "ETH",
                "price_trend": "stable",
                "market_cap": "high",
                "energy_use": "medium",
                "sustainability_score": 6,
                "current_price": "$2,800",
                "description": "Smart contract platform with DeFi ecosystem"
            },
            "Cardano": {
                "symbol": "ADA",
                "price_trend": "rising",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 8,
                "current_price": "$0.45",
                "description": "Proof-of-stake blockchain focused on sustainability"
            },
            "Solana": {
                "symbol": "SOL",
                "price_trend": "rising",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 7,
                "current_price": "$95",
                "description": "High-speed blockchain for DApps and DeFi"
            },
            "Polkadot": {
                "symbol": "DOT",
                "price_trend": "stable",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 8,
                "current_price": "$7.50",
                "description": "Multi-chain protocol enabling interoperability"
            }
        }
        
        self.greetings = [
            "Hey there! 👋 Ready to explore the crypto universe?",
            "Welcome to CryptoBuddy! 🚀 Let's find your perfect crypto match!",
            "Hello, crypto explorer! 🌟 I'm here to help you make smart decisions!"
        ]
        
        self.farewells = [
            "Happy investing! Remember: DYOR (Do Your Own Research)! 💎",
            "Crypto adventures await! Stay safe out there! 🛡️",
            "May your portfolio be green and your investments wise! 🌱📈"
        ]

    def greet(self):
        """Welcome message with disclaimer"""
        greeting = random.choice(self.greetings)
        disclaimer = "\n⚠️ DISCLAIMER: This is for educational purposes only. Cryptocurrency investments are risky. Always do your own research!"
        return f"{greeting}\n{disclaimer}\n\nHow can I help you today? Try asking about:\n• Trending cryptos\n• Sustainable coins\n• Investment advice\n• Specific crypto info"

    def analyze_query(self, user_input):
        """Analyze user input and determine intent"""
        query = user_input.lower()
        
        # Sustainability queries
        if any(word in query for word in ['sustainable', 'eco', 'green', 'environment', 'energy']):
            return 'sustainability'
        
        # Profitability queries
        elif any(word in query for word in ['profit', 'rising', 'trending', 'growth', 'gains']):
            return 'profitability'
        
        # Specific crypto queries
        elif any(crypto.lower() in query for crypto in self.crypto_db.keys()):
            return 'specific_crypto'
        
        # General advice queries
        elif any(word in query for word in ['invest', 'buy', 'recommend', 'advice', 'best']):
            return 'general_advice'
        
        # Market info queries
        elif any(word in query for word in ['price', 'market', 'cap', 'value']):
            return 'market_info'
        
        # Help queries
        elif any(word in query for word in ['help', 'what', 'how', 'commands']):
            return 'help'
        
        else:
            return 'unknown'

    def get_sustainable_crypto(self):
        """Find the most sustainable cryptocurrency"""
        best_crypto = max(self.crypto_db.items(), 
                         key=lambda x: x[1]['sustainability_score'])
        
        crypto_name, crypto_data = best_crypto
        return f"🌱 **{crypto_name} ({crypto_data['symbol']})** is your best eco-friendly choice!\n" \
               f"• Sustainability Score: {crypto_data['sustainability_score']}/10\n" \
               f"• Energy Use: {crypto_data['energy_use']}\n" \
               f"• Current Price: {crypto_data['current_price']}\n" \
               f"• Why it's great: {crypto_data['description']}\n" \
               f"Perfect for long-term, environmentally conscious investing! 🌍"

    def get_profitable_crypto(self):
        """Find cryptocurrencies with rising trends"""
        rising_cryptos = {name: data for name, data in self.crypto_db.items() 
                         if data['price_trend'] == 'rising'}
        
        if not rising_cryptos:
            return "📈 Currently, no cryptos in my database show strong rising trends. Market conditions change rapidly!"
        
        # Prioritize high market cap among rising cryptos
        best_crypto = max(rising_cryptos.items(), 
                         key=lambda x: 1 if x[1]['market_cap'] == 'high' else 0)
        
        response = "📈 **Hot Trending Cryptos:**\n\n"
        for name, data in rising_cryptos.items():
            trend_emoji = "🚀" if data['market_cap'] == 'high' else "📊"
            response += f"{trend_emoji} **{name} ({data['symbol']})**\n"
            response += f"• Price: {data['current_price']} (Rising!)\n"
            response += f"• Market Cap: {data['market_cap']}\n"
            response += f"• {data['description']}\n\n"
        
        return response + "Remember: Rising trends don't guarantee future gains! 💡"

    def get_crypto_info(self, user_input):
        """Get information about a specific cryptocurrency"""
        query = user_input.lower()
        
        for crypto_name, crypto_data in self.crypto_db.items():
            if crypto_name.lower() in query or crypto_data['symbol'].lower() in query:
                trend_emoji = "📈" if crypto_data['price_trend'] == 'rising' else "📊"
                sustain_emoji = "🌱" if crypto_data['sustainability_score'] >= 7 else "⚡"
                
                return f"{trend_emoji} **{crypto_name} ({crypto_data['symbol']})** {sustain_emoji}\n" \
                       f"• Current Price: {crypto_data['current_price']}\n" \
                       f"• Trend: {crypto_data['price_trend'].title()}\n" \
                       f"• Market Cap: {crypto_data['market_cap'].title()}\n" \
                       f"• Energy Use: {crypto_data['energy_use'].title()}\n" \
                       f"• Sustainability Score: {crypto_data['sustainability_score']}/10\n" \
                       f"• About: {crypto_data['description']}\n"
        
        return "🤔 I don't have information about that cryptocurrency in my database. Try asking about Bitcoin, Ethereum, Cardano, Solana, or Polkadot!"

    def get_general_advice(self):
        """Provide general investment advice"""
        # Find balanced recommendation
        balanced_cryptos = []
        for name, data in self.crypto_db.items():
            if data['sustainability_score'] >= 6 and data['price_trend'] == 'rising':
                balanced_cryptos.append((name, data))
        
        if balanced_cryptos:
            best_choice = random.choice(balanced_cryptos)
            crypto_name, crypto_data = best_choice
            
            return f"💡 **My Balanced Recommendation: {crypto_name} ({crypto_data['symbol']})**\n\n" \
                   f"Why it's a smart choice:\n" \
                   f"✅ Price trending: {crypto_data['price_trend']}\n" \
                   f"✅ Sustainability score: {crypto_data['sustainability_score']}/10\n" \
                   f"✅ Energy efficient: {crypto_data['energy_use']} usage\n" \
                   f"✅ Current price: {crypto_data['current_price']}\n\n" \
                   f"💭 {crypto_data['description']}\n\n" \
                   f"⚠️ Remember: Diversify your portfolio and never invest more than you can afford to lose!"
        
        return "💡 Based on my analysis, consider a mix of sustainable and trending cryptos. Cardano and Solana show good potential!"

    def get_market_info(self):
        """Provide market overview"""
        total_cryptos = len(self.crypto_db)
        rising_count = sum(1 for data in self.crypto_db.values() if data['price_trend'] == 'rising')
        sustainable_count = sum(1 for data in self.crypto_db.values() if data['sustainability_score'] >= 7)
        
        return f"📊 **Market Overview:**\n" \
               f"• Total tracked cryptos: {total_cryptos}\n" \
               f"• Currently rising: {rising_count}\n" \
               f"• Highly sustainable (7+/10): {sustainable_count}\n" \
               f"• Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n" \
               f"💡 Tip: Look for cryptos that balance profitability with sustainability!"

    def get_help(self):
        """Provide help information"""
        return """🤖 **CryptoBuddy Help Center**

**What I can help you with:**
• 🌱 Find sustainable/eco-friendly cryptos
• 📈 Discover trending/profitable cryptos  
• 💰 Get investment advice and recommendations
• 📊 Check specific crypto information
• 🔍 Market overview and analysis

**Try asking:**
• "What's the most sustainable crypto?"
• "Which cryptos are trending up?"
• "Tell me about Bitcoin"
• "What should I invest in?"
• "Show me market info"

**Remember:** I'm here to educate and inform, not provide financial advice! 🎓"""

    def process_query(self, user_input):
        """Main query processing logic"""
        if not user_input.strip():
            return "🤔 I didn't catch that. Try asking me about crypto trends, sustainability, or specific coins!"
        
        intent = self.analyze_query(user_input)
        
        if intent == 'sustainability':
            return self.get_sustainable_crypto()
        elif intent == 'profitability':
            return self.get_profitable_crypto()
        elif intent == 'specific_crypto':
            return self.get_crypto_info(user_input)
        elif intent == 'general_advice':
            return self.get_general_advice()
        elif intent == 'market_info':
            return self.get_market_info()
        elif intent == 'help':
            return self.get_help()
        else:
            return "🤔 I'm not sure what you're asking about. Try:\n" \
                   "• 'What's sustainable?'\n" \
                   "• 'Which crypto is trending?'\n" \
                   "• 'Tell me about Ethereum'\n" \
                   "• 'What should I buy?'\n" \
                   "• Type 'help' for more options!"

def main():
    """Main chatbot interaction loop"""
    buddy = CryptoBuddy()
    
    print("=" * 60)
    print("🤖 CRYPTOBUDDY - Your AI Crypto Advisor")
    print("=" * 60)
    print(buddy.greet())
    print("\n" + "─" * 60)
    
    while True:
        try:
            user_input = input("\n💬 You: ").strip()
            
            # Exit conditions
            if user_input.lower() in ['quit', 'exit', 'bye', 'goodbye']:
                print(f"\n🤖 CryptoBuddy: {random.choice(buddy.farewells)}")
                break
            
            # Process query
            response = buddy.process_query(user_input)
            print(f"\n🤖 CryptoBuddy: {response}")
            print("─" * 60)
            
        except KeyboardInterrupt:
            print(f"\n\n🤖 CryptoBuddy: {random.choice(buddy.farewells)}")
            break
        except Exception as e:
            print(f"\n🤖 CryptoBuddy: Oops! Something went wrong. Let me try again! 🔧")

if __name__ == "__main__":
    main()
