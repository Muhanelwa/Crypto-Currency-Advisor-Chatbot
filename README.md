# Crypto-Currency-Advisor-Chatbot 

**Your First AI-Powered Financial Sidekick!** 

A rule-based chatbot that analyzes cryptocurrency data and provides investment advice based on **profitability** (price trends) and **sustainability** (energy efficiency, project viability).


##  Features

- **Smart Analysis**: Rule-based decision making for crypto recommendations
- **Sustainability Focus**: Prioritizes eco-friendly cryptocurrencies
- **Profitability Tracking**: Identifies trending and rising cryptos
- **Interactive Chat**: Natural conversation flow with friendly personality
- **Educational**: Includes disclaimers and investment safety tips
- **Comprehensive Data**: Covers major cryptocurrencies with detailed metrics

## What This Project Demonstrates

This chatbot showcases **basic AI decision-making** through:

1. **Pattern Recognition**: Analyzes user queries to determine intent
2. **Rule-Based Logic**: Uses if-else conditions to match queries with appropriate responses
3. **Data Processing**: Filters and ranks cryptocurrencies based on multiple criteria
4. **Decision Trees**: Combines profitability and sustainability factors for balanced recommendations

## Technology Stack

- **Language**: Python 3.7+
- **Libraries**: Built-in Python modules (no external dependencies required)
- **Architecture**: Object-oriented design with clear separation of concerns
- **Data Structure**: Dictionary-based cryptocurrency database

## Cryptocurrency Database

Currently tracking 5 major cryptocurrencies:

| Crypto | Symbol | Trend | Market Cap | Energy Use | Sustainability Score |
|--------|--------|--------|------------|------------|---------------------|
| Bitcoin | BTC | Rising | High | High | 3/10 |
| Ethereum | ETH | Stable | High | Medium | 6/10 |
| Cardano | ADA | Rising | Medium | Low | 8/10 |
| Solana | SOL | Rising | Medium | Low | 7/10 |
| Polkadot | DOT | Stable | Medium | Low | 8/10 |


### Sample Conversations

**Sustainability Query:**
```
You: What's the most sustainable crypto?
CryptoBuddy: 🌱 Cardano (ADA) is your best eco-friendly choice!
• Sustainability Score: 8/10
• Energy Use: low
• Current Price: $0.45
• Perfect for long-term, environmentally conscious investing! 🌍
```

**Profitability Query:**
```
You: Which cryptos are trending up?
CryptoBuddy: 📈 Hot Trending Cryptos:
🚀 Bitcoin (BTC) - Price: $45,000 (Rising!)
📊 Cardano (ADA) - Price: $0.45 (Rising!)
📊 Solana (SOL) - Price: $95 (Rising!)
```

**Investment Advice:**
```
You: What should I invest in?
CryptoBuddy: 💡 My Balanced Recommendation: Cardano (ADA)
Why it's a smart choice:
✅ Price trending: rising
✅ Sustainability score: 8/10
✅ Energy efficient: low usage
⚠️ Remember: Diversify your portfolio and never invest more than you can afford to lose!
```

## 🎮 Available Commands

- **Sustainability**: "sustainable crypto", "eco-friendly", "green coins"
- **Profitability**: "trending up", "profitable", "rising cryptos"
- **Specific Info**: "tell me about Bitcoin", "Ethereum info"
- **General Advice**: "what should I buy?", "investment advice"
- **Market Overview**: "market info", "show prices"
- **Help**: "help", "commands", "what can you do?"

## 🧠 AI Decision-Making Logic

The chatbot mimics AI decision-making through:

### 1. Intent Recognition
```python
def analyze_query(self, user_input):
    query = user_input.lower()
    if any(word in query for word in ['sustainable', 'eco', 'green']):
        return 'sustainability'
    elif any(word in query for word in ['profit', 'rising', 'trending']):
        return 'profitability'
    # ... more conditions
```

### 2. Data-Driven Recommendations
```python
def get_sustainable_crypto(self):
    best_crypto = max(self.crypto_db.items(), 
                     key=lambda x: x[1]['sustainability_score'])
    return recommendation
```

### 3. Multi-Criteria Decision Making
```python
def get_general_advice(self):
    # Find cryptos that balance sustainability AND profitability
    for name, data in self.crypto_db.items():
        if data['sustainability_score'] >= 6 and data['price_trend'] == 'rising':
            balanced_cryptos.append((name, data))
```

## 🔮 Future Enhancements

- [ ] **Real-time Data**: Integrate CoinGecko API for live prices
- [ ] **NLP Processing**: Add NLTK for better natural language understanding
- [ ] **Machine Learning**: Implement predictive models for price trends
- [ ] **Web Interface**: Create a Flask/Django web app
- [ ] **Portfolio Tracking**: Add investment tracking features
- [ ] **Risk Analysis**: Include volatility and risk metrics

## ⚠️ Important Disclaimers

- **Educational Purpose Only**: This chatbot is for learning AI concepts, not financial advice
- **Investment Risk**: Cryptocurrency investments are highly risky and volatile
- **Do Your Own Research**: Always conduct thorough research before investing
- **Not Financial Advice**: Responses are based on simplified rules, not professional analysis

## 📚 Learning Outcomes

This project teaches:

- **AI Fundamentals**: Rule-based systems and decision trees
- **Python Programming**: Object-oriented design and string processing
- **Data Analysis**: Filtering, sorting, and ranking algorithms
- **User Experience**: Conversational interface design
- **Financial Technology**: Cryptocurrency market basics

## 👥 Contributing

Want to improve CryptoBuddy? Here are some ideas:

1. Add more cryptocurrencies to the database
2. Improve the natural language processing
3. Add new analysis metrics (volatility, trading volume)
4. Create a graphical user interface
5. Implement real-time data feeds

##  Acknowledgments

- PLP Academy for the assignment framework
- Cryptocurrency community for education and awareness
- Python community for excellent documentation and tools

##  Contact

Created as part of PLP Academy's AI development course.

**Happy Investing! Remember: DYOR (Do Your Own Research)! 💎**

