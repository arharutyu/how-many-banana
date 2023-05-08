from settingsoop import Item, Settings
import settingsoop

# class Convert:

# def __init__(self, settings, input_Length):
#         self.settings = settings
#         self.input_Length = input_Length

def convert_from_m(met_length, item_name):
        met_length = met_length
        item_name = settingsoop.Item(item_name, item_length)
        item_length = Item.get_item_length(item_name)
        converted_length = met_length / item_length
        return f'{converted_length:.2f}'
    
def convert_from_i(self, feet, inches):
        self.feet = feet
        self.inches = inches
        met_length = (feet * 12 + inches) * .0254
        return met_length
    


