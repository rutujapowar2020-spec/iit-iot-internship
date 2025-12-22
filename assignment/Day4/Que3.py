
"""Define a function overlapping() that takes two lists and returns True if they have at least one member in
common, False otherwise"""


def overlapping(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False

print(overlapping([1, 2, 3], [4, 5, 3]))
print(overlapping([1, 2], [4, 5]))
