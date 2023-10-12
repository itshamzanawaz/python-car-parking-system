import math
# Constants for pricing
weekday_pricing = {
    "sunday": {"morning_price": 2.00, "evening_price": 2.00},
    "monday": {"morning_price": 10.00, "evening_price": 2.00},
    "tuesday": {"morning_price": 10.00, "evening_price": 2.00},
    "wednesday": {"morning_price": 10.00, "evening_price": 2.00},
    "thursday": {"morning_price": 10.00, "evening_price": 2.00},
    "friday": {"morning_price": 10.00, "evening_price": 2.00},
    "saturday": {"morning_price": 4.00, "evening_price": 2.00},
}

# Daily total payments
daily_total = 0.00
discount1 = 0.1
discount2 = 0.5
def calculate_price(day, arrival_hour, hours, frequent_parking_number):
    # Check if the frequent parking number is valid
    if frequent_parking_number:
        if not is_valid_frequent_parking_number(frequent_parking_number):
            return "Invalid frequent parking number. No discount applied."

    # Calculate the price based on the day and arrival time
    morning_price = weekday_pricing[day]["morning_price"]
    evening_price = weekday_pricing[day]["evening_price"]
    combined_hours = arrival_hour + hours
    if arrival_hour < 16:
        if combined_hours > 16:
            if frequent_parking_number:
                total_price = ((evening_price * (combined_hours - 16)) * (1-discount2)) + ((morning_price * (16 - arrival_hour)) * (1 - discount1))
            else:
                total_price = ((evening_price * (combined_hours - 16))) + ((morning_price * (16 - arrival_hour)))
              
        else:
            total_price = morning_price * hours
        
        
    else:
        total_price = evening_price * hours
        if frequent_parking_number:
            total_price *= (1 - discount2)
    
    return total_price

def is_valid_frequent_parking_number(number):
    if number == "":
      return False 
    if len(number) != 5:
      return False
    
    digits = [int(digit) for digit in number[:4]]
    check_digit = int(number[4])
    
    weighted_sum = sum(digit * (5 - index) for index, digit in enumerate(digits))
    calculated_check_digit = weighted_sum % 11
    
    return check_digit == calculated_check_digit

def main():
    global daily_total
    day = input("Enter the day of the week: ")
    if day not in weekday_pricing:
        print("Invalid day of the week.")
        return
    arrival_hour = int(input("Enter the hour of arrival (0-23): "))
    hours = int(input("Enter the number of hours to park: "))
    check_frequent_parking_number = input("if you have a frequent parking number, enter y for yes or n for no: ")
    if check_frequent_parking_number == "y":
        frequent_parking_number = input("Enter frequent parking number: ")
    else:
        frequent_parking_number = ""
    price = calculate_price(day, arrival_hour, hours, frequent_parking_number)

    if price == "Invalid frequent parking number. No discount applied.":
        print(price)
    else:
        print(f"Amount to pay: ${price:.2f}")
        payment = float(input("Enter payment amount: "))
        daily_total += payment

    end_of_day_report()

def end_of_day_report():
    global daily_total
    print(f"Daily Total: ${daily_total:.2f}")
    daily_total = 0.00


while True:
  main()
