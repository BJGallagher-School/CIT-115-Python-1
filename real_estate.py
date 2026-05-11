# Name: Brian Gallagher
# Assignment:   Real Estate Analyzer
# Reflection:   I liked figuring out the loop for appending the list data.
#               I keep struggling to remember the exact directionality of how
#               functions pass variables.
#               I think the simplest way to describe a list is that it's like
#               a variable that can hold more than one value at a time. It helps
#               simplify the overall code by centralizing a pool of data, and is very
#               versitile with how it's data can be manipulated.
#               Lists could have been implemented in the Grade Analyzer assignment.
#               Instead of assigning variables to every single test, they could all
#               be entered in a list, and it also could have made the amount of entries
#               more flexible. If you made it a two-dimensional list, it could've
#               also expanded to include multiple tests and students.


def main():
    # Start with creating an empty list
    lstSalesPricesBJG = []

    # Calls the function for inputing the first property
    fSalesPriceBJG = getFloatInput("Enter property sales value: ")

    # Adds the returned value to the end of the list
    lstSalesPricesBJG.append(fSalesPriceBJG)

    # Prompts the user if another property needs entry
    sMoreInputBJG = input("Enter another value Y or N:")

    # Validates the Y/N response, and repeats if entry is invalid
    while sMoreInputBJG != "Y" and sMoreInputBJG != "y" and \
          sMoreInputBJG != "N" and sMoreInputBJG != "n":
        print("Error: Please enter Y or N.")
        sMoreInputBJG = input("Enter another value Y or N:")

    # Initiates a loop if Y/y was input, until a N/n is input
    while sMoreInputBJG == "Y" or sMoreInputBJG == "y":
        # Gets the next property
        fSalesPriceBJG = getFloatInput("Enter property sales value: ")
        # Append the new value to the list.
        lstSalesPricesBJG.append(fSalesPriceBJG)
        # Ask whether to continue entering values
        sMoreInputBJG = input("Enter another value Y or N:")
        # Validate the Y/N response again inside the loop.
        while sMoreInputBJG != "Y" and sMoreInputBJG != "y" and \
              sMoreInputBJG != "N" and sMoreInputBJG != "n":
            print("Error: Please enter Y or N.")
            sMoreInputBJG = input("Enter another value Y or N:")

    # Sorts the values in the list in default ascending
    lstSalesPricesBJG.sort()

    # Displays all items from list in a formatted way
    iPropertyNumBJG = 1  # Counter to display which property
    for fSaleBJG in lstSalesPricesBJG:
        print(f"Property {iPropertyNumBJG}  ${fSaleBJG:>12,.2f}")
        iPropertyNumBJG += 1  # Increment the property counter each iteration

    # Calculates the minimum value
    fMinBJG = min(lstSalesPricesBJG)

    # Calculates the maximum value
    fMaxBJG = max(lstSalesPricesBJG)

    # Calculates the sum of the values
    fTotalBJG = sum(lstSalesPricesBJG)

    # Calculates the average value using the sum total,
    # and len for length of the list
    fAverageBJG = fTotalBJG / len(lstSalesPricesBJG)

    # Calls the funtion for calculating the median
    fMedianBJG = getMedian(lstSalesPricesBJG)

    # Calculates the commission value
    fCommissionBJG = fTotalBJG * 0.03

    # Displays the previous 6 calculations from above in a formatted way
    print(f"{'Minimum:':<11} ${fMinBJG:>12,.2f}")
    print(f"{'Maximum:':<11} ${fMaxBJG:>12,.2f}")
    print(f"{'Total:':<11} ${fTotalBJG:>12,.2f}")
    print(f"{'Average:':<11} ${fAverageBJG:>12,.2f}")
    print(f"{'Median:':<11} ${fMedianBJG:>12,.2f}")
    print(f"{'Commission:':<11} ${fCommissionBJG:>12,.2f}")

# Function for validating inputs
def getFloatInput(sPromptBJG):
    # Keep looping until a valid value is obtained. 'while True' creates an
    # infinite loop that only exits when an approved value is returned
    while True:
        try:
            # Checks if the input is a working float
            fValueBJG = float(input(sPromptBJG))

            # Checks if the number is greater than zero, and prints an error if not
            if fValueBJG <= 0:
                print("Error: Please enter a positive, non-zero number.")
            else:
                # Input is valid, so the loop is closed, and a valid value is returned
                return fValueBJG
        except ValueError:
            # The message printed when a non-float input is detected. Loops back to input
            print("Error: Invalid input. Please enter a numeric value.")

def getMedian(lstValuesBJG):
    # Find out how many items are in the list
    iCountBJG = len(lstValuesBJG)

    # Determines if the item count is even or odd
    if iCountBJG % 2 == 1:
        # Odd number of entries, so the median item index can directly be returned
        iMiddleIndexBJG = iCountBJG // 2
        fMedianBJG = lstValuesBJG[iMiddleIndexBJG]
    else:
        # Even number of entries, so the median is calculated between the two item indexes
        iUpperMiddleBJG = iCountBJG // 2
        iLowerMiddleBJG = iUpperMiddleBJG - 1
        fMedianBJG = (lstValuesBJG[iLowerMiddleBJG] + lstValuesBJG[iUpperMiddleBJG]) / 2

    # Return the calculated median
    return fMedianBJG

if __name__ == '__main__':
    main()