# Name: Brian Gallagher
# Assignment:   Temp Converter
# Reflection:   I liked figuring out the flow of nested if-else statements.
#               
#               I struggled with using logical operators at first, until I
#               realized I couldn't group the possible values I wanted, I had
#               to do them individually. i.e. sTempScaleBJG == 'F' or 'f' or 'C' or 'c':
#               
#               If-else works by taking a value and applying logic to produce one of two
#               two outcomes to execute. If-elif-else works like if-else, except it can
#               continue to apply logic in a linear fashion, to achieve iterative answers.
#               I went with nesting if-else statements, with the idea of short-circuit
#               evaluation if this program operated on a larger scale. Plus it's easier
#               for me to view it like a dailogue tree this way.
#               
#               How to think about planning if-else and if-elif-else trees.
#               How to properly apply logical operators.
#               Indenting properly for nested instructions.
#               
# Welcome message with name of program.
print("Brian G's Temp Converter:")

# Prompts user for the temperature to convert and assigns it to a variable.
fTempEnteredBJG = float(input('Enter a temperature: '))

# Prompts user for the temp scale and assigns it to a variable.
sTempScaleBJG = input('Is the temp F for Fahrenheit or C for Celsius? ')

# Checks if the entered value for temp scale is a valid entry.
if sTempScaleBJG == 'F' or sTempScaleBJG == 'f' or sTempScaleBJG == 'C' or sTempScaleBJG == 'c':
    if sTempScaleBJG == 'F' or sTempScaleBJG == 'f':  # Checks for Fahrenheit.
        if fTempEnteredBJG > 212:  # Checks if temp is too high.
            print('Temp can not be > 212')
        else:  # Converts temp to Celcius.
            print(f'The Celsius equivalent is: {(5/9)*(fTempEnteredBJG - 32):.1f}')
    else:  # If the check isn't Fahrenheit, assumes Celcius.
        if fTempEnteredBJG > 100:  # Checks if temp is too high.
            print('Temp can not be > 100')
        else:  # Converts temp to Fahrenheit.
            print(f'The Fahrenheit equivalent is: {((9/5)*fTempEnteredBJG) + 32:.1f}')
else:  # If temp scale isn't valid, produces error message and ends program.
    print('Enter a F or C')