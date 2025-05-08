MATRIX: 297264  
NAME: ALYA FARHANA BINTI MOHD AZMI

## Introduction

This manual is meant to guide the user in operating this simple tax calculator program, beginning with installation, configuration, and operation of the Python-based tool. It also describes the workflow, logic, and structure of this code.

## Objective

The objective of the Malaysian Tax Input Program is to develop a Python program that allows the following:

* User registration and login via IC Number  
* Income and relief inputs to calculate the tax payable.  
* Storage and retrieval of data using CSV files.

As well as a practice for the use of pandas, CSV, Python variables, control flow, functions, and file operations.

## Background

This project simulates a real-world application where users can:

* Register and log in securely.  
* Input financial details to compute tax based on Malaysian guidelines.  
* Save and view tax history.

Technologies used include:

* Python (Core logic and I/O)  
* Pandas (for CSV manipulation)  
* CSV module (for user authentication data)

## Initial setup and configuration

### 1\. Install Python

Recommended version: Python 3.10 or later  
Download: [https://www.python.org/downloads](https://www.python.org/downloads)

### 2\. Install pandas

Run this code in the terminal:  
\[pip install pandas\] *(without the \[ \])*

### 3\. Ensure the paths are set correctly

Check where the pandas is installed:  
*pip show pandas*  
Find the line that says:  
*Location: C:\\Users\\YourName\\... (or similar)*  
Then type:  
*where python*  
This will show the full path:  
Example: *C:\\Users\\YourName\\AppData\\Local\\Programs\\Python\\Python311\\python.exe*

Ensure your Python interpreter points to the version with pandas installed.

## Methodology/Workflow

1. Start the program  
   1. After the file installations are completed, double-click the **autorun.cmd** to start the program.  
   2. The User will then be prompted to register (for new users) or log in (existing users).  
2. User Registration  
   1. Users enter a unique **user\_id** and a 12-digit IC Number  
   2. The User information (IC number and user\_id) will be stored in a CSV file.  
   3. Registered Users will be directed to log in  
3. Login Authentication  
   1. Users log in using their **user\_id** and **password** (the last 4 digits of their IC).  
   2. The credentials are verified using the logic written in **functions[.](http://functions.py)py**  
4. Tax Input and Calculation  
   1. Valid Users input their annual income and tax relief  
   2. The system proceeds to calculate tax based on:  
      1. **chargeable\_income \= income \- tax\_relief**  
      2. The Tax system is applied according to the current (2025) Malaysian tax rates.  
5. Data Storage and Viewing  
   1. The results (user ID, IC, income, relief, tax payable) are stored in **tax\_records.csv** using pandas.  
   2. Users can view all past tax records.

## Basic Operations

* Registering a new User  
* Login Authentication  
* Entering tax Details  
* Saving and Viewing Data

## Troubleshooting and FAQs

**Q: I get the "Import 'pandas' could not be resolved" error.**  
*A: Make sure pandas is installed in the environment you're using. You can also try restarting your IDE and confirming the correct Python interpreter is selected.*

**Q: My registration isn’t saved after restarting the program.**  
*A: Ensure **save\_user\_to\_csv()** is called after registration and that you’re reading users from the file at the start using **load\_users\_from\_csv()**.*

**Q: Login isn’t working even with the correct credentials.**  
*A: Make sure **registered\_users** is loaded from the CSV, not just stored in memory. (e.g., registered\_users \= {}, this causes the dictionary to become empty.)*

**Q: The Login still isn’t working after cross-checking the code.**  
*A: At line 5 of the main.py code, \[ \# print (registered\_users) || Used during testing to see if the users were saved \] remove the \[ \# \] and everything after and including \[ || \]. Rerun the program, it should print the currently existing users. Cross-check if the login details that were input were correct.*

**Q: I don’t see tax records after entering them.**  
*A: Check that the file **citizen\_tax\_records.csv** is written correctly using **save\_to\_csv()***.

## 

## References

*CSV \- csv file reading and writing*. Python documentation. (n.d.). https://docs.python.org/3/library/csv.html 

*Tax rate*. Lembaga Hasil Dalam Negeri Malaysia. (n.d.). https://www.hasil.gov.my/en/individual/individual-life-cycle/how-to-declare-income/tax-rate/ 

*Pandas Documentation*. pandas documentation \- pandas 2.2.3 documentation. (n.d.). https://pandas.pydata.org/docs/ 

