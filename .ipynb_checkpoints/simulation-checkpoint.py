import sys
import modules.lootbox_functions as lootbox
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from modules.classes import *
from rich.console import Console
from rich.table import Table
from rich.progress import track
from scipy.ndimage.filters import gaussian_filter1d

def simulate(player, times):

    sim_data = np.empty(shape=[0,5], dtype='int64')

    for i in track(range(times), description='Simulating...'):

        #print(f"simulating iteration {i}")

        boxes_bought = 0
        boxes_opened = 0
        items_sold = 0

        while player.currency >= 5:
            if player.currency < 40:
                player.purchase_box(lootbox.get_box('common'))
            elif player.currency >= 40 and player.currency < 100:
                player.purchase_box(lootbox.get_box('uncommon'))
            elif player.currency >= 100 and player.currency < 10000:
                player.purchase_box(lootbox.get_box('rare'))
            elif player.currency >= 5000:
                player.purchase_box(lootbox.get_box('legendary'))
            boxes_bought += 1

        while len(player.box_inventory) > 0:
            #print(player.box_inventory[0].box_type)
            player.open_box(player.box_inventory[0])
            boxes_opened += 1
        
        while len(player.item_inventory) > 0:
            player.sell_item(0)
            #print(f"new currency: {player.currency}")
            items_sold += 1

        sim_data = np.append(sim_data, [[i, player.currency, boxes_bought, boxes_opened, items_sold]], axis=0)
        #print(sim_data)
        #display_save_data_table(player, sim_data)
        #player.save()

    player.save()
    #print(sim_data)
    display_save_data_table(player, sim_data)

def display_save_data_table(player, data):
    item_table = Table(title = 'Simulation Data')

    item_table.add_column('Iteration')
    item_table.add_column('Final Currency')
    item_table.add_column('Boxes Bought')
    item_table.add_column('Boxes Opened')
    item_table.add_column('Items Sold')

    for num_list in data:
        item_table.add_row(str(num_list[0]), str(num_list[1]), str(num_list[2]), str(num_list[3]), str(num_list[4]))

    #item_table.add_row(str(player.currency), str(boxes_bought), str(boxes_opened), str(items_sold))
    
    console = Console()
    console.print(item_table)

   #print(data.T[0])
    #print(data.T[1])

    #xnew = np.linspace(data.T[0].min(), data.T[0].max(), 300000)
    #spl = make_interp_spline(data.T[0], data.T[1], k=11)
    #data_smooth = spl(xnew)

    iterations = data.T[0].max()+1

    print(iterations/50)

    data_smooth = gaussian_filter1d(data.T[1], sigma=iterations/50)

    plt.scatter(data.T[0], data.T[1], s=2/(iterations/100))
    plt.plot(data.T[0], data_smooth)
    plt.show()

if __name__ == '__main__':

    player = Player()

    simulate(player, int(sys.argv[1]))