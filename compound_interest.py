# Name: Brian Gallagher
# Assignment:   Compound Interest
# Reflection:   I liked figuring out how to write out the equation in a format
#               that was usable in python.
#               
#               I only struggled with the equation formatting, but it was mostly
#               because I forgot to convert the percentage to it's equation value.
#               
#               Parenthesis were needed because python can only read equations on a
#               single line, so you need to manipulate the order of operations.
#               
#               1. Converting percentages for equations in the input
#               2. This assignment highlighted how planning a flow chart makes coding easier
#               3. Indirectly learned how compounding interest works
                
# Prompts user for the initial amount deposited
fPrincipalInterestBJG = float(input('Enter the starting principal: '))

# Prompts user for the annual interest rate percentage, and converts it into a
# usable number for equations 
fInterestRateBJG = float(input('Enter the annual interest rate: '))/100

# Prompts user for how many times per year the interest compounds
fAnnualCompoundingBJG = float(input('How many times per year is the interest compounded? '))

# Prompts user for number of years the account will be left alone
fYearsBJG = float(input('For how many years will the account earn interest? '))

# Calculates the variables 
fFinalAmountBJG = fPrincipalInterestBJG*((1+(fInterestRateBJG/fAnnualCompoundingBJG))**(fAnnualCompoundingBJG*fYearsBJG))

# Displays results to user, formatting it for money
print(f'At the end of {fYearsgBJG} years you will have ${fFinalAmountBJG:,.2f}')
