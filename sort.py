string =  input("Please enter a message:")
list = list(string)
list.sort(reverse=True)
for letter in enumerate(list):
    print(letter[1], end="")