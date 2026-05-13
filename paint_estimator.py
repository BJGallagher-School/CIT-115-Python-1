# Name: Brian Gallagher
# Assignment:   Paint Estimator
# Reflection:   I liked figuring out how to translate the commands so that the data written
#               to the txt file would match what was printed on screen.
#               I struggle to remember how variables are passed through functions and their
#               calls.
#               A function is basically a macro, a saved preconstructed list of instructions,
#               that can be used whenever needed. You code a sequence of instructions into a
#               block, and then when you need to execute the sequence, you simply call the
#               functions name, and pass any variables to it as needed.
#               Functions should be used whenever a sequence of instructions needs to be used
#               more than once. You should also use them because they are easy to reuse and
#               repurpose in other projects.

def main():
    # Each call passes a prompt string and stores the returned validated float
    fWallSpaceBJG = getFloatInput("Enter wall space in square feet: ")
    fPaintPriceBJG = getFloatInput("Enter paint price per gallon: ")
    fFeetPerGalBJG = getFloatInput("Enter feet per gallon: ")
    fLaborHrsPerGalBJG = getFloatInput("How many labor hours per gallon: ")
    fLaborChargeBJG = getFloatInput("Labor charge per hour: ")

    # Collect the strings needed for the main function
    sStateBJG = input("State job is in (Enter in CAPS): ")
    sLastNameBJG = input("Customer Last Name: ")

    # Calls the function for calculating the integer for how many gallons needed 
    iGallonsBJG = getGallonsOfPaint(fWallSpaceBJG, fFeetPerGalBJG)

    # Calls the function for calculating the amount of work hours 
    fLaborHoursBJG = getLaborHours(fLaborHrsPerGalBJG, iGallonsBJG)

    # Calls the function for calculating the cost of labor 
    fLaborCostBJG = getLaborCost(fLaborHoursBJG, fLaborChargeBJG)

    # Calls the function for calculating the cost of paint
    fPaintCostBJG = getPaintCost(iGallonsBJG, fPaintPriceBJG)

    # Calls the function for calculating the sales tax rate 
    fTaxRateBJGBJG = getSalesTaxBJG(sStateBJG)

    # Calaculates the subtotal cost of paint and labor
    fSubtotalBJG  = fPaintCostBJG + fLaborCostBJG

    # Calculates the tax amount on the total cost
    fTaxAmountBJG = fSubtotalBJG * fTaxRateBJGBJG

    # Calaculates the subtotal with the tax
    fTotalCostBJG = fSubtotalBJG + fTaxAmountBJG

    # Calls the function to display results to screen and write them to the output file
    showCostEstimate(sLastNameBJG, iGallonsBJG, fLaborHoursBJG, fPaintCostBJG,
                     fLaborCostBJG, fTaxAmountBJG, fTotalCostBJG)

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

# Function for calculating the integer for how many gallons needed
def getGallonsOfPaint(fWallSpaceBJG, fFeetPerGalBJG):
    iGallonsBJG = int(fWallSpaceBJG / fFeetPerGalBJG)

    # If there is any remainder from the above equation, adds another gallon
    if fWallSpaceBJG % fFeetPerGalBJG != 0:
        iGallonsBJG += 1

    return iGallonsBJG

# Function for calculating the amount of work hours 
def getLaborHours(fLaborHrsPerGalBJG, iTotalGallonsBJG):
    return fLaborHrsPerGalBJG * iTotalGallonsBJG

# Function for calculating the cost of labor
def getLaborCost(fLaborHoursBJG, fLaborChargeBJG):
    return fLaborHoursBJG * fLaborChargeBJG

# Function for calculating the cost of paint
def getPaintCost(iTotalGallonsBJG, fPaintPriceBJG):
    return iTotalGallonsBJG * fPaintPriceBJG

# Function for returning the state tax rate
def getSalesTaxBJG(sStateBJG):
# The upper() method could be use here to conform the passed string
# into caps, but that's in a future chapter
    if sStateBJG == "CT":
        fTaxRateBJG = 0.06
    elif sStateBJG == "MA":
        fTaxRateBJG = 0.0625
    elif sStateBJG == "ME":
        fTaxRateBJG = 0.085
    elif sStateBJG == "NH":
        fTaxRateBJG = 0.0  # Not an error, NH has no sales tax
    elif sStateBJG == "RI":
        fTaxRateBJG = 0.07
    elif sStateBJG == "VT":
        fTaxRateBJG = 0.06
    else:
        # Any state not in the list above gets a 0% rate
        fTaxRateBJG = 0.0
    return fTaxRateBJG

# Function to display results to screen and write them to the output file
def showCostEstimate(sLastNameBJG, iGallonsBJG, fLaborHoursBJG, fPaintCostBJG,
                     fLaborCostBJG, fTaxAmountBJG, fTotalCostBJG):
    # Build the output file name by joining the customer's last name with
    # the standardized suffix
    sFileNameBJG = sLastNameBJG + "_PaintJobOutput.txt"
    # Fstrings for the formatted results are added to variables so that they can
    # be displayed, and saved to text file in the same format
    sGallonsBJG = f"Gallons of paint: {iGallonsBJG}"
    sHoursBJG = f"Hours of labor: {fLaborHoursBJG:.1f}"
    sPaintCostBJG = f"Paint charges: ${fPaintCostBJG:,.2f}"
    sLaborCostBJG = f"Labor charges: ${fLaborCostBJG:,.2f}"
    sTaxBJG = f"Tax: ${fTaxAmountBJG:,.2f}"
    sTotalBJG = f"Total cost: ${fTotalCostBJG:,.2f}"
    # Displays all results to the screen
    print(sGallonsBJG)
    print(sHoursBJG)
    print(sPaintCostBJG)
    print(sLaborCostBJG)
    print(sTaxBJG)
    print(sTotalBJG)

    # Creates or opens a text file using the name built with the sFileNameBJG variable
    # The other variables are then written to the file line by line
    with open(sFileNameBJG, "w") as outFileBJG:
        outFileBJG.write(sGallonsBJG + "\n")
        outFileBJG.write(sHoursBJG + "\n")
        outFileBJG.write(sPaintCostBJG + "\n")
        outFileBJG.write(sLaborCostBJG + "\n")
        outFileBJG.write(sTaxBJG + "\n")
        outFileBJG.write(sTotalBJG + "\n")

    # Displays that the text file was created, with the correct file name
    print(f"File: {sFileNameBJG} was created.")

if __name__ == '__main__':
    main()