
hotel_name = "Grand Palace Hotel"

def calculate_bill(room_charge, food_charge, service_charge):
    return room_charge + food_charge + service_charge

def apply_discount(total_amount):
    if total_amount > 5000:
        return total_amount * 0.85   
    return total_amount

def display_bill(guest_name, final_amount):
    print("Hotel Name :", hotel_name)
    print("Guest Name :", guest_name)
    print("Final Bill :", final_amount
guest_name = input()
room_charge = float(input())
food_charge = float(input())
service_charge = float(input())

total = calculate_bill(room_charge, food_charge, service_charge)
final_amount = apply_discount(total)

display_bill(guest_name, final_amount)