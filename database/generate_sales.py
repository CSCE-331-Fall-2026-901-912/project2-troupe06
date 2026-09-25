import csv
import random
from datetime import datetime, timedelta

orders = []
date = datetime(2026, 8, 24)

for day in range(32):
    numOrders = random.randint(80, 150)

    if day < 5:
        numOrders += 100

    for i in range(numOrders):
        time = date + timedelta(days=day, hours=random.randint(10, 21), minutes=random.randint(0, 59))
        price = round(random.uniform(5, 35), 2)
        orders.append([len(orders) + 1, time, "Completed", price, random.randint(1, 5)])

with open("orders.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["orderID", "timestamp", "orderStatus", "totalPrice", "processedByEmployee"])
    writer.writerows(orders)