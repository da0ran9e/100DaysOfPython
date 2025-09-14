#problem with 'w' mode->>>overwrite file  content
#to preserves existing content, use 'a' mode
f= open('sample.txt', 'a')
f.write('\nI am fine')
f.close()