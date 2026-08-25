
 def show_menu_card(menu_items):
    print("\n" + "="*35)
    print(f"| {'Product Name':<20} | {'Price':<7} |")
    print("="*35)
    
    if not menu_items:
        print(f"| {'Menu is empty!':<31} |")
    else:
        for item, price in menu_items.items():
            print(f"| {item:<20} | {price:<7} |")
            
    print("="*35 + "\n")


def main():
    menu_card = {}
    
    while True:
        print("--- Menu Card System ---")
        print("1. Add new product and price")
        print("2. View Menu Card ")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            product_name = input("Enter product name: ")
            try:
                product_price = float(input("Enter its price: "))
                menu_card[product_name] = product_price
                print(f"'{product_name}' added to the menu successfully!\n")
            except ValueError:
                print("Please enter a valid number for the price!\n")
                
        elif choice == '2':
            show_menu_card(menu_card)
            
        elif choice == '3':
            print("Exiting program. Thank you!")
            break
            
        else:
            print("Invalid choice! Please try again.\n")


if __name__ == "__main__":
    main()
