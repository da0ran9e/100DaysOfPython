## 'read()' usage
#f = open('sample.txt', 'r')
#s = f.read()
#print(s)
#f.close()
## note: file I/O handles date as string 
##       'txt' filesprocess data as text only, no other formats


## wite multiple lines to a file
#L = ['hello\n', 'hi\n', 'how are you\n', 'im fine']

#f= open('sample.txt', 'w')
#f.writelines(L) #efficiently writemultiple lines
#f.close()