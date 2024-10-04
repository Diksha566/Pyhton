
room_type = input("Enter the type of room you want to choose:\n1. Standard: $100/night\n2. Deluxe: $150/night\n3. Suite: $250/night\n")


nights = int(input("How many nights do you want to stay? "))


if nights > 7:
    discount_rate = 0.20  
elif nights > 3:
    discount_rate = 0.10  
else:
    discount_rate = 0.0   


if room_type == '1':
    price_per_night = 100
elif room_type == '2':
    price_per_night = 150
elif room_type == '3':
    price_per_night = 250
else:
    print("Invalid room type selected.")
    price_per_night = 0

total_price = price_per_night * nights


discount_amount = total_price * discount_rate
final_price = total_price - discount_amount


peak_season = input("Is it peak season? (yes/no): ").strip().lower()

if peak_season == 'yes':
    final_price += 0.20 * final_price  
else:
    final_price -= 0.15 * final_price  

print(f"The total price after the discount is: ${final_price:.2f}")

