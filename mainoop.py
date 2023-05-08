# from convert import Convert
from settingsoop import Settings, Item, convert_from_m, convert_from_i
import json, convert, settingsoop

#Heading
print('Welcome to How Many Banana?')


#Main loop
run = True
while run == True:
    #Settings retrieval
    settings = settingsoop.Settings()

    # #Print current settings
    print(settings.__str__())
    
    #Ask user for input
    get_input = input("Enter 'C' to convert, 'S' to adjust settings, or '\Q' to quit: ")
    # try:
    match get_input.lower():
            #Convert to banana feature
            case 'c':
                item = settingsoop.Item(settings.item)
                item_length = item.item_length
                if settings.is_metric:
                    met_length = input("Enter a number in metres: ")
                    print(f'{met_length}m is {convert_from_m(met_length, item_length)} {item_name}s long!')
                else:
                    feet = input("Enter a number in feet: ")
                    inches = input("Enter a number in inches: ")
                    met_length = convert_from_i(feet, inches)
                    print(f'{feet} feet {inches} inches is {convert_from_m(met_length, item_length)} {item_name}s long!')
                
        #Adjust settings feature
            case 's':
                settings.update_measure()
                settings.update_settings(settings.item, settings.is_metric)
                

             
        #Quit from menu

            case '\q':
                print('See you later!')
    # except KeyboardInterrupt:
 
                    