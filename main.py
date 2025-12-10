num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
sum_result = num1 + num2
print(f"The sum of {num1} and {num2} is {sum_result}.")

import numpy as np 

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
array_sum = np.add(array1, array2)
print(f"The sum of {array1} and {array2} is {array_sum}.")

def add_numbers(a, b):
    return a + b
result = add_numbers(10, 20)
print(f"The sum of 10 and 20 is {result}.")