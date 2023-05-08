import json, csv

# def get_input(prompt):
#      prompt = input(prompt)
#      if prompt.lower() == '\q':
#         raise KeyboardInterrupt

def convert_from_m(met_length, item_length):
        met_length = float(met_length)
        item_length = float(item_length)
        converted_length = met_length / item_length
        return f'{converted_length:.2f}'
    
def convert_from_i(feet, inches):
        feet = float(feet)
        inches = float(inches)
        met_length = (feet * 12 + inches) * .0254
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
        with open('settings.json') as s:
            settings = json.load(s)
            item = str(settings[0]["item_name"]).lower()
            is_metric = settings[0]["is_metric"]
        self.item = item
        self.is_metric = is_metric

    def update_settings(self, item_name, is_metric):
        update = [{'item_name': item_name, 'is_metric': str(is_metric)}]
        print(update)
        with open('settings.json', 'w') as s:
                json.dump(update, s, indent=2)
        return print('Settings have been updated')
    
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
            except ValueError:
                 print("Sorry, please type 'metric' or 'imperial'")
        
    
class Item:
    def __init__(self, item_name):
        self.item_name = item_name
        with open('library.csv') as library:
            reader = csv.DictReader(library, delimiter=',')
            for row in reader:
                                    
                    if item_name.lower() == row['item_name'].lower():
                        item_length = row['item_length']
        self.item_length = item_length

    def __repr__(self):
         item_name = self.item_name
         return f'item: {item_name}'
              
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
                    item_length = row['item_length']
                    break
        return item_length

    def add_item(self, item_name, item_length):
        item_name = str(item_name).lower()
        item_length = float(item_length)
        new_item = {"item_name": item_name, "item_length": item_length}
        with open('library.csv', 'a', newline='') as library:
            writer = csv.DictWriter(library, new_item.keys())
            writer.writerow(new_item)
        return print(f'{item_name} has been added to the library with a length of {item_length} metres.\n')
