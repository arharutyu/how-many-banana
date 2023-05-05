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