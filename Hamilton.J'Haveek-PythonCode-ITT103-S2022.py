Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Author: J'Haveek Hamilton
#Date Created: April 30, 2022
#Course: ITT103
#Purpose: To calculate and print the commission received by a salesperson

switch_exit = 1
while switch_exit == 1:
    salesperson_number = input("Please enter your salesperson number: ")
    class_sales = input("Please enter your class (1,2,3): ")
    sales = input("Please enter your sales amount: ")
    rate = 0
    if "class_sales" == 1:
        if sales <= 1000:
            rate = 6
        if 1000 < sales < 2000:
            rate = 7
        if sales >= 2000:
            rate = 10
    elif "class_sales" == 2:
        if sales < 1000:
            rate = 4
        if sales >= 1000:
            rate = 6
    elif "class_sales" == 3:
        rate = 4.5
    else:
        print("Error, incorrect class should be entered")
    if rate != 0:
        print("* commission:" + str(sales * rate/100))
    switch_exit = input("Enter the data again? (1-Yes, 0-No) ")    