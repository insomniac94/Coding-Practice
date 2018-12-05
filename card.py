import re

# What kind of card is it?

# Visa - starts with a 4 (up to 19 digits)

# Mastercard - (16 digits) First digit must be 5 and second digit must be in the range 1 through 5 inclusive. The range is 510000 through 559999
#              First digit must be 2 and second digit must be in the range 2 through 7 inclusive. The range is 222100 through 272099

# Discover - (16 digits) First 6 digits must be in one of the following ranges: 601100 through 601109, 601120 through 601149, 601174, 601177 through 601179, 
#            601186 through 601199, or 644000 through 659999 

cardNumberInput = input("Enter a card number: ")
regEx = r'\d{1}'
pattern = re.compile(regEx)
matches = pattern.findall(cardNumberInput)

count = 0
for match in matches:
    count +=1
    if count <= 4:
        print(match)

if(matches[0] == '4'):
    print("Visa Card! Card number: ", end="")
    for match in matches:
        print(match, end="")