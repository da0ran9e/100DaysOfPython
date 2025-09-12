a = 0b1010
b = 100 
c = 0o332
d = 0x849c
#float
f1 = 0.1
f2 = 1.5e2
f3 = 1.5e-3
#complex
x = 3.14j
print(a, b, c, d)
print(f1, f2, f3)
print(x, x.imag, x.real)




unicode = u"\U0001f600\U0001F606\U0001F823"
raw_str = r"raw \n string"
print(unicode)
print(raw_str)


a = True + 4  # True == 1
b = False + 10   # False  == 0
print ("a:", a)
print ("b:", b)