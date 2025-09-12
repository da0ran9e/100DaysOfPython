# Ngày 1: Hàm `print`
```python
print("Hello World")

print(6)

print(5.6)

print(False)

print("India", "Pakistan", "Nepal", "Srilanka")

print("India", 5, True)

print("India", "Pakistan", "Nepal", "Srilanka", sep='/')

print("India", "Pakistan", "Nepal", "Srilanka", sep='-')

print("Hello")
print("World")

print("Hello", end=' ')
print("World")

print("Hello\nWorld")  # xuống dòng
print("Hello\tWorld")  # tab
print("She said: \"Python is fun!\"")

print("""This is
a multi-line
string""")

name = "An"
age = 22
print("My name is %s and I am %d years old" % (name, age))  # style cũ
print("My name is {} and I am {} years old".format(name, age))  # style mới
print(f"My name is {name} and I am {age} years old")  # f-string (hiện đại)


print(5 + 3)
print("Sum of 5 and 3 is", 5 + 3)
```