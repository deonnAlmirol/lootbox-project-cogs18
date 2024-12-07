from modules.classes import *
from rich.console import Console
from rich.table import Table
import random

# common: 90% chance common 6% uncommon 3% rare 1% legendary
# uncommon: 30% common 62% uncommon 5% rare 3% legendary
# rare: 5% common 10% uncommon 75% rare 10% legendary
# legendary: 1% common 2% uncommon 30% rare 67% legendary

# lootbox class: takes in chance pool (int) and bias as input
# class contains shop methods

def common():
    chance = random.randint(0, 100000)

    if chance <= 90000:
        item = Item(name = 'common item', rarity = 1, value = random.randint(0, 10))

    if chance > 90000 and chance <= 96000:
        item = Item(name = 'uncommon item', rarity = 2, value = random.randint(10, 20))

    if chance > 96000 and chance <= 99000:
        item = Item(name = 'rare item', rarity = 3, value = random.randint(20, 50))

    if chance > 99000:
        item = Item(name = 'legendary item', rarity = 4, value = random.randint(75, 1000))
    
    return item

def uncommon():
    return Item(name = 'uncommon item', rarity = 2, value = 20)

def rare():
    return Item(name = 'reare item', rarity = 3, value = 10)

def legendary():
    return Item(name = 'legends item', rarity = 4, value = 100)

def show_shop():
    shop_table = Table(title = 'Lootbox Shop', row_styles=['','cyan','yellow','red'])

    shop_table.add_column("Item")
    shop_table.add_column('Price', style='green')

    shop_table.add_row("Common Box", '10')
    shop_table.add_row("Uncommon Box", '20')
    shop_table.add_row("Rare Box", '50')
    shop_table.add_row("Legendary Box", '100')

    console = Console()
    console.print(shop_table)

def get_box(rarity: str):
    rarity_prices = {
        'common': 5,
        'uncommon': 10,
        'rare': 50,
        'legendary': 500
    }

    if rarity in rarity_prices.keys():
        return Box(rarity, rarity_prices[rarity])