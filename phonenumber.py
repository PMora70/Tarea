phone =  input("Phone number: ")
digits_mapping = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four"
}
output = ''
for characters in phone:
    output += digits_mapping.get(characters, "!") + " "
print(output)