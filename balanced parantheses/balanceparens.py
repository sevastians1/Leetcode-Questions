from hashlib import new


def balanceParens(string):
    tester=[[0,0]]
    new_string=[]
    dictionary={}
    for count, x in enumerate(string):
        dictionary[count]=x
        # print(tester, x)
        if x =="(":
            tester.insert(0, [x, count])
        elif x==")" and tester[0][0]=="(":
            # print(tester[0], "help here")
            dictionary[tester[0][1]]=True
            dictionary[count]=True 
            del tester[0]
        elif x =="[":
             tester.insert(0, [x, count])
        elif x=="]" and tester[0][0]=="[":
             del tester[0]
             new_string.append("[]")
        elif x =="{":
             tester.insert(0, [x, count])
        elif x=="}" and tester[0][0]=="{":
             del tester[0]
             new_string.append("{}")
        elif x=="}"or x=="]" or x==")":
             continue
        else:
            dictionary[count]=True


    for count, x in enumerate(string):
        if dictionary[count]==True:
            new_string.append(x)
    return "".join(new_string)
print(balanceParens(")[((a))(")) # should return "(())"




print(balanceParens("()")) # should return "()"
print(balanceParens("a(b)c)")) # should return "a(b)c"
print(balanceParens("(a)(bdd)c)")) # should return "(a)(bdd)c"
print(balanceParens("a(dbvb)c)")) # should return "a(dbvb)c"
print(balanceParens("a(b)(c)())")) # should return "a(b)(c)()"
print(balanceParens(")(")) # should return ""
print(balanceParens("(((((")) # should return ""

print(balanceParens("(()()(")) # should return "()()"
print(balanceParens(")())(()()(")) # should return "()()()"