def display_menu():
    menu = {
        "Burger": 59.00,
        "Pizza": 700.00,
        "1 Bucket Fried Chicken": 456.99,
        "1 Piece Chicken": 129.00,
        "Soda": 35.00
    }
    
    print("\nWelcome to Markdonalds!!")
    print("Here's our Menu:\n")
    
    for item, price in menu.items():
        print(f"{item}: ₱{price:.2f}")
    
    return menu

def take_order(menu):
    order_items = []
    total_cost = 0
    
    print("\nEnter the items you want to order. Type 'dine in' or 'take out' to finish.")
    
    while True:
        order = input("Please enter a food item: ").title()
        
        if order.lower() == 'dine in' or order.lower() == 'take out':
            break
        
        if order in menu:
            order_items.append(order)
            total_cost += menu[order]
            print(f"You've selected {order} which costs ₱{menu[order]:.2f}")
        else:
            print("Sorry, that's not on the menu. Please select a valid item.")
    
    return order_items, total_cost

def display_order_summary(order_items, menu, total_cost):
    print("\nOrder Summary:")
    for item in order_items:
        print(f"{item}: ₱{menu[item]:.2f}")
    print(f"\nTotal Cost: ₱{total_cost:.2f}")

def process_payment(total_cost):
    cash = input(f"\nThe total cost is ₱{total_cost:.2f}. Please enter your payment: ₱")
    
    if cash.replace('.', '', 1).isdigit() and cash.count('.') <= 1:

        cash = float(cash)
        
        if cash < total_cost:
            while cash < total_cost:
                print(f"Insufficient payment! You need ₱{total_cost - cash:.2f} more.")
                cash = input(f"\nThe total cost is ₱{total_cost:.2f}. Please enter your payment: ₱")
                
                if cash.replace('.', '', 1).isdigit() and cash.count('.') <= 1:
                    cash = float(cash)
                else:
                    print("Invalid input! Please enter a valid number.")
                    cash = input(f"\nThe total cost is ₱{total_cost:.2f}. Please enter your payment: ₱")
        else:
            change = cash - total_cost
            print(f"Thank you for your purchase! Your change is: ₱{change:.2f}")
    
    else:
        print("Invalid input! Please enter a valid number.")
        cash = input(f"\nThe total cost is ₱{total_cost:.2f}. Please enter your payment: ₱")

        process_payment(total_cost)

def main():
    menu = display_menu()
    
    
    order_items, total_cost = take_order(menu)
    
    
    if len(order_items) == 0:
        print("\nNo items were ordered. Exiting the system.")
        return
    
    
    display_order_summary(order_items, menu, total_cost)
    
   
    process_payment(total_cost)

if __name__ == "__main__":
    main()
