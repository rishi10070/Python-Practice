# Get user input
temp = int(input("Temperature: "))
rain = input("Will it rain (yes/no): ")

# Always printed
print("Wear jeans and a T-shirt")

# Temperature recommendations
if temp <= 20:
    print("I recommend a jumper as well")

if temp <= 10:
    print("Take a jacket with you")

if temp <= 5:
    print("Make it a warm coat, actually")

if temp <= 3:
    print("I think gloves are in order")

# Rain recommendation
if rain == "yes":
    print("Don't forget your umbrella!")