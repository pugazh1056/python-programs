"""Functions to keep track and alter inventory."""


def create_inventory(items):
    freq = {}
    for i in items:
        freq[i] = freq.get(i, 0) + 1
    return freq


def add_items(inventory, items):
    for item in items:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory


def decrement_items(inventory, items):
    for item in items:
        if item in inventory and inventory[item] > 0:
            inventory[item] -= 1
    return inventory


def remove_item(inventory, item):
    if item in inventory:
        del inventory[item]
    return inventory


def list_inventory(inventory):
    result = []
    for item, count in inventory.items():
        if count > 0:
            result.append((item, count))
    return result