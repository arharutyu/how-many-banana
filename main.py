from bananaconvert import bconvert, fconvert, check_library
import bananaconvert
import json, csv


#Set what the measuring item is & metric/imperial measurements

with open('settings.json') as s:
    settings = json.load(s)
    item = str(settings[0]["item"]).lower()
    measures = str(settings[0]["measures"]).lower()

settings = bananaconvert.Settings(item, measures)

#Heading
print('Welcome to How Many Banana?')
print(settings.__str__(item, measures))
#Main loop
run = True
while run == True:
    
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
            settings.update_settings(item, measures)
            settings.__str__(item, measures)

        #Quit from menu
        case 'q':
            print('See you later!')
            break
        case _:
            print("Invalid input")