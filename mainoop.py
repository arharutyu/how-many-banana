from settingsoop import convert_from_m, convert_from_i, Item
import settingsoop
from sys import argv
from termcolor import cprint

#Set kwarg as item name (if entered, default to banana per bash script)
kw_input = argv[1]
kw_input = str(kw_input).lower()
settings = settingsoop.Settings()
active_item = Item(kw_input)

#Check kwarg item in library & update 
if active_item.check_item(kw_input):
    settings.update_settings(active_item.item_name, settings.is_metric)

#Default to banana if not
else:
    settings.update_settings('banana', settings.is_metric)


#Heading
cprint("Welcome to How Many Banana?", 'black', 'on_light_yellow')


#Main loop
run = True
while run:
    #Settings retrieval
    settings = settingsoop.Settings()
    active_item = Item(settings.item)

    # #Print current settings
    print(settings.__str__())
    
    #Ask user for input
    get_input = input("Enter 'C' to convert, 'S' to adjust settings, or '\Q' to quit: ")
    # try:
    match get_input.lower():
            #Convert to banana feature
            case 'c':
                item_length = active_item.item_length
                if settings.is_metric == "True":
                    while run:
                        try:
                            met_length = input("Enter a number in metres: ")
                            float(met_length)
                            break
                        except ValueError:
                            cprint("That's not a number! Please enter a number", "red")
                    
                    print(f'\n{met_length}m is:') 
                    cprint(f'{convert_from_m(met_length, item_length)} {active_item.item_name}s long!', 'black', 'on_light_yellow')
                else:
                    while run:
                        try:
                            feet = input("Enter a number in feet: ")
                            float(feet)
                            break
                        except ValueError:
                            cprint("That's not a number! Please enter a number", "red")
                    while run:    
                        try:                        
                            inches = input("Enter a number in inches: ")
                            float(inches)
                            break
                        except ValueError:
                            cprint("That's not a number! Please enter a number", "red")                            
                    met_length = convert_from_i(feet, inches)
                    print(f'\n{feet} feet {inches} inches is:')
                    cprint(f'{convert_from_m(met_length, item_length)} {active_item.item_name}s long!', 'black', 'on_light_yellow')
                    
        #Adjust settings feature
            case 's':
                settings.update_measure()
                active_item.get_item()
                settings.update_settings(active_item.item_name, settings.is_metric)
                cprint('Settings have been updated', "white", "on_dark_grey")
        #Quit from menu
            case '\q':
                print('See you later!')
                quit()
 
                    