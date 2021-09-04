import csv
inventory = {'gold coin': 45, 'arrow': 12,
             'torch': 6, 'dagger': 2, 'rope': 1, 'ruby': 1}
added_items = input("Please add your items: ")
removed_items = input('Please type the items you want to remove: ')


def display_inventory(inventory):
    for key, value in inventory.items():
        print(key, ', ', value)


display_inventory(inventory)


def add_to_inventory(inventory, added_items):
    for new_item in added_items.split():
        x = new_item
        if x in inventory:
            inventory[x] = inventory[x]+1
        else:
            inventory[x] = 1

    print(inventory)


add_to_inventory(inventory, added_items)


def remove_from_inventory(inventory, removed_items):
    removed_items_split = removed_items.split()
    for item in removed_items_split:
        y = item
        if y in inventory:
            inventory[y] = inventory[y] - 1
            if inventory[y] == 0:
                inventory.pop(y)
            else:
                pass
    print(inventory)


remove_from_inventory(inventory, removed_items)


def print_table(inventory, order=None):

    print("-----------------\n")
    print("item name | count\n")
    print("-----------------\n")

    if order == "count, asc":
        inventory = sorted(inventory.items(), key=lambda count: count[1])
        inventory = dict(inventory)
    if order == "count, desc":
        inventory = sorted(inventory.items(),
                           key=lambda count: count[1], reverse=True)
        inventory = dict(inventory)
    for i, c in inventory.items():
        print(f"{i:>9} |  {c:>4}\n")

    print("-----------------\n")


print_table(inventory, order=None)


def import_inventory(inventory, filename="test_inventory.csv"):
    items_from_file = []

    with open("test_inventory.csv") as filename:
        csv_file = csv.reader(filename)
        for item_f in csv_file:
            items_from_file.extend(item_f)

    for item_f in items_from_file:
        if item_f not in inventory:
            inventory.update({item_f: 0})

    for item in inventory:
        for item_f in items_from_file:
            if item == item_f:
                inventory[item] += 1


import_inventory(inventory)


print_table(inventory, "count, desc")


def export_inventory(inventory, filename="export_inventory.csv"):
    with open(filename, "w", newline='') as file:
        writer = csv.writer(file, delimiter=",",
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
        data = []
        for k, v in inventory.items():
            data.extend([k] * v)
        writer.writerow(data)


export_inventory(inventory)
