def calculate_mode(lists):
    dictionary={}
    answer=[]
    for x in lists:
        if dictionary.get(x):
            dictionary[x]+=1
        else:
            dictionary[x]=1
    compare_list=[0]
    for x in dictionary:
        if dictionary[x]>compare_list[0]:
            compare_list[0]=dictionary[x]

    # print(compare_list)        
    for x in dictionary:
        if dictionary[x]==compare_list[0]:
            answer.append(x)
    # print(dictionary)
    return answer

    # => [3]
# calculate_mode([4.5, 0, 0])       # => [0]
# calculate_mode([1.5, -1, 1, 1.5]) # => [1.5]
# calculate_mode([1,1,2,2])         # => [1,2]
# calculate_mode([1,2,3])           # => [1,2,3], because all occur with equal frequency
# calculate_mode(["who", "what", "where", "who"]) # => ["who"]
# Remember to write tests!

