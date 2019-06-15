import re
regex = re.compile('[^a-zA-Z]')
letters    = 'abcdefghijklmnopqrstuvwxyz'
dic={}

def possible_edit1(word):
	deletes=[]
	for i in range(len(word)):
		deletes.append(word[:i]+word[i+1:])

	transposes=[]
	for i in range(len(word)-1):
		transposes.append(word[:i]+word[i+1]+word[i]+word[i+2:])

	replaces=[]
	for i in range(len(word)):
		for j in letters:
			replaces.append(word[:i]+j+word[i+1:])

	inserts=[]
	for i in range(len(word)+1):
		for j in letters:
			inserts.append(word[:i]+j+word[i:])
	return(deletes+transposes+replaces+inserts)


wordList=[]
file=open("big.txt","r")
for line in file:
	for word in line.split():
		word=regex.sub("",word)
		wordList.append(word.lower())

def correction(word):
	word=word.lower()
	if word in wordList:
		print("correct word")
		return
	possibles=possible_edit1(word)
	set_possibles=set(w for w in possibles if w in wordList)
	if(len(set_possibles)==0):
		possibles2=possibles
		for i in possibles:
			temp=possible_edit1(i)
			possibles2=possibles2+temp
		set_possibles=set(w for w in possibles2 if w in wordList)
	if(len(set_possibles)==0):
		print("no suggestion found")
		return
	m=0
	out=""
	for i in set_possibles:
    		if dic[i]>m:
        		out=i
        		m=dic[i]
	print(out)
for i in wordList:
	if i not in dic:
		dic[i]=1
	else:
		dic[i]+=1
wordList=set(wordList)
word=input("enter the word")
correction(word)