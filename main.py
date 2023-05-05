from bananaconvert import bconvert, fconvert, check_library
import json, csv


#Set what the measuring item is & metric/imperial measurements
with open('settings.json') as s:
    settings = json.load(s)
    item = str(settings[0]["item"]).lower()
    measures = str(settings[0]["measures"]).lower()

#Heading
print('Welcome to How Many Banana?')

#Main loop
run = True
while run == True:
    print(f"\nYou are measuring with {item}s in the {measures} system.")
    get_input = input('Type C to convert, S to adjust settings, or Q to quit: ')
    match get_input.lower():
        #Convert to banana feature
        case 'c':
            if measures == 'imperial':    
                feet = input("Enter a number in feet: ")
                inches = input("Enter a number in inches: ")
                num = fconvert(feet, inches)
                print(f"{feet} feet {inches} inches is {bconvert(num)} {item}s long!")
            else:    
                num = input("Enter a number in metres: ")
                print(f"{num}m is {bconvert(num)} {item}s long!")
        #Adjust settings feature
        case 's':
            updatesettings = [{'item': item, 'measures': measures}]
            #Metric/Imperial Settings
            while run == True:
                measures = input('Convert using metric or imperial system?\n')
                match measures.lower():
                    case 'metric':
                        updatesettings[0]['measures'] = 'metric'
                        break
                    case 'imperial':
                        updatesettings[0]['measures'] = 'imperial'
                        break
                    case _:
                        print("Sorry, please type 'metric' or 'imperial'")
            while run == True:
                #Item settings
                get_item = input('What item would you like to measure with?\n')
                
                if check_library(get_item):
                    updatesettings[0]['item'] = str(get_item)
                    item = get_item
                    break
                    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    # !!!!!!!!! MAKE SURE YOU ACTUALLY CODE THE CHANGE OF ITEM LENGTH IN BANANACONVERT.PY
                    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                else:
                      print(f"Looks like {get_item} isn't in the library. Would you like to add it's length now? (Yes/No) ")
                        #Add an item to the library


            #Update settings json file
            with open('settings.json', 'w') as s:
                json.dump(updatesettings, s, indent=2)
                print('Settings have been updated')

        #Quit from menu
        case 'q':
            print('See you later!')
            break
        case _:
            print("Invalid input")

# with library.csv as item:
