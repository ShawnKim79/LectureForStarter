class Menu:
    name = ''
    price = 0
    
class Order_info:
    order_menu = None
    qty = 0
    def set_order(self, menu, qty):
        self.order_menu = menu
        self.qty = qty
    def get_order_menu(self):
        return self.order_menu
    def get_order_qty(self):
        return self.qty
    
    
class Order_manager:
    order_list = []
    def set_order(self, menu):
        self.order_list.append(menu)
        
    def print_all_order(self):
        for order in self.order_list:
            qty = str(order.get_order_qty())
            print('주문은 : ' + order.get_order_menu().name + qty + '개')

def load_menu_list():
    menu_list = []
    f_menu = open("../kitchin_menu.txt", 'r')
    while True:
        menu = Menu()
        line = f_menu.readline()
        if not line: break
        menu.name = line
        menu.price = int(input(line + '은 얼마입니까?'))
        menu_list.append(menu)

    f_menu.close()
    return menu_list

def menu_output(menu_list):
    for menu in menu_list:
        print(menu.name)
        print(menu.price)

def main():
    # menus = load_menu_list()
    # menu_output(menus)
    
    my_order_manager = Order_manager()
    order_menu = Menu()
    order_menu.name = '돈까스'
    
    new_order = Order_info()
    new_order.set_order(order_menu, 3)
    
    my_order_manager.set_order(new_order)
    my_order_manager.print_all_order()
    
    

if __name__ == '__main__':
    main()