# What is python ?
    1. Python is a high level interpriter programing language.
    2. Python supports OOP.
    3. Python language used in many areas for developing web applications, automate webapplications with selenium ,
    Machine Learning, Automation, IOT, Network Programming, Text processing and Multimedia.

# Advantages of python ?
    1. Python is easy to learn and use
    2. Python syntax is easy to use and Simple.
    3. Python supports OOP, modules and packages.
    4. It is a Interpreted language
    5. Compatible with Major Platforms
    6. Python has Extensive Support Libraries like(panda, numpy, matplotlib) and frameworks(django, flask, bottle and Robot Framework)
    7. Python is a open source.

# Dis Advanatges in python ?
    1. Python runs only on single core.
    2. It is not suitable for mobile applications.
    3. Speed: Python is slower than C or C++. But of course, Python is a high-level language, unlike C or C++ it's not closer to hardware.

# Which python version you are using ?
    1. i am using python 3.6.8 version

# Write a pattern for match ip address ?
ip = '1.200.33.25'
r = re.search(r'^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$', ip)
print(r)

# Write a pattern for match email address ?
email = 'sriram.instinfo@gmail.com'
r  = re.search('[a-zA-Z0-9.]+@[A-Za-z]+\.(com|in)',email)
print(r)

# Find Max and Min values without inbult finctions ?
l = [3,4,5,6,2,1]
fv = l[0]
for i in l:
    if fv < i:
       fv = i
print(' Max value is :', fv)

for i in l:
    if fv > i:
       fv = i
print(' Min value is :', fv)

# Remove duplicate values from list
l = [1,2,3,3,5,5]
NL =[]
for i in l:
    if i not in NL:
        NL.append(i)
print(NL)

# Convert two lists into one dictionary
l = [1,2,3,4]
ll = ['sri','ram','kumar','naidu']
d = dict(zip(l,ll))
print(d)

# Convert list into dictionary
a = ['name','anjan','age',28,'proper','tdp']
b = {}
for i in range(0,len(a),2):
    b[a[i]] = a[i+1]
print(b)

# Minssing number in list
l = [1,2,3,5,6,7]
for i in range(max(l)):
    if i not in l:
        print(i)

# How to Reverse a string 
s = 'sriram'
## 1 with slicing
print(s[::-1]
## 2 With for loop
l = []
for i in s:
    l.insert(0,i)
s = ''.join(l)
print(s)


# How to reverse words in string 
s = "How are you Balu"
ms = ''
for i in s.split():
    ms += ' ' + i[::-1]
print(ms)

# How to reverse word characters in a string?
A = "Hi how are you "
##  Output is : iH woh era uoy 
for word in A.split():
    print (word[::-1])

# How Get Charecter count in string ?
s = 'sriram kumar'
print({i:s.count(i) for i in set(s)})

# How do you know given string is Palindrome or not ?
'''A palindrome is a word, number, phrase, or other sequence of characters which reads the same backward as forward, such as madam or racecar or the number 10801.'''
v = 'sas'
if v == v[::-1]:
    print(v, ' is a palindrome ')
else:
    print(v, ' is not a palindrome ')


# Sort a list without sort function
l = [2,4,3,55,6,7]
ll= []
for i in range(len(l)):
    m = min(l)
    ll.append(m)
    l.remove(m)
print(ll)

# get Prime number with list comprihence
print([i for i in range(0,10) if i > 1 if 0 not in[i%j for j in range(2,i)]])

# Get Prime number with for loop
for i in range(0,10):
    if i > 1:
        if all(i%j != 0 for j in range(2,i)):
            print ' prime number with for loop :', i

# Write a Fibanacci program ?
def fib(n) :
   a,b = 0,1
   for _ in range(n) :
     yield a
     a,b = b,a+b
print(list(fib(10)))

# Write a Factorial Program ?
def fact(n):
  f = 1
  for i in range(1, n +1):
   f = f * i
  return f
print fact(5)




