def sum_pairs(lists, sum):
    answer_list=[]
    dictionary={}
    for x in lists:
        dictionary[x]=x
    print(dictionary)
    for key in dictionary:
        one_value=dictionary[key]
        print(one_value)
        for secondkey in dictionary:
            if key==secondkey:
                continue
            if isinstance(dictionary[key], str)or isinstance(dictionary[secondkey], str):
                continue
            elif dictionary[key]+dictionary[secondkey]==sum:
                answer_list.append([key, secondkey])
                dictionary[key]="used"
                dictionary[secondkey]="used"
            print(dictionary)
    if answer_list==[]:
        return 'unable to find pairs'  
    print(answer_list)          
    return answer_list









# sum_pairs([1,2,3,4,5], 9)
# sum_pairs([1,2,3,4,5], 7)
# sum_pairs([3, 1, 5, 8, 2], 27)

# Before writing your code, don't forget to write your tests!!

# Write a method that takes an integer array and a desired sum. The output will be pairs of numbers from the inputed integer array that equal that desired sum. If there are no pairs that work, return 'unable to find pairs'

# Sample output:

# sum_pairs([1,2,3,4,5], 9) # [[4,5]]
# sum_pairs([1,2,3,4,5], 7) # [[2,5], [3,4]]
# sum_pairs([3, 1, 5, 8, 2], 27) # 'unable to find pairs'