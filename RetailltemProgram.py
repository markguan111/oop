import RetailltemClass as RC

from tabulate import tabulate
def main():
    
    for i in range(1,4) :
        if i == 1 :
             item_description = "Jacket"
             units_inventory = 12
             price = 59.95
             item_1 = RC.Retailltem(item_description,units_inventory,price)

        if i == 2:
             item_description = "Designer Jeans"
             units_inventory = 40
             price = 34.95
             item_2 = RC.Retailltem(item_description,units_inventory,price)

        if i == 3:
             item_description = "Shirt"
             units_inventory = 20
             price = 24.95
             item_3 = RC.Retailltem(item_description,units_inventory,price)


    table = [['item_number','Description','Units in inventory','Price'],
             ['item #1',item_1.get_item_decription(),item_1.get_units_inventory(),item_1.get_units_inventory()],
             ['item #2',item_2.get_item_decription(),item_2.get_units_inventory(),item_2.get_units_inventory()],
             ['item #3',item_3.get_item_decription(),item_3.get_units_inventory(),item_3.get_units_inventory()]]


    print(tabulate(table))
    #print("Description" , "Units in inventory" , "Price")
    #print("item #1:",item_1.get_item_decription(),item_1.get_units_inventory(),item_1.get_units_inventory())
   # print("item #2:",item_2.get_item_decription(),item_2.get_units_inventory(),item_2.get_price())
    #print("item #3:", item_3.get_item_decription(),item_3.get_units_inventory(),item_3.get_price())
    
main()
