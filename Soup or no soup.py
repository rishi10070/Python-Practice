name=str(input("Please tell me your name:"))
if name == "Jerry":
    print("Next please!")
else:
    portions=int(input("How many portions of soup?"))
    cost=5.90* int(portions)
    print(f"The total cost is {cost}")
    print( "Next please!")
