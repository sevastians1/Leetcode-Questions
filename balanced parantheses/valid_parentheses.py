from operator import truediv


def isValid(s):
    arr=[]
    para=[]
    square=[]
    curly=[]
    for x in s:
        arr.append(x)
        # if obj.get(x):
        #     obj[x]+=1
        # else:
        #     obj[x]=1
    try: 
        for count, x in enumerate(arr):
            if x=="(":
                para.append(count)
            elif x=="[":
                square.append(count)
            elif x=="{":
                curly.append(count)
            elif x==")":
                if count>para[len(para)-1]:
                    del para[len(para)-1]
            elif x=="]":
                if count>square[len(square)-1]:
                    del square[len(square)-1]
            elif x=="}":
                if count>curly[len(curly)-1]:
                    del curly[len(curly)-1]
        print(para, square, curly)
        if para ==[] and square == [] and curly ==[]:
            return True
        return False
    except:
        return False
print(isValid("()[]{}"))
string="{[((}))]"

