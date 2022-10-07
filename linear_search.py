array_to_search_through = []
for number in range(1, 1001):
    array_to_search_through.append(number)

def linear_search(finder, list):
    index=-1
    for x in list:
        index=index+1
        if finder==x:
            return index
    return None
def linear_search_global(finder, list):
    index=-1
    new_list=[]
    for x in list:
        index=index+1
        if finder==x:
            new_list.append(index)
    return new_list
