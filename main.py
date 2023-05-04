from bananaconvert import bconvert
import settings

#Set what the measuring item is & metric/imperial measurements
item = 'banana'
measures = 'metric'
run = True

print('Welcome to How Many Banana?')

#Main loop
while run == True:
    print(f"\nYou are measuring with {item}s in the {measures} system.")
    get_input = input('Type C to convert, S to adjust settings, or Q to quit: ')
    match get_input:
        case 'C':
            num = input("Enter a number in metres: ")
            print(f"{num}m is {bconvert(num)} {item}s long!")
        case 'S':
            pass
        case 'Q':
            print('See you later!')
            break
        case _:
            print("Invalid input")

# with library.csv as item:
