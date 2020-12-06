
heads = float(input("How many heads: "))
legs = float(input("How many legs: "))

if legs % 2 != 0:
    print("Please enter an even value for legs.")
    exit(0)

if (heads * 2 <= legs and heads * 4 >= legs) == False:
    print("Please check the values for legs.")
    exit(0)

rabbits = legs / 2 - heads
chickens = heads - rabbits

print(f"Number of chickens is {int(chickens)}")
print(f"Number of rabbits is {int(rabbits)}")
