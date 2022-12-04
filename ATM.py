print("-------------------------------------------")
print("******Welcome to INDIAN OVERSEAS BANK******")
print("-------------------------------------------")
print("Insert Your ATM CARD properly...")
pin = int(input("Enter your pin number:"))
amt_limit = 20000
amount = 2000
if (pin == 7860):
    print("Select Your Language")
    print("1-Tamil")
    print("2-English")
    lg = int(input("Select Option:"))
    if lg == 1:
        mobile_no = int(input("Enter Your Mobile no:"))
        if (mobile_no == 1234567890):
            print(f"You Mobile No is {mobile_no}")
            print("Your Mobile No is CORRECT")
            print(" ")
            print("----------------------------")
            print("*****LOGIN SUCCESSFULLY*****")
            print("----------------------------")
            print(" ")
            print("1-Deposit")
            print("2-Withdraw")
            print("3-Balance query")
            print("4-Exit")
            print(" ")
            option = int(input("Enter your option:"))
        if (option == 1):
            deposit = int(input("Enter your Deposit amount:"))
            print("Deposit amount Properly")
            print(f"Your amount is {deposit}")
            print("Enter")
            print("Cancel")
            verify = (input("Select Your Option:"))
            print(" ")
            if verify == "Enter":
                if (deposit < amt_limit):
                    print("-------------------------")
                    print("Please Wait Processing...")
                    print("-------------------------")
                    print(" ")
                    print("--------------------------")
                    print("***Deposit Successfully***")
                    print("--------------------------")
            else:
                print("Invalid Cash...Thank you for visiting IOB")
    # ---------------------------------------------------------------------------
    # ************************IMPLEMENT 2ND OPTION*******************************
    # ---------------------------------------------------------------------------
        elif (option == 2):
            print("------------------------")
            withdraw = int(input("Enter Your Withdraw amount:"))
            print("******************")
            print(f"Your amount is {withdraw}")
            print("Enter")
            print("Cancel")
            verify = (input("Select Your Option:"))
            print(" ")
            if verify == "Enter":
                if (withdraw < amount):
                    print("Please Wait Processing...")
                    print(" ")
                    print("-------------------")
                    print("Collect Your Amount")
                    print("-------------------")
                elif (withdraw > amount):
                    print(" ")
                    print("-----------------------------")
                    print("You Have Insufficient Balance")
                    print("-----------------------------")
                    print(" ")
                else:
                    print("------------------")
                    print("Transaction Failed")
                    print("------------------")
    # ---------------------------------------------------------------------------
    # ************************IMPLEMENT 3rD OPTION*******************************
    # ---------------------------------------------------------------------------
        elif (option == 3):
            print("Enter the Correct Username and Password")
            count = 0
            while count < 3:
                username = input("Enter username:")
                password = input("Enter password:")
                if username == 'mohamed' and password == 'basith':
                    print("--------------")
                    print("Access Granted")
                    print("--------------")
                    print("Please Wait Processing....")
                    print("-------------------------------------")
                    print("Your Balance Amount is R.S. 15,000.00")
                    print("-------------------------------------")
                    print(" ")
                    print("-----------------------------------------------------")
                    print("*****Thank You For Visiting INDIAN OVERSEAS BANK*****")
                    print("-----------------------------------------------------")
                    break

                else:
                    print("----------------------------------")
                    print("Access Denied.....Try again later.")
                    print("----------------------------------")
                    count += 1
        elif (option == 4):
            print("EXIT OR CANCEL")
            print("1-YES")
            print("2-NO")
            exit = int(input("ARE YOU EXIT NOW:"))
            if (exit == 1):
                print(" ")
                print("-------------")
                print("You Are Exits")
                print("-------------")
                print(" ")
                print("****************************************************")
                print("$$$$$THANK YOU FOR CONNECT INDIAN OVERSEAS BANK$$$$$")
                print("****************************************************")
            else:
                print(" ")
                print("-------------------")
                print("Still Processing...")
                print("-------------------")
                print(" ")
                print("****************************************************")
                print("$$$$$THANK YOU FOR CONNECT INDIAN OVERSEAS BANK$$$$$")
                print("****************************************************")
    else:
        print("YOUR LANGUAGE IS ENGLISH")

else:
    print("")
    print("------------------")
    print("Transaction Failed")
    print("------------------")
    print(" ")
    print("-------------------------------------------------")
    print("$$$THANK YOU FOR VISITING INDIAN OVERSEAS BANK$$$")
    print("-------------------------------------------------")
    print(" ")
    print(" ")
    print("*******************************************************")
