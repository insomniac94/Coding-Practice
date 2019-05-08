import re

cardNumber = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

if cardNumber[0] == 4:
elif cardNumber[1] == 5:
    print("test")

cardNumberInput = input("Enter a card number: ")
regEx = r'\d{1}'
pattern = re.compile(regEx)
matches = pattern.findall(cardNumberInput)

count = 0
for match in matches:
    count +=1
    if count <= 4:
        print(match)

if matches[0] == '4':
    print("This is a Visa Card with the card number: ", end="")
    for match in matches:
        print(match, end="")
else: 
    print("Not a Visa Card.")
