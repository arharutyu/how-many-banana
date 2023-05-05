import csv
item_length = 0.13

def bconvert(metres):
    metres = float(metres)
    converted = metres / item_length
    return f'{converted:.2f}'

def fconvert(feet, inches):
    feet = float(feet)
    inches = float(inches)
    metres = (feet * 12 + inches) * .0254
    return metres

def check_library(check_item):
    check_item = check_item
    with open('library.csv') as library:
                reader = csv.DictReader(library, delimiter=',')
                for row in reader:
                    if check_item not in str(row): 
                          return False