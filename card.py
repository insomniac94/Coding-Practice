import re

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