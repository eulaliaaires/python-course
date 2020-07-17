
def smallestF(numbers, smallest):
    for num in numbers:
        if smallest is None:
            smallest = num
        elif num < smallest:
            smallest = num
    return int(smallest)

def largestF(numbers, largest):
    for num in numbers:
        if largest is None:
            largest = num
        elif num > largest:
            largest = num
    return int(largest)

largest = None
smallest = None
numbers = []

while True:
    number = input("Enter a number: ")
    if number == "done" :
        break
    try:
        num = float(number)
    except:
        print('Invalid input')
        continue
    numbers.append(num)

print("Maximum is", largestF(numbers, largest))
print("Minimum is", smallestF(numbers, smallest))
