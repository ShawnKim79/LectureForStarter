import os.path

def register_kitchin_owner():
    owner_name = input("사장님의 이름을 알려주세요:")
    print(owner_name + " 사장님 앞으로 멋진 식당을 만들어봐요")    
    
    f_kitchin_name = open("../owner_name.txt", 'w')
    f_kitchin_name.write(owner_name)
    f_kitchin_name.close()
      
    os.path.isfile("../kitchin_menu.txt")

def hello_kitchin_owner():
    f_kithcin_name = open("../owner_name.txt", 'r')
    while True:
        line = f_kithcin_name.readline()
        if not line: break
        print(line)
    
    f_kithcin_name.close()

def register_menu():
    menu01 = input("첫번째 메뉴 이름을 정해주세요: ")
    menu02 = input("두번째 메뉴 이름을 정해주세요: ")
    menu03 = input("세번째 메뉴 이름을 정해주세요: ")
    
    print("이 식당에서는 아래와 같은 요리를 먹을수 있습니다.")
    print(menu01)
    print(menu02)
    print(menu03)
    
    f_menu = open("../kitchin_menu.txt", 'w')
    f_menu.write(menu01 + '\n')
    f_menu.write(menu02 + '\n')
    f_menu.write(menu03 + '\n')
    f_menu.close()
    
def print_menu_list():
    f_menu = open("../kitchin_menu.txt", 'r')
    while True:
        line = f_menu.readline()
        if not line: break
        print(line)
    
    f_menu.close()

def main():
    print("안녕하세요 사장님!")
    if(os.path.isfile("../owner_name.txt")):
        hello_kitchin_owner()
    else:
        register_kitchin_owner()
    
    if(os.path.isfile("../kitchin_menu.txt")):
        print_menu_list()
    else:
        register_menu()

if __name__ == '__main__':
    main()