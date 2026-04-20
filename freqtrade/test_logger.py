import csv
import os
from datetime import datetime, timezone

# Simulate the CSV logger function
def log_trade_to_csv(pair, open_date, close_date, profit, exit_reason, duration):
    log_file = "user_data/trade_log.csv"
    file_exists = os.path.isfile(log_file)

    with open(log_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow([
                "Pair", "Open Date", "Close Date",
                "Profit %", "Exit Reason", "Trade Duration (hrs)"
            ])
        writer.writerow([pair, open_date, close_date, profit, exit_reason, duration])
    print(f"Trade logged: {pair} | Profit: {profit} | Reason: {exit_reason}")

# Simulate 5 sample trades
log_trade_to_csv("BTC/USDT", "2024-01-05 09:00", "2024-01-05 14:30", "2.30%", "roi", "5.5")
log_trade_to_csv("ETH/USDT", "2024-01-06 10:00", "2024-01-06 18:00", "-1.80%", "daily_loss_limit_reached", "8.0")
log_trade_to_csv("SOL/USDT", "2024-01-07 08:00", "2024-01-08 09:00", "4.10%", "trailing_stop", "25.0")
log_trade_to_csv("BTC/USDT", "2024-01-09 11:00", "2024-01-10 11:00", "-0.90%", "stuck_trade_exit", "48.0")
log_trade_to_csv("ETH/USDT", "2024-01-10 13:00", "2024-01-10 20:00", "1.50%", "roi", "7.0")

print("CSV log created at user_data/trade_log.csv")