# Comment out the run_bot loop:
# if __name__ == "__main__":
#     run_bot()

# Instead, test a single trade:
from strategy import place_trade
place_trade("XAU_USD", "BUY")
