# Contri Calculator
print("Welcome to Contri Calculator\n")
Bill = float(input("What was your Bill? $"))
Person = int(input("How many person you are "))
Tip = int(input("What the percentage of tip according to your Bill, 10,12,and 15.. "))
Total_Bill = (((Bill/100 * Tip)+ Bill)/Person)
Final_Bill = round(Total_Bill, 2)
print(f"Bill per person is {Final_Bill} ")