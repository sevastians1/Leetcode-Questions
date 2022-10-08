#REMEMBER TO PSEUDOCODE
def pad(array, min_size, value=None):
    while len(array)<min_size:
        array.append(value)
    return array
print(pad ([1,2,3, 4, 6, 7], 5, "apple"))
