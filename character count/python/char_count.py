import functools
def char_count(str):
  txt= str.replace(" ", "")
  dictionary={}
  for x in txt:
    if dictionary.get(x):
      dictionary[x]+=1
    else:
      dictionary[x]=1
  answer=[]

  for x in dictionary:
    values=[x, dictionary[x]]
    answer.append(values)
  # def myFunc(x):
  #   return x[1]
  answer.sort(key=lambda x: x[1], reverse=True)
  print(answer)
  return answer
  

print(char_count("aa abbc"))
  # Your code here