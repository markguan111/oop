

class Retailltem:

    def __init__(self, des, inv, price):
        self.__item_description = des
        self.__units_inventory = inv
        self.__price = price

    def set_item_description(self, des):
        self.__item_description = des

    def set_units_inventory(self, inv):
        self.__units_inventory = inv

    def set_price(self, price):
        self.__price = price

    def get_item_decription(self):
        return self.__item_description

    def get_units_inventory(self):
        return self.__units_inventory

    def get_price(self):
        return self.__price


    


    
