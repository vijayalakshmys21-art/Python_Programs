menu=int(input("Enter the selected items: "))
match menu:
    case 1:print("Idly")
    case 2:print("Dosa")
    case 3:print("Pongal")
    case 4:print("Vada")
    case _:print("Invalid Choice")