# Chicken Inventory Management System
## Overview
This script calculates and manages an inventory of chicken portions (legs, wings, and flesh). The program is designed to fulfill orders based on the available inventory of chickens, ensuring that no more than the available portions are sold. It calculates the total weight of the order, the number of chickens used, and the remaining inventory after an order is placed.

## Features
1) Inventory Management: The script maintains a stock of chicken portions (legs, wings, and flesh) and ensures the inventory is not oversold.
2) Order Fulfillment: Users can place an order by specifying the number of legs, wings, and flesh portions. If the order exceeds the available stock, it will notify the user that the order cannot be fulfilled.
3) Weight Calculation: The total weight of the order (in kilograms) is calculated based on the portions ordered.
4) Inventory Tracking: The script tracks the remaining inventory of legs, wings, and flesh after each order is placed.
## How It Works
* Initial Setup:
  * The script starts by initializing the number of legs, wings, and flesh portions per chicken.
  * The total weight per chicken is assumed to be 1.6 kg (legs, wings, and flesh combined).
  * The number of chickens in stock is set to 12, but this can be changed based on the needs of the user.
* User Input:
  * The user is prompted to enter the number of legs, wings, and flesh portions for the order.
* Order Validation:
  * The script checks if the requested order exceeds the available inventory.
  * If the order is valid, the script calculates the total weight of the order and updates the inventory accordingly.
* Order Summary:
  * After a valid order is placed, the script displays:
    * Total weight of the order.
    * Number of chickens used.
    * Remaining number of legs, wings, and flesh portions.
    * Remaining total inventory weight in kilograms.
## Code Structure
```
legs_per_chicken = 2
wings_per_chicken = 2
flesh_per_chicken = 1
leg_weight = 200  # grams
wing_weight = 200  # grams
flesh_weight = 800  # grams
total_chickens = 12  

# Total inventory calculation
total_legs = total_chickens * legs_per_chicken
total_wings = total_chickens * wings_per_chicken
total_flesh = total_chickens * flesh_per_chicken
total_weight = total_chickens * 1.6  # kg

# Order input
order_legs = int(input("Enter the number of legs: "))
order_wings = int(input("Enter the number of wings: "))
order_flesh = int(input("Enter the number of flesh portions: "))

# Order validation and fulfillment
if order_legs > total_legs or order_wings > total_wings or order_flesh > total_flesh:
    print("Order cannot be fulfilled. Not enough inventory.")
else:
    order_weight = (order_legs * leg_weight + order_wings * wing_weight + order_flesh * flesh_weight) / 1000  # kg
    remaining_legs = total_legs - order_legs
    remaining_wings = total_wings - order_wings
    remaining_flesh = total_flesh - order_flesh
    chickens_used = max(order_legs // legs_per_chicken, order_wings // wings_per_chicken, order_flesh)
    remaining_weight = total_weight - order_weight

    # Order summary
    print("\nOrder Summary:")
    print(f"Total order weight: {order_weight:.2f} kg")
    print(f"Chickens used: {chickens_used}")
    print(f"Remaining legs: {remaining_legs}")
    print(f"Remaining wings: {remaining_wings}")
    print(f"Remaining flesh portions: {remaining_flesh}")
    print(f"Remaining inventory weight: {remaining_weight:.2f} kg")
```
## Requirements
Python 3.13
## Usage
Clone the repository to your local machine.
Run the script using Python:
```
python chicken_inventory.py
```
* Input the number of legs, wings, and flesh portions for the order when prompted.
* The script will output the order summary and update the remaining inventory.

## Contributing
If you'd like to contribute to this project, please submit a pull request or open an issue to discuss proposed changes.

