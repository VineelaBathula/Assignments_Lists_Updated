#user interface to the main menu
import data
import functions
def show_main_menu():
  while True:
    print("Vineela's diner") #edit to show your name
    print("__________")
    print('N for a new order')
    print('C to change an existing order')
    print('X for close orders and print the check')
    print('Q for quit')
    user_menu_choice = input('Your choice: ').upper()
    if user_menu_choice in 'Qq':
      break
    elif user_menu_choice in 'Xx': 
      print('This option prints the list of items ordered, extended price, total, Taxes, and Grand total ')
      close_order(user_menu_choice)
    elif user_menu_choice in 'Cc':
      print('Change Order')
    elif user_menu_choice in 'Nn': 
      print('New order')
      make_order(user_menu_choice.upper())  #calls a function for adding to the orders

def make_order(menu_choice):
  print(menu_choice)
  while True:
    user_selection = functions.get_item_number()  # Get user input for item and quantity
    item_code, quantity = user_selection.split()  # Split the user input into item code and quantity
    functions.add_to_order(item_code, quantity)  # Add the selected item to the order
    another_item = input("Do you want to add another item? (Y/N): ").upper()  # Ask if the user wants to add another item
    if another_item != 'Y':  # Break the loop if the user doesn't want to add more items
      break
  
  

def close_order(menu_choice):
  """ Closes the order , prints the receipt and reset the current order"""

  if not functions.current_order:  # Check if there are no items in the order
        print("No items in your order.")
        return
  print("\nYour order:")
  Total = 0  # Initialize total for the order

# Loop through the current order and calculate the total
  for item_name, item_price, quantity in functions.current_order:
    item_total = item_price * quantity
    Total += item_total
    print(f"{quantity} x {item_name} @ ${item_price} = ${item_total}")


  tax = Total* 0.07  # Assuming 7% tax
  grand_total = Total + tax
  print(f"\nSubtotal: ${Total:.2f}")
  print(f"Tax (7%): ${tax:.2f}")
  print(f"Grand Total: ${grand_total:.2f}\n")

# Clear the current order after printing the receipt
  functions.current_order.clear()
  print("Order complete and reset for the next customer.")







if __name__ == '__main__':
  #initialize the lists
    drinks = []
    appetizers = []
    salads = []
    entrees = []
    dessert= []
show_main_menu()
