def load_menu():
    menu = []
    f_menu = open("../kitchin_menu.txt", 'r')
    while True:
        line = f_menu.readline()
        if not line: break
        menu.append(line)

    f_menu.close()
    return menu


def total_price(price):
    total = 0
    for p in price:
        p = int(p)
        total += p
    return total

def define_price(menu):
    price = []

    for m in menu:
        price.append(int(input(m + " 의 가격은?")))
    
    total_price_menu = total_price(price)
    print("모든 메뉴의 총합은: " + str(total_price_menu))
    return price
    
def daily_sales(menu):
    sales = []
    for m in menu:
        sales.append(int(input(m + " 몇 개 팔았나요?")))
    return sales

def daily_income(price, sales):
    income = 0
    for i in range(3):
        income += price[i] * sales[i]
    return income
    

def main():
    menu = load_menu()
    price = define_price(menu)
    sales = daily_sales(menu)
    income = daily_income(price, sales)
    print(income)

if __name__ == '__main__':
    main()