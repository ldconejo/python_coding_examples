import sys
from database_model import database
from shopping_list import ShoppingListCollection

def add_item():
    item_id = input("Please enter item id: ")
    item_description = input("Please enter item description: ")
    result = shopping_list_instance.add_item(item_id, item_description)
    if result:
        print(f"{item_id} successfully added.")
    else:
        print(f"ERROR: Could not add {item_id}")           

def update_item():
    item_id = input("Please enter the item id to update: ")
    item_description = input("Please enter updated item description: ")
    result = shopping_list_instance.update_item(item_id, item_description)
    if result:
        print(f"{item_id} successfully updated.")
    else:
        print(f"ERROR: Could not update {item_id}")

def delete_item():
    item_id = input("Please enter ID for the item to delete: ")
    result = shopping_list_instance.delete_item(item_id)
    if result:
        print(f"{item_id} deleted")
    else:
        print(f"ERROR: {item_id} not found")

def search_item():
    item_id = input("Please enter item id to search: ")
    result = shopping_list_instance.search_item(item_id)
    if result:
        print(f"Item ID: {result.product_code}")
        print(f"Description: {result.product_description}")
    else:
        print(f"ERROR: {item_id} not found")

def quit_program():
    sys.exit(0)

if __name__ == "__main__":
    shopping_list_instance = ShoppingListCollection(database)
    menu_options = {
        'A': add_item,
        'B': update_item,
        'C': delete_item,
        'D': search_item,
        'Q': quit_program
    }
    while True:
        user_selection = input("""
                            A: Add item
                            B: Update item
                            C: Delete item
                            D: Search item
                            Q: Quit
                               
                            Please enter your choice: """)
        if user_selection.upper() in menu_options:
            menu_options[user_selection.upper()]() # If I type "A", this will result in add_item() --> the function is called
        else:
            print("Invalid option")