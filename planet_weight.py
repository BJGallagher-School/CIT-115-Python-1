# Name: Brian Gallagher
# Assignment:   Planetary Weights
# Reflection:   I liked the balance between the information that was given for
#               the assignment, and having to figure things out myself.
#               
#               I struggled with trying to remember the different kinds output
#               formatting, and had to look them up directly in the book. 
#               
#               1. How to apply a data type to an input
#               2. How to combine output formatting and f strings
#               3. How to write a working script, this was my first real one
                
# These are the named constants for each planet, since they don't change
MERCURY = 0.38
VENUS = 0.91
MOON = 0.165
MARS = 0.38
JUPITER = 2.34
SATURN = 0.93
URANUS = 0.92
NEPTUNE = 1.12
PLUTO = 0.066

# Prompts user for their name and assigns to variable
sNameBJG = input('What is your name? ')

# Prompts user for their Earth weight and assigns to float variable
fWeightEnteredBJG = float(input('What is your Earth weight? '))

# Calculates user's weight with all planets,
# and outputs final results to user in easy to read format
print(sNameBJG + ", here are your weights on our Solar System's planets:")
print(f'Weight on Mercury:    {fWeightEnteredBJG * MERCURY:>10.2f}')
print(f'Weight on Venus:      {fWeightEnteredBJG * VENUS:>10.2f}')
print(f'Weight on Moon:       {fWeightEnteredBJG * MOON:>10.2f}')
print(f'Weight on Mars:       {fWeightEnteredBJG * MARS:>10.2f}')
print(f'Weight on Jupiter:    {fWeightEnteredBJG * JUPITER:>10.2f}')
print(f'Weight on Saturn:     {fWeightEnteredBJG * SATURN:>10.2f}')
print(f'Weight on Uranus:     {fWeightEnteredBJG * URANUS:>10.2f}')
print(f'Weight on Neptune:    {fWeightEnteredBJG * NEPTUNE:>10.2f}')
print(f'Weight on Pluto:      {fWeightEnteredBJG * PLUTO:>10.2f}')
