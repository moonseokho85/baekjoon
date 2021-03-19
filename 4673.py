# Function of finding self number
def d(n):

    # Stringify the number
    string_n = str(n)

    # Finding the sum of each digit
    sum_of_each_digit = 0
    for i in range(len(string_n)):
        sum_of_each_digit += int(string_n[i])

    self_number = int(n) + sum_of_each_digit
    return self_number


# Making list of numbers
numbers = list()
for i in range(10000):
    numbers.append(i + 1)

# Making list of self numbers
self_numbers = list()
for i in numbers:
    self_number = d(i)
    self_numbers.append(self_number)

# Removing the difference between numbers and self numbers
for i in set(self_numbers):
    try:
        numbers.remove(i)
    except:
        pass

# Printing the numbers
for i in numbers:
    print(i)
