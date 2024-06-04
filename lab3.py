"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                                LAB 3
-----------------------------------------------------------------------------------------------
- File Name: lab3.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Develop a user interface for the Inventory Management System. This interface will
               allow users to interact with the InventoryManager to add, update, remove, and view
               items in the inventory using a command-line interface.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Step 1: Import necessary classes (Item class from lab1, InventoryManager class from lab2)
from lab1 import Item
from lab2 import InventoryManager
from utility import get_int

# Step 2: Define an add_item function that prompts the user for item details and adds the item to the inventory
def add_item_ui(manager):
    name = input("Enter the Item Name:")
    price = get_int("Enter the Item Price:")
    quantity = get_int("Enter the Item Quantity:")
    manager.add_item(Item(name, price, quantity))


# Step 3: Define an update_item function that prompts the user for item details and updates the item in the inventory
def update_item_ui(manager):
    name = input("Enter the Item you Wish to Update:")
    choice = get_int("Enter - 1 to Update Price - 2 to Update Quantity:")
    if choice == 1:
        new_price = get_int(f"Enter the New price for {name}:") 
        if manager.update_item_price(name, new_price):
           print(f"Price of {name} Updated Successfully")
        else:
           print(f"Unable to Update Price of {name}")
    elif choice == 2:
        new_quantity = get_int(f"Enter the New Quantity for {name}:") 
        if manager.update_item_quantity(name, new_quantity):
           print(f"Price of {name} Updated Successfully")
        else:
           print(f"Unable to Update Quantity of {name}")
        

# Step 4: Define a remove_item function that prompts the user for an item name and removes the item from the inventory
def remove_item_ui(manager):
    name = input("Enter the Item you Wish to Delete:")
    if manager.remove_item(name):
        print(f"{name} Removed Successfully")
    else:
        print(f"Unable to Remove {name}")

# Step 5: Define a display_inventory function that displays all items in the inventory
def display_inventory_ui(manager):
    manager.display_items()

def main():
    # Step 6: Initialise an instance of InventoryManager
    manager = InventoryManager()

    # Step 7: Use the actions dictionary to map user input to the corresponding functions
    actions = {'1': add_item_ui, '2': update_item_ui, '3': remove_item_ui, '4': display_inventory_ui}
    
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. Update Item")
        print("3. Remove Item")
        print("4. Display Inventory")
        print("5. Exit")

        choice = input("Enter choice: ")

        # Step 8: Implement the logic to call the appropriate function based on user input
        # Exit the loop if the user chooses 5, otherwise display an error message for invalid choices
        if choice == 5:
            pass
        elif choice in actions:
            actions[choice](manager)
        else: 
            print("Invalid Choice")

        

if __name__ == "__main__":
    main()