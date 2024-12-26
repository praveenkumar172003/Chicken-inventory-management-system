legs_per_chicken = 2
wings_per_chicken = 2
flesh_per_chicken = 1
leg_weight = 200  # grams
wing_weight = 200  # grams
flesh_weight = 800  # grams
total_chickens = 12  


total_legs = total_chickens * legs_per_chicken
total_wings = total_chickens * wings_per_chicken
total_flesh = total_chickens * flesh_per_chicken
total_weight = total_chickens * 1.6 


order_legs = int(input("Enter the number of legs: "))
order_wings = int(input("Enter the number of wings: "))
order_flesh = int(input("Enter the number of flesh portions: "))


if order_legs > total_legs or order_wings > total_wings or order_flesh > total_flesh:
    print("Order cannot be fulfilled. Not enough inventory.")
else:
    order_weight = (order_legs * leg_weight + order_wings * wing_weight + order_flesh * flesh_weight) / 1000  # Converting grams into kilograms
    
    remaining_legs = total_legs - order_legs
    remaining_wings = total_wings - order_wings
    remaining_flesh = total_flesh - order_flesh
    
    chickens_used = max(order_legs // legs_per_chicken, order_wings // wings_per_chicken, order_flesh)
    
    remaining_weight = total_weight - order_weight

    print("\nOrder Summary:")
    print(f"Total order weight: {order_weight:.2f} kg")
    print(f"Chickens used: {chickens_used}")
    print(f"Remaining legs: {remaining_legs}")
    print(f"Remaining wings: {remaining_wings}")
    print(f"Remaining flesh portions: {remaining_flesh}")
    print(f"Remaining inventory weight: {remaining_weight:.2f} kg")
