# How Many Banana?
---
# R3 References

Attribution to referenced sources will be provided per requirement grouping (if present) for ease of access.

# R4 Source Control Repository

[GitHub Repository](https://github.com/arharutyu/how-many-banana)

# R5 Styling Conventions

Identify any code style guide or styling conventions that the application will adhere to.

Reference the chosen style guide appropriately.

## Reference


# R6 List of Features
## Feature 1: Menu
Looping landing point to navigate to convert + settings features
Navigation to be done by match case to avoid issues caused by (incorrect) user input
Exit program available here

## Feature 2: Convert functions
This feature operates with conditional control structure depending on the is_metric variable from settings. If is_metric is true, user inputs measurements in meters, output converted to bananas.
If is_metric is false, user inputs measures in feet/inches, this is converted to meters, then converted to bananas for the output.

## Feature 3: Adjust settings (item/length, and imperial/metric)
Settings kept in JSON file - allows for updating & program to remember previous settings.
Stores values of global variables/objects, and methods to retrieve, and update values.
An additional loop can be put in to allow for new items to be added if the user input is not matched to the existing library. (Lower priority - extra featurel in feature)

# R7 Implementation Plan

## Identify global objects/variables, and classes for main features

## Global Objects
### Item
- Item name
- Item length
### Measure
- Is Metric Boolean


## Convert Functions
### Description
Contains methods to perform conversions which make the main feature of the app
### Properties
- settings (item, measure)
- input length (length)
- converted length 
### Methods
- convert from met length to item length
- convert from imp length to met length
### Notes
Default measuring system is metric, & calculations done in metres (m)

## Settings Class
### Description
Contains methods to to access stored settings information, and update settings.
### Properties
- item (item name, item length)
- measure system (measure type)
### Methods
- retrieve information from settings file
- update information in settings file

## Item Class
### Description
Contains methods that work with the item object in settings
### Properties
- item name
- item length
### Methods
- check item name in library
- get item details from library
- add item details to library
- change item details in library (optional)

## Prioritization and tracking
Feature development priorities:
1. convert functions: as the basis of the core functionality of the app the function definitions for conversion are the highest priority.
2. menu: as the main loop to apply the functions the menu feature is also high priority.
3. adjust settings: containing the methods to update global objects/variables and loops within loops, this feature requires 1 & 2 to be complete before it can be applied.

Tracking and due dates were done via trello at the following link: [Trello Board](https://https://trello.com/b/UWY9MUmn)

Priorities for feature boards were highlighted with red tags, and within the checklist for each feature were ordered by importance.
Projected due dates are noted in the checklist.

A card will start in the 'Backlog' column, and make it's way across to the 'Done' column as work is complete.

![Trello board implementation plan, boards left to right: backlog, design, to-do, doing, code review, testing, done](/docs/trellooverview.png)

Convert functions were split in two as the default metric was used in the base level design of the code

![Convert functions trello cards screenshots, left: convert from imperial, right: convert from metric](/docs/trelloconvert.png)

Menu

![menu trello card screenshot](/docs/trellomenu.png)

Adjust settings was also split into two as 'adding item' to library is not part of the core functionality of the program.

![Settings trello cards screenshots, left: adjust settings, right: add item](/docs/trellosettings.png)


# R8 Help Documentation

### Requirements
- WSL or Linux
- Python version 3.10 or higher

### Dependencies
- csv, json, and sys modules (no install required)
- termcolor 2.3.0 (installed via script)

*For assessment purposes only, the following pytest dependencies are also required:*
- exceptiongroup 1.1.1
- iniconfig 2.0.0
- packaging 23.1
- pluggy 1.0.0
- pytest 7.3.1
- tomli 2.0.1


### Installation
*Please ensure your computer has all requirements to run the program successfully*

1. Fork 'How Many Bananas?' remote repository to your GitHub account
2. Clone repository to local machine
3. Use cmd to navigate to main repository directory
4. Run the following command: ```./wrapper.sh```
	1. If this results in permission denied, run the following script: ```chmod +x wrapper.sh```
	2. Repeat step 4
5. Enjoy converting bananas!

### Using the Program
Step 4 of installation above is the command to run the program.
You have the option to add a keyword argument and specify the item to use for converting as follows:
``` ./wrapper.sh itemname ```

*For example: if you want to run the program to measure with apples, you would enter the command:* ``` ./wrapper.sh apple ```

If the item specified is not in the library, or no item is specified, the program will default to measuring with bananas.

#### Menu
The main menu will present you with 3 options:
- Convert
- Adjust Settings
- Quit

#### Converting
Enter a standard length (metres or feet/inches), and the program will convert into standard banana length, and reset.

#### Settings
The units used for converting can be adjusted here. You can update two settings:
1. Measuring system: The program offers 2 conversion types. Metric (from metres to banana), or Imperial (from feet & inches to banana)
2. Item: The item used for converting

The program comes with a few pre programmed lengths of standard fruit/ items for your measuring pleasure. If you try to measure with an item that is not in the library, you will be prompted to add its' length, and the library will save these details for future conversion.

#### Quit
To exit the program enter ```\Q``` from any input request

#### Library 
Fruits and measurements in the standard library include:

| Item      | Measurement |
| ----------- | ----------- |
| Banana      | 0.19       |
| Apple   | 0.06        |
| Kiwi   | 0.05        |
| Pear   | 0.09        |
| Washing Machine   | 0.75        |
| Argine   | 1.64        |

*Note: The default system for this program is metric, and item lengths are stored in metres*

