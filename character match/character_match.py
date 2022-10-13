
# Part 1
def is_character_match(string1, string2):
	string1=string1.lower()
	string2=string2.lower()
	dict1={}
	dict2={}
	for x in string1:
		if dict1.get(x):
			dict1[x]+=1
		else:
			dict1[x]=1
	for x in string2:
		if dict2.get(x):
			dict2[x]+=1
		else:
			dict2[x]=1
	
	for key in dict1:
		if key==" ":
			continue
		if dict2.get(key):
			if dict2[key]==dict1[key]:
				continue
			else:
				return False
		else:
	   		return False
	print(string1, string2, dict1, dict2)
	return True






# Part 2
def anagrams_for(words, list_of_words):
	word=words.lower()
	dict1={}
	answer_list=[]
	for x in word:
		if dict1.get(x):
			dict1[x]+=1
		else:
			dict1[x]=1
	for checkedword in list_of_words:
		loop_broken=False
		string2=checkedword.lower()
		dict2={}
		# print(checkedword)
		for x in string2:
			if dict2.get(x):
				dict2[x]+=1
			else:
				dict2[x]=1
		# print(dict2, dict1)
		for key in dict1:
			if key==" ":
				continue
			if dict2.get(key):
				if dict2[key]!=dict1[key]:
					loop_broken=True
					break
			else:
				loop_broken=True
				break
			# print("gothere")
		if loop_broken==False:
			answer_list.append(checkedword)
	return answer_list