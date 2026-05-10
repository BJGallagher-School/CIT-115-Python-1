# Name: Brian Gallagher
# Assignment:   Compound Interest Loops

# Input and error checking loop prompting the original account balance
while (fDepositBJG := float(input('What is the original deposit (positive value): '))) <= 0:
    print('Input must be a positive numeric value')

# Input and error checking loop prompting the interest rate. It is converted to a usable number for 
# monthly calculations
while (fInterestRateBJG := (float(input('What is the interest rate (positive value): '))/100)/12) <= 0:
    print('Input must be a positive numeric value')
    
# Input and error checking loop prompting the amount of months to be calculated
while (iMonthsBJG := int(input('What is the number of months (positive value): '))) <= 0:
    print('Input must be a positive numeric value')

# Input and error checking loop prompting the users final goal amount
while (fGoalBJG := float(input('What is the goal amount (can enter 0 but not negative): '))) < 0:
    print('Input must be a 0 or positive numeric value')

# Since I will need to modify the deposit variable for two different loops, I assigned it a new value 
fAccountTotalBJG = fDepositBJG

# Loops the calculation for monthly accrual, and outputs the new values for each month
for iLoopCountBJG in range(iMonthsBJG):
    fAccountTotalBJG += (fAccountTotalBJG * fInterestRateBJG)
    print(f"Month: {iLoopCountBJG + 1} Account balance is: ${fAccountTotalBJG:,.2f}") 

# Since I will need to modify the deposit variable for two different loops, I assigned it a new value 
fAccountGoalBJG = fDepositBJG

# The variable for counting how many months  it will take to reach the entered goal
iGoalLengthBJG = 0

# Loop calculating how many months to reach the entered goal. It compares the amount from each loop
# against the goal, closing the loop once it becomes higher than the goal
while fAccountGoalBJG < fGoalBJG:
    fAccountGoalBJG += (fAccountGoalBJG * fInterestRateBJG)
    iGoalLengthBJG += 1

# Outputs the amount of months it will ttake to reach the goal    
print(f"It will take {iGoalLengthBJG:,} months to reach the goal of ${fGoalBJG:,.2f}")
