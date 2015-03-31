import re


def find_words(string_to_check):
		present=[] #array that contains the key words that are present
		count=0
		word_dict= ({'Title':['title','position','profile'],'Description':['description','detail','purpose'],'Based at':['based at','located'],'Duties/Responsibilities':['function','duties','responsibilities']
		,'Skills':['skills','qualifications'],'Experience':['experience','know-how'],'Education':['education','learning']
		,'Work-status':['contract','full-time']})

		for k,v in word_dict.iteritems():
			arr=v
			for i in arr:
				searchObj = re.search(i,string_to_check,flags=re.I | re.X | re.S)
				if searchObj!=None:
					count+=1
					present.append(k)
					break
		absent=[i for i in word_dict.keys() if i not in present]
		return count, absent

#count,absent=find_words('Description,\nEducation')
#print count, absent