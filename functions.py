#this module will be where most functionality will be stored
#create your def blocks for the assignment in this module
#Use this  function that will return the item name and price for a given item code
# for example, find_menu_item('D2') should return Lemonade, and integer 3 as the result
import data

current_order = []
def get_item_information(item_code):
  """ this  function that will return the item name and price for a given item code.
    For example, find_menu_item('D2') should return Lemonade, and integer 3 as the result """
  print(item_code)
  for item in data.menu_items:
    item_number, item_name, item_price = item.split(' ')
    if item_number == item_code:
      return item_name.encode("ascii", "ignore").decode(), int(item_price)

def display_items():
  pass

def get_item_number():
  while True:
    print('Drinks', [d.replace('\u200b','') for d in data.menu_items if d[0] == 'D'])
    print('Appetizers', [a.replace('\u200b','') for a in data.menu_items if a[0] == 'A'])
    print('Salads', [s.replace('\u200b','') for s in data.menu_items if s[0] == 'S'])
    print('Entrees', [e.replace('\u200b','') for e in data.menu_items if e[0] == 'E'])
    print('Desserts', [t.replace('\u200b','') for t in data.menu_items if t[0] == 'T'])
    #write code for displaying the other dishes also
    order_item = input('Enter dish number and quantity: ')
    if order_item.split()[0] in data.all_items:
      return order_item
    else:
      print('Invalid dish number.  Please try again')

def add_to_order(item_code, quantity):
    """Add an item and its quantity to the current order."""
    item_name, item_price = get_item_information(item_code)
    current_order.append((item_name, item_price, int(quantity)))
    print(f'Added {quantity} x {item_name} to your order.')

def change_order(User_choice):
    """Allow user to change an order by selecting an item to update or remove."""
    if not current_order:
        print("No items in the order to change",User_choice)
        return
    
    print("Current order:")
    for i, (item_name, _, quantity) in enumerate(current_order, 1):
        print(f"{i}. {item_name} (Quantity: {quantity})")

    item_index = int(input("Enter the item number you want to change or remove: ")) - 1
    if 0 <= item_index < len(current_order):
        action = input("Enter 'C' to change quantity or 'R' to remove the item: ").upper()
        if action == 'C':
            new_quantity = int(input("Enter new quantity: "))
            current_order[item_index] = (*current_order[item_index][:2], new_quantity)
            print(f"Updated {current_order[item_index][0]} quantity to {new_quantity}.")
        elif action == 'R':
            removed_item = current_order.pop(item_index)
            print(f"Removed {removed_item[0]} from your order.")
    else:
       print("Invalid Selection")

