Car = input("Enter the car colour: ")
Array = []

while Car != "":
    Array.append(Car)
    Car = input("Enter the car colour: ")

dictionary = {}
for i in Array:
    if i in dictionary:
        dictionary[i] = dictionary[i] + 1
    else:
        dictionary[i] = 1

for i in dictionary:
    print(f"cars that are {i}: {dictionary[i]}")
            