from order_execution import place_order_with_sl_tp

# Example values for a test trade:
instrument = "EUR_USD"
units = 1  # Buy 1 unit (positive number)
stop_loss_price = 1.1000
take_profit_price = 1.1050

place_order_with_sl_tp(instrument, units, stop_loss_price, take_profit_price)
