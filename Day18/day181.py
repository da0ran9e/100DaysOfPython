 #'read()' usage
f = open('sample.txt', 'r')
s = f.read()
print(s)
f.close()
## note: file I/O handles date as string 
##       'txt' filesprocess data as text only, no other formats