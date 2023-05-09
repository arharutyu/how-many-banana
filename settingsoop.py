import json, csv

# def get_input(prompt):
#      prompt = input(prompt)
#      if prompt.lower() == '\q':
#         raise KeyboardInterrupt

def convert_from_m(met_length, item_length):

    try:    
        met_length = float(met_length)
        item_length = float(item_length)
        converted_length = met_length / item_length

    except Exception:
         converted_length = 1
         print('Error in calculation, assuming converted length of 1')
          
    return f'{converted_length:.2f}'      
    
def convert_from_i(feet, inches):
    try:
        feet = float(feet)
        inches = float(inches)
        met_length = (feet * 12 + inches) * .0254

    except Exception:
         met_length = 1
         print('Error in calculation, assuming length of 1')

    return met_length
    

class Settings:
    def __init__(self):
        self.item = ' '
        self.is_metric = ' '
        self.retrieve_settings()

    def __str__(self):
        is_metric = self.is_metric
        item = self.item
        if is_metric == 'True':
             measure_name = 'metric'
        else:
             measure_name = 'imperial'
        return f"\nYou are measuring with {item}s in the {measure_name} system."

    def retrieve_settings(self):
        try:    
            with open('settings.json') as s:
                settings = json.load(s)
                item = str(settings[0]["item_name"]).lower()
                is_metric = settings[0]["is_metric"]
            self.item = item
            self.is_metric = is_metric

        except Exception:
             print("Something went very wrong, sorry it's broken.")
             quit()


    def update_settings(self, item_name, is_metric):
        try:    
            update = [{'item_name': item_name, 'is_metric': str(is_metric)}]
            with open('settings.json', 'w') as s:
                    json.dump(update, s, indent=2)
            return print('Settings have been updated')
        except Exception:
             print('Sorry, something went wrong. Settings were not updated.')
        
    def update_measure(self):
        run = None
        while run == None:
            try:
                get_is_metric = input('Convert using metric or imperial system?\n')
                match get_is_metric[0].lower():
                    case 'm':
                            self.is_metric = True
                            break
                    case 'i':
                            self.is_metric = False
                            break
                    case _:
                          raise ValueError
            except ValueError:
                 print("Sorry, please type 'metric' or 'imperial'")
        
    
class Item:
    def __init__(self, item_name):
        self.item_name = item_name
        self.item_length = ' '
        try:    
            with open('library.csv') as library:
                reader = csv.DictReader(library, delimiter=',')
                for row in reader:       
                    if item_name.lower() == row['item_name'].lower():
                        self.item_length = row['item_length']
        except:
            self.item_name = "banana"
            self.item_length = 0.13
            print("Something went wrong. Item has been set to default banana")

    def __repr__(self):
         item_name = self.item_name
         return f'item: {item_name}'
    
    def add_item(self, item_name, item_length):
        item_name = str(item_name).lower()
        item_length = float(item_length)
        new_item = {"item_name": item_name, "item_length": item_length}
        with open('library.csv', 'a', newline='') as library:
            writer = csv.DictWriter(library, new_item.keys())
            writer.writerow(new_item)
        return print(f'{item_name} has been added to the library with a length of {item_length} metres.\n')     
             
    def check_item(self, item_name):
        with open('library.csv') as library:
            reader = csv.DictReader(library, delimiter=',')
            for row in reader:
                if item_name in str(row).lower(): 
                    return True

    def get_item_length(self, item_name):
        item_length = self.item_length
        with open('library.csv') as library:
            reader = csv.DictReader(library, delimiter=',')
            for row in reader:
                if item_name == row['item_name']:
                    self.item_length = row['item_length']
                    break
        return item_length



    def get_item(self):
        run = True
        while run:
            get_input = input('What item would you like to measure with?\n')
            if self.check_item(get_input):
                self.item_name = get_input.lower()
                break
            else:
                while run:    
                    ask_add = input(f"Looks like {get_input} isn't in the library. Enter its' length in metres to add to the library. Enter 'S' to skip.\n")
                    if ask_add.lower() == 's':
                        break
                    elif ask_add <= '0':
                        print("Length must be a number greater than 0.")
                    else:
                        try:
                            self.item_name = get_input
                            self.item_length = float(ask_add)
                            self.add_item(self.item_name, self.item_length)
                            break                        
                        except ValueError:
                            print("Length must be a number greater than 0")
                        
                
                break