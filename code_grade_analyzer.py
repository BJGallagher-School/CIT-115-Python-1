# Name: Brian Gallagher
# Assignment:   Code Grade Analyzer
# Reflection:   I liked trying to streamline and simplify the code.
#               I keep struggling to remember that you can't simplify by grouping only
#               values with logical operatrors.
#               Once I planned it out in a list, I realized I could compare each score
#               with the others. However, I couldn't think of a way to prevent the code
#               from defaulting to dropping score 4 if there were any ties for lowest score,
#               outside of writing out for every possible 4 test combination.
#               1. How to nest elif into if/else statements.
#               2. Utilizing more than one action triggering with if/else statements.
#               3. How to use elif on it's own.


# Prompts user for their name
sUserNameBJG = input('What is your name? ')

# Prompts user for their 4 test scores as int variables
iScore1BJG = int(input('What is your first test score? Whole numbers only. '))
iScore2BJG = int(input('What is your second test score? Whole numbers only. '))
iScore3BJG = int(input('What is your third test score? Whole numbers only. '))
iScore4BJG = int(input('What is your fourth test score? Whole numbers only. '))

# Checks if any score is less than 0, and exits with a message if invalid value is found
if iScore1BJG < 0 or iScore2BJG < 0 or iScore3BJG < 0 or iScore4BJG < 0:
    print('Test scores must be greater than 0.')
    raise SystemExit

# Prompts user if the lowest score should be dropped or not
sDropBJG = input('Do you wish to drop the lowest grade Y or N? ')

# Checks if a Y or N was entered, and exits if invalid value is found
if sDropBJG != 'Y' and sDropBJG != 'N':
    print('Enter Y or N to drop the lowest grade.')
    raise SystemExit

# Calculates the lowest score if the user wants it dropped using nested if/else to compare
# each score for the lowest
if sDropBJG == 'Y':
    if iScore1BJG < iScore2BJG and iScore1BJG < iScore3BJG and iScore1BJG < iScore4BJG:
        iScoreTotalBJG = iScore2BJG + iScore3BJG + iScore4BJG
    elif iScore2BJG < iScore1BJG and iScore2BJG < iScore3BJG and iScore2BJG < iScore4BJG:
        iScoreTotalBJG = iScore1BJG + iScore3BJG + iScore4BJG
    elif iScore3BJG < iScore1BJG and iScore3BJG < iScore2BJG and iScore3BJG < iScore4BJG:
        iScoreTotalBJG = iScore1BJG + iScore2BJG + iScore4BJG
    else:
        iScoreTotalBJG = iScore1BJG + iScore2BJG + iScore3BJG
    iTestCountBJG = 3  # Applies the variable for total test number for final calculation alongside
                       # the elif statement for dropping the lowest score
else:  # If not dropping lowest, calculates test score total and changes the total test number variable  
    iScoreTotalBJG = iScore1BJG + iScore2BJG + iScore3BJG + iScore4BJG
    iTestCountBJG = 4

# Calculates the average score
fAverageScoreBJG = iScoreTotalBJG/iTestCountBJG

# Outputs the final average score to user
print(f"{sUserNameBJG}'s test average is: {fAverageScoreBJG:.1f}")

# Elif statement for comparing average score to which grade it should be
if fAverageScoreBJG >= 97:
    sFinalGradeBJG = "A+"
elif fAverageScoreBJG >= 94 and fAverageScoreBJG < 97:
    sFinalGradeBJG = "A"
elif fAverageScoreBJG >= 90 and fAverageScoreBJG < 94:
    sFinalGradeBJG = "A-"
elif fAverageScoreBJG >= 87 and fAverageScoreBJG < 90:
    sFinalGradeBJG = "B+"
elif fAverageScoreBJG >= 84 and fAverageScoreBJG < 87:
    sFinalGradeBJG = "B"
elif fAverageScoreBJG >= 80 and fAverageScoreBJG < 84:
    sFinalGradeBJG = "B-"
elif fAverageScoreBJG >= 77 and fAverageScoreBJG < 80:
    sFinalGradeBJG = "C+"
elif fAverageScoreBJG >= 74 and fAverageScoreBJG < 77:
    sFinalGradeBJG = "C"
elif fAverageScoreBJG >= 70 and fAverageScoreBJG < 74:
    sFinalGradeBJG = "C-"
elif fAverageScoreBJG >= 67 and fAverageScoreBJG < 70:
    sFinalGradeBJG = "D+"
elif fAverageScoreBJG >= 64 and fAverageScoreBJG < 67:
    sFinalGradeBJG = "D"
elif fAverageScoreBJG >= 60 and fAverageScoreBJG < 64:
    sFinalGradeBJG = "D-"
else:
    sFinalGradeBJG = "F"

# Outputs final grade to user
print(f"{sUserNameBJG}'s letter grade for the tests is: {sFinalGradeBJG}")
