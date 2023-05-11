# How Many Banana?

# R1

Answers to all the _documentation requirements_ below.

# R2

Your `README.md` should have a separate heading for each _documentation requirement_ and answers organised under the appropriate headings.

# R3 References

Attribution to referenced sources will be provided per requirement for ease of access.

# R4 Source Control Repository

https://github.com/arharutyu/how-many-banana

# R5 Styling Conventions

Identify any code style guide or styling conventions that the application will adhere to.

Reference the chosen style guide appropriately.

## Reference


# R6 List of Features

**Develop** a list of features that will be included in the application. It must include:  
- at least THREE **features**  
- **describe** each feature  
  
**Note:** **Ensure** that your features above allow you to demonstrate your understanding of the following language elements and concepts:  
- use of variables and the concept of variable scope  
- loops and conditional control structures  
- error handling  
  
**Consult with your educator** to check your features are sufficient .

## Feature 1:

## Feature 3:

## Feature 2:


# R7 Implementation Plan

**Develop** an implementation plan which:  
- **outlines** how each feature will be implemented and a checklist of tasks for each feature  
- prioritise the implementation of different features, or checklist items within a feature  
- provide a deadline, duration or other time indicator for each feature or checklist/checklist-item  
  
Utilise a suitable project management platform to track this implementation plan.

Provide screenshots/images and/or a reference to an accessible project management platform used to track this implementation plan. 

  
> Your checklists for each feature should have at least 5 items.

# R8 Help Documentation

**Design** help documentation which includes a set of instructions which accurately **describe** how to use and install the application.  
  
You must include:  
- steps to install the application  
- any dependencies required by the application to operate  
- any system/hardware requirements  
- how to use any command line arguments made for the application

### Requirements
WSL or Linux
Python version 3.10 or higher

### Dependencies
csv, json modules (no install required)

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
To exit the program enter ```\Q``` at the menu

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

