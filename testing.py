# from datetime import datetime

# def AddOne(num):
# 	return num + 1

# def MultiplyByTwo(num):
# 	return num * 2

# # This function accepts a function as input, then returns a new function that behaves similarly to the one that is passed in
# def PrintCurrentTimeAndAlso(func):

# 	# this function accepts any number of positional arguments (*args) and any number of named arguments (**kwargs)
# 	def WrapperFunction(*args, **kwargs):
# 		print(f'Calling {func.__name__} at {datetime.now()}')
# 		return func(*args, **kwargs)

# 	return WrapperFunction

# # This creates a new, decorated function
# PrintCurrentTimeAndAlsoAddOne = PrintCurrentTimeAndAlso(AddOne)
# one_plus_one = PrintCurrentTimeAndAlsoAddOne(1)
# print(one_plus_one)
# PrintCurrentTimeAndAlsoMultiplyByTwo=PrintCurrentTimeAndAlso(MultiplyByTwo)
# Five_Times_Two=PrintCurrentTimeAndAlsoMultiplyByTwo(5)
# print(Five_Times_Two)
# import math
# class Pizza:
#         def __init__(self, radius, ingredients):
#             self.radius=radius
#             self.ingredients=ingredients
#         def pizza_amount(self):
#             return self.radius **2 *math.pi
#         def circle_area(r):
#             return r **2 *math.pi
# my_slice=Pizza(4, "pepperoni")
# print(my_slice.pizza_amount)
# class ContactList:
#     def __init__(self, name, list_of_objects):
#         self.name=name
#         self.list_of_objects=list_of_objects

#     def __str__(self):
#         for each in self.list_of_objects:
#             print(each)
#             return self.name
# lis=[]
# friends = [{'name':'Alice','number':'867-5309'},{'name':'Zeek', 'number':'444-5555'}, {'name':'Bob', 'number':'555-5555'}]
# work_buddies = [{'name':'Alice','number':'867-5309'},{'name':'Carlos', 'number':'555-5555'}]
# for x in friends:
#     print(x,"---")
#     for y in work_buddies:
#         print(y, "+++++")
#         if x==y:
#             lis.append("did something")
# print(lis)






# my_friends_list = ContactList('My Friends', friends)
# my_work_buddies = ContactList('Work Buddies', work_buddies)
# def get_key(x):
#     return x['name']
# def sort(input):
#     var=input.sort(key=get_key)
#     return var
# # print(friends.sort(key=get_key))

# def myFunc(e):
#   return e['car']

# cars = [
#   {'car': 'Ford', 'year': 2005},
#   {'car': 'Mitsubishi', 'year': 2000},
#   {'car': 'BMW', 'year': 2019},
#   {'car': 'VW', 'year': 2011}
# ]

# cars.sort(key=myFunc)
# print(cars)

# class Person:
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age
#         print("super")
#     def print(self):
#         print("superduper")


# class Student(Person):
#     def __init__(self, name, age):
#         super().__init__(name, age)
#     var=super().print()
# Billy=Student("billy", 16)
#
list=[['H', 'O', 'O', 'U'], ['S', 'T', 'W', 'Y'], ['F', 'I', 'W', 'U'], ['X', 'J', 'Z', 'Y']]
if False:
    if list[0][4]:
        print("urmmom")
print(list[0][4])
# letter_to_check="W"
# list_of_first_letter=[[1, 2],[2, 2]]
# print(list[0][2])
# def check_if_valid_location(row, index):
#     if row<0:
#         return False
#     elif row>4:
#         return False
#     elif index<0:
#         return False
#     elif index>4:
#         return False
#     else:
#         return True
# def check_row_and_index(row, index, letter_to_check):
#     if check_if_valid_location(row, index) and letter_to_check==list[row][index]:
#       return [row, index]
# def return_next_letter_locations(location_of_letter, letter_to_check):
#     new_locations=[]
#     while(len(location_of_letter)>1):
#         row=location_of_letter[0][0]
#         index=location_of_letter[0][1]
#         row1=row-1
#         row2=row
#         row3=row+1
#         index1=index-1
#         index2=index
#         index3=index+1
#         check_row_and_index(row1, index1, letter_to_check)
#         check_row_and_index(row1, index2, letter_to_check)
#         check_row_and_index(row1, index3, letter_to_check)

#         check_row_and_index(row2, index1, letter_to_check)
#         check_row_and_index(row2, index3, letter_to_check)

#         check_row_and_index(row3, index1, letter_to_check)
#         check_row_and_index(row3, index2, letter_to_check)
#         check_row_and_index(row3, index3, letter_to_check)
#         location_of_letter=location_of_letter[1:]
#     return new_locations
# print(check_if_valid_location(-1, list_of_first_letter[0][1]))
# print(check_row_and_index(-1, list_of_first_letter[0][1], letter_to_check))
# # test=[1, 2, 3]
# # test=test[1:]
# # test=test[1:]
# # test=test[1:]
# # print(len(test))
# print(return_next_letter_locations([[1, 2],[3, 2]], "O"))
# # print(check_row_and_index(1, 2, "O"))

