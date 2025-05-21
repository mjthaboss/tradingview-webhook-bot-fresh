# Risk-Reward ratio (1:1)
RISK_REWARD_RATIO = 1.0

# Allowed instruments for trading
ALLOWED_INSTRUMENTS = [
    "XAU_USD",
    "NAS100_USD",
    "GBP_USD",
    "USD_CAD",
    "EUR_USD",
    "USD_CHF",
    "NZD_USD",
    "BTC_USD"
]

# Session hours in UTC (24h format)
SESSIONS = {
    "ASIAN": (0, 6),    # 12 AM to 6 AM UTC (adjust as needed)
    "LONDON": (6, 13),  # 6 AM to 1 PM UTC
    "NY": (13, 21),     # 1 PM to 9 PM UTC
}

# OANDA API credentials and URL
OANDA_API_KEY = "f69b4cf57b5a0e8a6a13ce624b3ca1c7-9006a9208d8fe117a94875e524eac3c3"
OANDA_ACCOUNT_ID = "101-001-26489913-001"
OANDA_URL = "https://api-fxpractice.oanda.com/v3"
