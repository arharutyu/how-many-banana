import csv, json
item_length = 0.13

with open('library.csv') as library:
    reader = csv.DictReader(library, delimiter=',')


def bconvert(metres):
    metres = float(metres)
    converted = metres / item_length
    return f'{converted:.2f}'

def fconvert(feet, inches):
    feet = float(feet)
    inches = float(inches)
    metres = (feet * 12 + inches) * .0254
    return metres

def check_library(item):
    item = str(item).lower()
    with open('library.csv') as library:
        reader = csv.DictReader(library, delimiter=',')
        for row in reader:
            if item in str(row): 
                return True
            
class Settings:
    def __init__(self, item, measures):
        self.item = item
        self.measures = measures
#Display current settings
    def __str__(self, item, measures):
        return f"\nYou are measuring with {item}s in the {measures} system."
#Update setting options
    def update_settings(self, item, measures):
        run = None
        update = [{'item': item, 'measures': measures}]
        while run == None:
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
        while run == None:
                #Item settings
                get_item = input('What item would you like to measure with?\n')
                
                if check_library(get_item):
                    update[0]['item'] = str(get_item)
                    item = get_item
                    break
                    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    # !!!!!!!!! MAKE SURE YOU ACTUALLY CODE THE CHANGE OF ITEM LENGTH IN BANANACONVERT.PY
                    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                else:
                      print(f"Looks like {get_item} isn't in the library. Would you like to add it's length now? (Yes/No) ")
                        #Add an item to the library


        with open('settings.json', 'w') as s:
                json.dump(update, s, indent=2)
                print('Settings have been updated')

        print(self.__str__(item, measures))