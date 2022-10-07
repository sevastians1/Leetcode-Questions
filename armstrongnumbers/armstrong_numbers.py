# How can you make this more scalable and reusable later?
import math
import functools

def find_armstrong_numbers(numbers):
    answer_list = []

    for n in numbers:

        one_num = str(n)

        # 
        num_list = []
        for x in one_num:
            num_list.append(int(x))


        #
        num_list[0] = math.pow(num_list[0],len(num_list))
        armstrong = int(functools.reduce(lambda a, b:  math.pow(b,len(num_list)) + a,num_list))

        if armstrong == int(one_num):
            answer_list.append(armstrong)
    
    return answer_list
# import MATH




