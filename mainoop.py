# from convert import Convert
from settingsoop import Settings, Item, convert_from_m, convert_from_i
import settingsoop

#Heading
print('Welcome to How Many Banana?')


#Main loop
run = True
while run == True:
    #Settings retrieval
    settings = settingsoop.Settings()
    active_item = settingsoop.Item(settings.item)

    # #Print current settings
    print(settings.__str__())
    
    #Ask user for input
    get_input = input("Enter 'C' to convert, 'S' to adjust settings, or '\Q' to quit: ")
    # try:
    match get_input.lower():
            #Convert to banana feature
            case 'c':
                # item = settingsoop.Item(settings.item)
                item_length = active_item.item_length
                if settings.is_metric == "True":
                    while run == True:
                        try:
                            met_length = input("Enter a number in metres: ")
                            int(met_length)
                        except ValueError:
                            print("That's not a number! Please enter a number")

                    print(f'{met_length}m is {convert_from_m(met_length, item_length)} {active_item.item_name}s long!')
                else:
                    while run == True:
                        try:
                            feet = input("Enter a number in feet: ")
                        except ValueError:
                            print("That's not a number! Please enter a number")
                        try:                        
                            inches = input("Enter a number in inches: ")
                        except ValueError:
                            print("That's not a number! Please enter a number")                            
                            met_length = convert_from_i(feet, inches)
                            print(f'{feet} feet {inches} inches is {convert_from_m(met_length, item_length)} {active_item.item_name}s long!')
                    
        #Adjust settings feature
            case 's':
                settings.update_measure()
                active_item.get_item()
                settings.update_settings(active_item.item_name, settings.is_metric)
             
        #Quit from menu
            case '\q':
                print('See you later!')
                quit()
 
                    