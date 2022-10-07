exitParameter=False
goodbyeChecker= False
def function(value):
  global exitParameter
  global goodbyeChecker
  newList= list(value)
  lowerCaseChecker= False
  for x in newList:
    if (x.islower()):
      lowerCaseChecker=True
  if lowerCaseChecker == True:
        print("SPEAK UP, KID!")
  elif value=="": 
        print("WHAT?!")
  elif lowerCaseChecker == False and value != "GOODBYE!": 
        print("NO, NOT SINCE 1946!")
  if value=="GOODBYE!" and goodbyeChecker==False: 
        print("LEAVING SO SOON?")
        goodbyeChecker =True
  elif value== "GOODBYE!" and goodbyeChecker==True: 
        print("LATER, SKATER!") 
        exitParameter=True
  if exitParameter==True:
    return
  else:
    value=input()
    function(value)
  
value= input("HELLO KID\n")
function(value)

