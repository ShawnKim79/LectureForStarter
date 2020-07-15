def main():
    print("안녕하세요 사장님!")
    owner_name = input("사장님의 이름을 알려주세요:")
    
    print(owner_name + " 사장님 앞으로 멋진 식당을 만들어봐요")
    
    menu01 = input("첫번째 메뉴 이름을 정해주세요: ")
    menu02 = input("두번째 메뉴 이름을 정해주세요: ")
    menu03 = input("세번째 메뉴 이름을 정해주세요: ")
    
    print("이 식당에서는 아래와 같은 요리를 먹을수 있습니다.")
    print(menu01)
    print(menu02)
    print(menu03)

if __name__ == '__main__':
    main()