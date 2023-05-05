from bananaconvert import bconvert, fconvert
import json

#Set what the measuring item is & metric/imperial measurements
with open('settings.json') as s:
    settings = json.load(s)
    item = settings[0]["item"]
    measures = settings[0]["measures"]

#Heading
print('Welcome to How Many Banana?')

#Main loop
run = True
while run == True:
    print(f"\nYou are measuring with {item}s in the {measures} system.")
    get_input = input('Type C to convert, S to adjust settings, or Q to quit: ')
    match get_input:
        case 'C' | 'c':
            if measures == 'imperial':    
                feet = input("Enter a number in feet: ")
                inches = input("Enter a number in inches: ")
                num = fconvert(feet, inches)
                print(f"{feet} feet {inches} inches is {bconvert(num)} {item}s long!")
            else:    
                num = input("Enter a number in metres: ")
                print(f"{num}m is {bconvert(num)} {item}s long!")
        case 'S' | 's':
            updatesettings = [{'item': item, 'measures': measures}]
            while run == True:
                measures = input('Convert using metric or imperial system?\n')
                match measures.lower():
                    case 'metric':
                        measures = 'metric'
                        break
                    case 'imperial':
                        measures = 'imperial'
                        break
                    case _:
                        print("Sorry, please type 'metric' or 'imperial'")
                # item = input('What item would you like to measure with?\n')
            with open('settings.json', 'w') as s:
                json.dump(updatesettings, s, indent=2)
                print('Settings have been updated')
        case 'Q' | 'q':
            print('See you later!')
            break
        case _:
            print("Invalid input")

# with library.csv as item:
