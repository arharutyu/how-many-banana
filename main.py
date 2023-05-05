from bananaconvert import bconvert, fconvert
import bananaconvert
import json, csv

#Heading
print('Welcome to How Many Banana?')

#Main loop
run = True
while run == True:

#Set what the measuring item is & metric/imperial measurements

    with open('settings.json') as s:
        settings = json.load(s)
        item = str(settings[0]["item"]).lower()
        measures = str(settings[0]["measures"]).lower()
    settings = bananaconvert.Settings(item, measures)

    #set item length from library
    with open('library.csv') as library:
        reader = csv.DictReader(library, delimiter=',')
        for row in reader:
            if item == row['item']:
                item_length = row['length']    

    print(settings.__str__(item, measures))  

    get_input = input('Type C to convert, S to adjust settings, or Q to quit: ')
    match get_input.lower():
        #Convert to banana feature
        case 'c':
            if measures == 'imperial':    
                feet = input("Enter a number in feet: ")
                inches = input("Enter a number in inches: ")
                num = fconvert(feet, inches)
                print(f"{feet} feet {inches} inches is {bconvert(num, item_length)} {item}s long!")
            else:    
                num = input("Enter a number in metres: ")
                print(f"{num}m is {bconvert(num, item_length)} {item}s long!")

        #Adjust settings feature
        case 's':
            settings.update_settings(item, measures)
            # settings.refresh(item, measures)
            settings.__str__(item, measures)
            

        #Quit from menu
        case 'q':
            print('See you later!')
            break
        case _:
            print("Invalid input")