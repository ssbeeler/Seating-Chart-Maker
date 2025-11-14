# Seating Chart Maker

This program randomizes students into groups given some specifications (students to group together, students who should not be together, and students who need specific seats). 

NOTE: This is a work in progress. The error-checking isn't particularly robust, and I'm sure I've missed some edge cases. Message me if you run into errors or have any questions!

## Download and Usage Instructions

**STEP 0: Download Python from https://www.python.org/downloads/**

**STEP 1: Download the program** 
  1. Click the green "<> Code" button
  2. Click "Download ZIP"
  3. Unzip files

**STEP 2: Put the program and specifications CSV file in a folder of your choosing**

**STEP 3: Edit the specifications file as desired**

**STEP 4: Right-click inside the folder where the program and specifications CSV file are located**

**STEP 5: Click "Open in Terminal"**

**STEP 6: Type ```python seating_chart.py``` to run the program**


## Specification Details
You can create several specification CSV files for your different sections. You can open CSV files in a text editor or in Excel (recommended). The parameters are as follows:
* ```Tables```: Number your tables using positive integers. If there are tables you want to leave empty if there's room, put them at the end.
    * Example: ```Tables,1,2,3,4,5,6,7,8,9```
        * If there's room, leave tables 9/8/7/etc. empty
* ```Seats Per Table```: List the number of seats per table using positive integers. These should correspond to the table numbers.
    * Example: ```Seats Per Table,3,3,3,3,3,3,3,3,2```
        * Tables 1-8 have 3 seats, table 9 has 2 seats
* ```Ideal Group Size```: To limit sparsely-populated tables, include a positive integer with the ideal number of students per group. Enter 0 if you don't want to deal with this.
    * Example: ```Ideal Group Size,3```
* ```Students```: List student names. Use underscores or hyphens for spaces (e.g., "Pooh B." should be entered as "Pooh_B.").
    * Example: ```Students,Apple,Banana,Blackberry,Sweet_Potato,...```
* ```Group Together```: List groups of students that should be grouped together. Format: NAME NAME
    * Example: ```Group Together,Blackberry Blueberry Raspberry,Apple Cranberry```
        * Blackberry, Blueberry, and Raspberry should be seated at the same table
        * Apple and Cranberry should be seated at the same table
* ```Do Not Pair```: List pairs of students that should not be grouped together. Format: NAME NAME
    * Example: ```Do Not Pair,Lemon Grape,Banana Orange```
        * Lemon and Grape should not be at the same table
        * Banana and Orange should not be at the same table
* ```Specify Table```: List students that need to sit at specific table(s). Format: NAME TABLE# TABLE#
    * Example: ```Specify Table,Plum 4 5,Cherry 1 2 3```
        * Plum feels most comfortable sitting at table 4 or table 5
        * Cherry needs to sit at table 1, 2, or 3 to see the board 

  
## Video Tutorial
