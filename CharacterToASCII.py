# Program to Convert given character into its ASCII value

# importing numpy python library
import numpy as np

# Creating charToInt function
def charToInt(char) :
    return ord(char) # ord() returns the ASCII value of any character

# Creating a numpy array named X
# array of characters
X = np.array(['A', 'B', 'C', 'D', 'E'])

# Iterating and converting characters to corresponding ASCII value
for i in X :
    print(charToInt(i))