price_menu01 = 0
price_menu02 = 0
price_menu03 = 0

def total_price(price_menu01, price_menu02, price_menu03):
    total = int(price_menu01) + int(price_menu02) + int(price_menu03)
    return total

def total_price_global():
    global price_menu01
    global price_menu02
    global price_menu03
    total = int(price_menu01) + int(price_menu02) + int(price_menu03)
    return total

def menu_income(count_menu01, count_menu02, count_menu03):
    global price_menu01
    global price_menu02
    global price_menu03
    
    total_menu01_income = int(price_menu01) * int(count_menu01)
    total_menu02_income = int(price_menu02) * int(count_menu02)
    total_menu03_income = int(price_menu03) * int(count_menu03)
    
    return total_menu01_income + total_menu02_income + total_menu03_income

def daily_sales_income():
    count_menu01 = int(input("메뉴1은 몇개 팔았나요?"))
    count_menu02 = int(input("메뉴2는 몇개 팔았나요?"))
    count_menu03 = int(input("메뉴3은 몇개 팔았나요?"))
    
    print(menu_income(count_menu01, count_menu02, count_menu03))
    

def define_price():
    global price_menu01
    global price_menu02
    global price_menu03
    
    f_menu = open("../kitchin_menu.txt", 'r')
    line = f_menu.readline()
    price_menu01 = input(line + "의 가격은 얼마입니까?")
    line = f_menu.readline()
    price_menu02 = input(line + "의 가격은 얼마입니까?")
    line = f_menu.readline()
    price_menu03 = input(line + "의 가격은 얼마입니까?")
    f_menu.close()
    
    #is fail!!
    # total_price_menu = price_menu01 + price_menu02 + price_menu03
    # total_price_menu = total_price(price_menu01, price_menu02, price_menu03)
    total_price_menu = total_price_global()
    print(total_price_menu)

def main():
    define_price()
    
    daily_sales_income()

if __name__ == '__main__':
    main()