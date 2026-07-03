# Shopping Cart
items = []
while True:
    item = input("Enter item (or type 'done'): ").strip()
    if item.lower() == "done":
        break
    if item == "":
        print("Please enter a valid item.")
        continue
    items.append(item)
print("🛒 Your Shopping Cart")
for position, item in enumerate(items, start=1):
    print(f"{position}. {item}")
print(f"Total items: {len(items)}")
item_to_remove = input("Enter the item you want to remove: ")
if item_to_remove in items:
    items.remove(item_to_remove)
else:
    print("Item not found in your cart.")
print("🛒 Your Shopping Cart")
for position, item in enumerate(items, start=1):
    print(f"{position}. {item}")
print(f"Total items: {len(items)}")