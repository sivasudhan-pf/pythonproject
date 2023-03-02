'''List of lists
You have a two-dimensional list in the following format:
data = [[2, 5], [3, 4], [8, 7]]
Each sub-list contains two items, and each item in the sub-lists is an integer.
Write a function process_data()/processData() that processes each sub-list like so:
[2, 5] --> 2 - 5 --> -3
[3, 4] --> 3 - 4 --> -1
[8, 7] --> 8 - 7 --> 1
and then returns the product of all the processed sub-lists: -3 * -1 * 1 --> 3.
For input, you can trust that neither the main list nor the sublists will be empty.'''

def process_data(data):
    processed_data = [sublist[0] - sublist[1] for sublist in data]
    product = 1
    for num in processed_data:
        product *= num
    return product

data = [[2, 5], [3, 4], [8, 7]]
result = process_data(data)
print(result) 