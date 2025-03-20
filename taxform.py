""" 
Chapter 2 Case Study Project
(Pages 30 - 31)
Program: taxform.py
2/24/2025
Application to calculate a person's income tax.
""" 

# Initialize the constants 
TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000.0
DEPENDENT_DEDUCTION = 3000.0

# Input phase
grossIncome = float(input("Please enter the gross income: "))
numDependents = int(input("Next, enter the number of dependents: "))

# Compute the income tax 
taxableIncome = grossIncome - STANDARD_DEDUCTION - (DEPENDENT_DEDUCTION * numDependents)
incomeTax = taxableIncome * TAX_RATE
incomeTax = round(incomeTax, 2)

# Output phase
print("For a gross income of $" + str(grossIncome) + " when claiming " + str(numDependents) + " dependents(s):")
print("The income tax is $" + str(incomeTax))
input("Press ENTER to exit the program")