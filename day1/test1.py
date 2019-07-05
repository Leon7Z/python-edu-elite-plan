if __name__ == '__main__':
    age = 28
    a = True
    while a:
        user_input = int(input("请猜年龄："))
        if user_input == age:
            print("Bingo!")
            break
        elif user_input < age:
            print("小了")
        else:
            print("大了")
