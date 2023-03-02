#1. Write a function to print symbols in reverse fashion
def print_symbol(num, symbol):
    for i in range(num, 0, -1):
        print(symbol * i)
print_symbol(11, '*')

# 2.  Modify print_symbol function to not print anything if symbol is "-"
def print_symbol(num, symbol):
    # Check if the symbol is "-"
    if symbol == "-":
        return
    
    # Loop through the range in reverse order using a negative step
    for i in range(num, 0, -1):
        print(symbol * i)

print_symbol(11, '-')

# Modify print_symbol fuction to not print anything greater than 1 character in length Ex - print_symbol(11, 'aa') will not work

def print_symbol(num, symbol):
    # Check if the length of the symbol is greater than 1
    if len(symbol) > 1:
        return
    
    # Loop through the range in reverse order using a negative step
    for i in range(num, 0, -1):
        print(symbol * i)

print_symbol(11, 'aa')

# 4. Write a function which will check if a given number is within a given range.
# Ex: is_in_range(number, start, end) will return True if number is in range, False if number is not in range.

def is_in_range(number, start, end):
    if start <= number <= end:
        return True
    else:
        return False

# Test cases
print(is_in_range(12, 0, 36)) 
print(is_in_range(12, 12, 36))  
print(is_in_range(120, 0, 36))

# 5. Write a function which takes numbers till user input,

# if number is divisible by 3, print "Three"

# if number is divisible by 5, print "Five"

## if number is divisible by both 5 and 3, print "Three and Five"

# else, print the number.

def print_numbers():
    while True:
        num = input("Enter a number (or 'q' to quit): ")
        if num == 'q':
            break
        
        try:
            num = int(num)
        except ValueError:
            print("Invalid input, please enter a number or 'q' to quit.")
            continue
        
        if num % 3 == 0 and num % 5 == 0:
            print("Three and Five")
        elif num % 3 == 0:
            print("Three")
        elif num % 5 == 0:
            print("Five")
        else:
            print(num)
print_numbers()

# 6. Write a function which will check if a given number is outside a given range.
# Ex:is_out_of_range(number, start, end) will return True if number is out of range, False if number is withiin range.

# Test:   
# is_out_of_range(12, 0, 36) returns False  
# is_out_of_range(12, 12, 36) returns False  
# is_out_of_range(120, 0, 36) returns True.

def is_out_of_range(number, start, end):
   if number < start or number > end:
        return True
   else:
        return False

#Test
print(is_out_of_range(12, 0, 36)) 
print(is_out_of_range(12, 12, 36)) 
print(is_out_of_range(120, 0, 36))