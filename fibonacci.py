def fibonacci(num):
  list=[0, 1]
  counter=0
  while counter!=num:
    newNum=list[0]+list[1]
    list.insert(0, newNum)
    list.pop()
    counter=counter+1
  return list[0]


