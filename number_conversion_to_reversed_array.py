''' Convert a number into a reversed array of digits
Given a random non-negative number, you have to return the digits of this number within an
array in reverse order.
Ex:
0 => [0]
3452 => [2,5,4,3]'''

def reverse_array_of_digits(num):
    return [int(digit) for digit in str(num)[::-1]]


num1 = 0
num2 = 3452
print(reverse_array_of_digits(num1))  
print(reverse_array_of_digits(num2))  




