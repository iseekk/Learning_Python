def display_inventory(inv):
    print("\nInventory:\n"
          "{items}\n"
          "----------\n"
          "Total number of items: {num}".format(items="\n".join([str(v) + " " + k for k, v in inv.items()]),
                                                num=sum(i for i in inv.values())))


def add_to_inventory(inv, loot):
    for i in set(loot):
        inv.setdefault(i, 0)
        inv[i] += loot.count(i)
    return inv


inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
display_inventory(inventory)
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
add_to_inventory(inventory, dragonLoot)
display_inventory(inventory)
