import csv, json
            
class Settings:
    def __init__(self, item, measures):
        self.item = item
        self.measures = measures
#Display current settings
    def __str__(self, item, measures):
        return f"\nYou are measuring with {item}s in the {measures} system."
#Update setting options
    def update_settings(self, item, measures):
        uprun = None
        update = [{'item': item, 'measures': measures}]
        while uprun == None:
            measures = input('Convert using metric or imperial system?\n')
            match measures.lower():
                case 'metric':
                        update[0]['measures'] = 'metric'
                        break
                case 'imperial':
                        update[0]['measures'] = 'imperial'
                        break
                case _:
                        print("Sorry, please type 'metric' or 'imperial'")
        while uprun == None:
                #Item settings
                get_item = input('What item would you like to measure with?\n')
                
                if check_library(get_item):
                    update[0]['item'] = str(get_item)
                    item = get_item
                    break
                else:
                        ask_add = input(f"Looks like {get_item} isn't in the library. If you'd like to add it, please enter its' length in metres. Enter 'Q' to skip.\n")
                        if ask_add[0].lower() == 'q':
                                break
                            #Add an item to the library
                        elif float(ask_add):
                                add_library(get_item, ask_add)
                                print(f"{get_item} has been added to the library with a length of {ask_add}m")
                                item = get_item
                                break
                        

        #Update settings.json with new settings
        with open('settings.json', 'w') as s:
                json.dump(update, s, indent=2)
                print('Settings have been updated')
         
#convert from metres to banana(/item)
def bconvert(metres, item_length):
    metres = float(metres)
    converted = metres / float(item_length)
    return f'{converted:.2f}'

#convert from imperial to metres
def fconvert(feet, inches):
    feet = float(feet)
    inches = float(inches)
    metres = (feet * 12 + inches) * .0254
    return metres

#Check if item already in library
def check_library(item):
    item = str(item).lower()
    with open('library.csv') as library:
        reader = csv.DictReader(library, delimiter=',')
        for row in reader:
            if item in str(row).lower(): 
                return True

def add_library(item, length):
     item = str(item).lower()
     length = float(length)
     new_item = {"item": item, "length": length}
     with open('library.csv', 'a') as library:
          writer = csv.DictWriter(library, new_item.keys())
          writer.writerow(new_item)
          


