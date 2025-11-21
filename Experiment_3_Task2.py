# Define a function list_summary that accepts a list of integers.
# Return the sum, average, and maximum value of the list as a tuple.
# Test the function with a sample list.

def list_summary (l):
    total = sum(l)
    avg = total / len(l) if l else 0  # handle empty list
    maximum = max(l) if l else None
    return (total, avg, maximum)

# Test the function
print("1.Total\n2.Average\n3.Maximum")
print('-'*40)
sample_list = [1, 2, 3, 4, 5]
print(list_summary(sample_list))  # Output: (15, 3.0, 5)

print('-'*40)
l=[3,4,5,6,7,8,9]
print(list_summary(l))
print('-'*40)
