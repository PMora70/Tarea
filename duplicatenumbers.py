numbers = [5, 2 , 7 , 2, 5, 1 ,4]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
