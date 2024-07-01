import math

operations = ["Addition", "Subtraction", "Multiplication", "Division"]


while True:
    choice = (input("What operation do you want to choose? (Addition, Subtraction, Multiplication, Division) ")).capitalize()

    if choice in operations:
        break
    else:
        print("Invalid operation choice")
        continue
        

number = int(input("How many numbers are you operating with? " ))


nums_they_working_with = []

for nums in range (number):
    x = float(input(f"Enter number {nums + 1} "))
    nums_they_working_with.append(x)


def addition():
    result = sum(nums_they_working_with)
    print(result)


def multiplication():
    result = math.prod(nums_they_working_with)
    print(result)

def division():
    result = nums_they_working_with[0]
    for num in nums_they_working_with[1:]:
        if num == 0:
            print("Division by 0 is not allowed ")
            return
        result /= num
    print(result)


def subtraction():
    result = nums_they_working_with[0]
    for num in nums_they_working_with[1:]:
        result -= num
    print(result)



if choice == "Addition":
    addition()
elif choice == "Subtraction":
    subtraction()
elif choice == "Multiplication":
    multiplication()
elif choice == "Division":
    division()
