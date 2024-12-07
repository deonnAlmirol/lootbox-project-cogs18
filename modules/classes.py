import json
import random

class Player:

    def __init__(self, item_inventory = [], box_inventory = [], currency = 25, savefile = 'savedata.dat'):
        self.item_inventory = item_inventory
        self.box_inventory = box_inventory
        self.currency = currency
        self.savefile = savefile

    def save(self, filename = None):
        if filename is None:
            filename = self.savefile
        
        file = open(filename, 'w')

        save_dict = {
            'item_inventory': [],
            'box_inventory': [],
            'currency': self.currency
        }

        #for item in self.item_inventory:
         #   save_dict['inventory'].append(json.dumps(item.__dict__))

        save_dict['item_inventory'] = [json.dumps(item.__dict__) for item in self.item_inventory]

        save_dict['box_inventory'] = self.box_inventory

        
        
        data_json = json.dumps(save_dict)
        file.write(data_json)
        print(f" saved to {filename}")

    def load(self, filename = None):
        if filename is None:
            filename = self.savefile
        
        try:
            save = open(filename, 'r')
            print(f"Save data found! Loading {filename}")
            save_dict = json.loads(save.read())
            save.close()
            self.inventory = save_dict['inventory']
            self.currency = save_dict['currency']

            for i in range(0, len(self.inventory)):
                item_data = json.loads(self.inventory[i])
                self.inventory[i] = Item(name = item_data['name'], rarity = item_data['rarity'], value = item_data['value'])
        except Exception as e:
            print('Save data corrupted or not found')

        self.savefile = filename
        
    def add_item(self, item):
        self.item_inventory.append(item)

    def sell_item(self, item_idx):
        self.currency += self.item_inventory[item_idx].value
        self.item_inventory.pop(item_idx)

    def add_box(self, box):
        self.box_inventory.append(box)

    def purchase_box(self, box):
        if self.currency >= box.price:
            self.add_box(box)
            self.currency -= box.price
            #print(f"successfully purchased {box.box_type} box")
        else:
            print("not enough money")

    def open_box(self, box):
        self.add_item(box.open())
        self.box_inventory.pop(0)

    def add_currency(self, amount):
        self.currency += amount

    def print_item_inventory(self):
        if len(self.item_inventory) > 0:
            for item in self.item_inventory:
                print(item.name)
        else:
            print('no itme')

    def print_box_inventory(self):
        if len(self.box_inventory) > 0:
            for box in self.box_inventory:
                print(box.box_type)
        else:
            print('no boxes')
        


class Item:

    def __init__(self, name, rarity, value):
        self.name = name
        self.rarity = rarity
        self.value = value

class Box:

    def __init__(self, box_type, price, opened = False):
        self.box_type = box_type
        self.price = price
        self.opened = opened

    def open(self):

        if self.opened:
            print('box already opened')
            return

        if self.box_type == 'common':
            chance = random.randint(0, 100000)

            if chance <= 90000:
                item = Item(name = 'common item', rarity = 1, value = random.randint(0, 10))

            if chance > 90000 and chance <= 96000:
                item = Item(name = 'uncommon item', rarity = 2, value = random.randint(10, 20))

            if chance > 96000 and chance <= 99000:
                item = Item(name = 'rare item', rarity = 3, value = random.randint(20, 50))

            if chance > 99000:
                item = Item(name = 'legendary item', rarity = 4, value = random.randint(75, 1000))

        if self.box_type == 'uncommon':
            chance = random.randint(0, 100000)

            if chance <= 30000:
                item = Item(name = 'common item', rarity = 1, value = random.randint(0, 10))

            if chance > 30000 and chance <= 92000:
                item = Item(name = 'uncommon item', rarity = 2, value = random.randint(10, 20))

            if chance > 92000 and chance <= 97000:
                item = Item(name = 'rare item', rarity = 3, value = random.randint(20, 50))

            if chance > 97000:
                item = Item(name = 'legendary item', rarity = 4, value = random.randint(75, 1000))

        if self.box_type == 'rare':
            chance = random.randint(0, 100000)

            if chance <= 5000:
                item = Item(name = 'common item', rarity = 1, value = random.randint(0, 10))

            if chance > 5000 and chance <= 15000:
                item = Item(name = 'uncommon item', rarity = 2, value = random.randint(10, 20))

            if chance > 15000 and chance <= 90000:
                item = Item(name = 'rare item', rarity = 3, value = random.randint(20, 50))

            if chance > 90000:
                item = Item(name = 'legendary item', rarity = 4, value = random.randint(75, 75000))

        if self.box_type == 'legendary':
            chance = random.randint(0, 100000)

            if chance <= 1000:
                item = Item(name = 'common item', rarity = 1, value = random.randint(0, 10))

            if chance > 1000 and chance <= 3000:
                item = Item(name = 'uncommon item', rarity = 2, value = random.randint(10, 20))

            if chance > 3000 and chance <= 33000:
                item = Item(name = 'rare item', rarity = 3, value = random.randint(20, 50))

            if chance > 33000:
                item = Item(name = 'legendary item', rarity = 4, value = random.randint(75, 1000))
    
        self.opened = True
        return item