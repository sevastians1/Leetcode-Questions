import functools
def credit_check(string):
    new_list=[]
    odd=True
    for x in string:
        if odd==True:
            # print("-----")
            double=int(x)*2
            # print(double)
            if double>=10:
                sum=0
                for y in str(double):
                    sum+=int(y)
                new_list.append(str(sum))
                # print(sum)
            else: 
                new_list.append(double)
        else:
            new_list.append(x)
        odd=not odd
    modulo_total=functools.reduce(lambda x, y:int(x)+int(y), new_list)
    # print(new_list, modulo_total)
    if modulo_total%10==0:
        return "The number is valid!"
    else:
        return "The number is invalid!"
# print(credit_check('5541808923795240'))
# Your Luhn Algorithm Here
# Expected Output:
# If it is valid, print "The number is valid!"
# If it is invalid, print "The number is invalid!"

