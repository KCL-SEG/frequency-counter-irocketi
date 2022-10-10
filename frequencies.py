"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}

    # converting all list elements to string
    for i in range(0, len(items)):
        items[i] = str(items[i])

    # extracting unique values
    uniqueItems = set(items)

    print("unique list: " + str(uniqueItems))
    for x in uniqueItems:
        count = items.count(x)
        frequencies.update({x:count})

    return frequencies