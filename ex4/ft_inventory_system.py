print("=== Player Inventory System ===\n")

alice_inventory = {
    "sword": {
        "category": "weapon",
        "rarity": "rare",
        "quantity": 1,
        "value": 500
    },
    "potion": {
        "category": "consumable",
        "rarity": "common",
        "quantity": 5,
        "value": 50
    },
    "shield": {
        "category": "armor",
        "rarity": "uncommon",
        "quantity": 1,
        "value": 200
    }
}
bob_inventory = {}
player = {
    "Alice": alice_inventory,
    "Bob": bob_inventory
}

print("=== Alice's Inventory ===")
total = 0
item_count = 0
categories = {}
for item, info in alice_inventory.items():
    cat = info["category"]
    qty = info["quantity"]
    print(f'{item} ({info["category"]}, {info["rarity"]}): '
          f'{info["quantity"]}x @ {info["value"]} gold each = '
          f'{info["quantity"] * info["value"]} gold')
    categories[cat] = categories.get(cat, 0) + qty
    total += info["quantity"] * info["value"]
    item_count += info["quantity"]

print(f"Inventory value: {total} gold")

print(f"Item count: {item_count} items")

print(f'Categories: weapon({categories.get("weapon", 0)}),'
      f' consumable({categories.get("consumable", 0)}),'
      f' armor({categories.get("armor", 0)})')

print("=== Transaction: Alice gives Bob 2 potions ===")
item = "potion"
amount = 2

alice_item = alice_inventory.get(item)
if alice_item and alice_item["quantity"] >= amount:
    alice_item["quantity"] -= amount
    bob_item = bob_inventory.get(item)
    if bob_item:
        bob_item["quantity"] += amount
        print("Transaction successful!")
    else:
        bob_inventory[item] = {}
        bob_inventory[item].update({
            "category": alice_item["category"],
            "rarity": alice_item["rarity"],
            "quantity": amount,
            "value": alice_item["value"]
        })
        print("Transaction successful!")


def inventory_value(inv):
    total = 0
    for info in inv.values():
        total += info["quantity"] * info["value"]
    return (total)


best_value = 0
richest = ""
for name, inv in player.items():
    value = inventory_value(inv)
    if value > best_value:
        best_value = value
        richest = name


def item_count(inv):
    count = 0
    for info in inv.values():
        count += info["quantity"]
    return (count)


most_items = 0
colloctor = ""
for name, inv in player.items():
    count = item_count(inv)
    if count > most_items:
        most_items = count
        colloctor = name


rare_items = []
for inv in player.values():
    for item, info in inv.items():
        if info["rarity"] == "rare" and item not in rare_items:
            rare_items.append(item)


print("=== Updated Inventories ===")
print(f"Alice potions: {alice_inventory['potion']['quantity']}")
print(f"Bob potions: {bob_inventory['potion']['quantity']}")
print("=== Inventory Analytcs ===")
print(f"Most valueable player: {richest} ({best_value} gold)")
print(f"Most items: {colloctor} ({most_items} items)")
print("Rarest items: ", ",".join(rare_items))
