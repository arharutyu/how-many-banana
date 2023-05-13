from settingsoop import convert_from_m, convert_from_i, get_input, Item
import settingsoop
from sys import argv
from termcolor import cprint

#Set kwarg as item name (if entered, else default to banana per bash script)
kw_input = argv[1]
kw_input = str(kw_input).lower()
settings = settingsoop.Settings()
active_item = Item(kw_input)

#Check kwarg item exists in library & update, else default to banana
if active_item.check_item(kw_input):
    settings.update_settings(active_item.item_name, settings.is_metric)
else:
    settings.update_settings('banana', settings.is_metric)

#Heading
with open('header.txt', 'r') as f:
    for line in f:
        print(line.rstrip())

with open('header2.txt', 'r') as f:
    for line in f:
        cprint(line.rstrip(), "light_yellow")
cprint("\n", 'black', 'on_light_yellow')

#Main loop
run = True
while run:
    #Settings retrieval
    settings = settingsoop.Settings()
    active_item = Item(settings.item)

    #Print current settings
    print(settings.__str__())
    
    #Ask user for input
    try:
        user_input = get_input("Enter 'C' to convert, 'S' to adjust settings, or '\Q' to quit: ").lower()
        match user_input:
                #Convert to banana feature
                case 'c':
                    item_length = active_item.item_length
                    if settings.is_metric == "True":
                        while run:
                            try:
                                met_length = get_input("Enter a number in metres: ")
                                float(met_length)
                                break
                            except ValueError:
                                cprint("That's not a number! Please enter a number", "red")
                        print(f'\n{met_length}m is:') 
                        cprint(f'{convert_from_m(met_length, item_length)} {active_item.item_name}s long!', 'black', 'on_light_yellow')
                    else:
                        while run:
                            try:
                                ask = get_input("Enter feet and inches separated by an apostrophe: ").split("\'")
                                feet = float(ask[0])
                                inches = float(ask[1].strip('\"'))
                                float(feet)
                                float(inches)
                                break
                            except ValueError:
                                cprint("Invalid input for imperial system. Enter two numbers seperated by an apostrophe.\n For example: 5'5 is 5 feet 5 inches", "red")
                        
                        met_length = convert_from_i(feet, inches)
                        print(f'\n{feet} feet {inches} inches is:')
                        cprint(f'{convert_from_m(met_length, item_length)} {active_item.item_name}s long!', 'black', 'on_light_yellow')
                        
                #Adjust settings feature
                case 's':
                    settings.update_measure()
                    active_item.get_item()
                    settings.update_settings(active_item.item_name, settings.is_metric)
                    cprint('Settings have been updated', "white", "on_dark_grey")

                #Error handling any other input
                case _:
                    cprint('Invalid input. Please try again.', "red")

    #Quit from menu
    except KeyboardInterrupt:
            print('\nSee you later!')
            quit()
    
                    