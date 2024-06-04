"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                                LAB 2
-----------------------------------------------------------------------------------------------
- File Name: lab2.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Extend the functionality developed in Lab 1 by creating an InventoryManager class 
               that acts as a facade for managing an inventory of items. Demonstrate the use of 
               encapsulation and the facade design pattern through practical examples.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Step 1: Import the Item class from lab1.py
from lab1 import Item




# Step 2: Define the InventoryManager class as a facade to handle the inventory operations.
# It should include methods to add, remove, update, and display items in the inventory.
class InventoryManager:
    def __init__(self):
        self.items = [] 

    def add_item(self, item):
        self.items.append(item)
        print("Item Added")

    def remove_item(self, item):
        self.items.remove(item)
        print("Item removed")
    
    def update_item_price(self, item, new_price):
        for items in self.items:
            if items.get_name() == item:
                items.set_price(new_price)
    
    def update_item_quantity(self, item, new_quantity):
        item.set_quantity(new_quantity)

    def display_items(self):
        for item in self.items:
            print(item)
         

 




# Step 2: Create instances of the Item class and InventoryManager, then demonstrate their usage.
# E.g. add items to the inventory, remove items, update items, and display the inventory.
#manager = InventoryManager()
#item1 = Item("Box", 2, 69)
#item2 = Item("Blox", 3, 96)
#manager.add_item(item1)
#manager.add_item(item2)
#manager.display_items()
#manager.update_item_price(item2, 99)
#manager.update_item_quantity(item1, 2)
#manager.display_items()
