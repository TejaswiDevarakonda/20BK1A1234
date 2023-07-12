train_name = "trainllame"
train_number = "2343"
departure_time = {
    "Hours": 9,
    "Minutes": 45,
    "Seconds": 0
}
seats_available = {
    "sleeper": 32,
    "AC": 1
}
price = {
    "sleeper": 1,
    "AC": 723
}
delayed_by = 3

output = f"Train: {train_name}\n"
output += f"Train Number: {train_number}\n"
output += f"Departure Time: {departure_time['Hours']}:{departure_time['Minutes']}:{departure_time['Seconds']}\n"
output += f"Seats Available: Sleeper - {seats_available['sleeper']}, AC - {seats_available['AC']}\n"
output += f"Price: Sleeper - {price['sleeper']}, AC - {price['AC']}\n"
output += f"Delayed by: {delayed_by} minutes"

print(output)
