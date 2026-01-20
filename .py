
num = int(input("Enter a number (1-3): "))

match num:
    case 1:
        print("You entered One")
    case 2:
        print("You entered Two")
    case 3:
        print("You entered Three")
    case _:
        print("Invalid number")
