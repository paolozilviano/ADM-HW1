#################
#               #
#     PART 1    #
#               #
#################


### INTRODUCTION ###

# Ex 1 - Say "Hello, World!" With Python

if __name__ == '__main__':
    print("Hello, World!")
    
# Ex 2 - Python If-Else
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
if n>=1 and n<=100:
    if n%2 != 0 :
        print("Weird")
    if n%2 == 0 and n>=2 and n<=5 :
        print('Not Weird')
    if n%2 == 0 and n>=6 and n<=20 :
        print('Weird')
    if n%2 == 0 and n>20 :
        print('Not Weird')
    
# Ex 3 - Arithmetic Operators

if __name__ == '__main__':
    a = int(input())
    b = int(input())

print (a+b)
print(a-b)
print(a*b)

# Ex 4 - Python:

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    

print(a//b)
print(a/b)

# Ex 5 - Loops

if __name__ == '__main__':
    n = int(input())
for i in range(n):
    print (i**2)
    
# Ex 6 - Write a function

def is_leap(year):
    leap = False
    
    if year%4 == 0:
        if year%100==0:
            if year%400==0:
                leap = True
        else:
            leap = False
    else:
        leap = False
    
    return leap

year = int(input())
print(is_leap(year))

# Ex 7 - Print function

n = int(input())

a = ''
if n>=1 and n<=150:
    for i in range(n):
        if i !=0 :
            a = a + str(i)
        
print(a+ str(n))

### DATA TYPES ###

#Ex 1 - List Comprehensions

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
perm = []   
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if (i+j+k != n):
                perm.append([i,j,k])
                
print(perm)

#Ex 2 - Nested Lists

records = []

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
       

L =[]
for i in records:
    L.append(i[1])
    

for i in L:
    while(L.count(i)>1):
        L.remove(i)   


x = min(L)

for i in records:
    if i[1] == x:
        records.remove(i)
        
        

records.sort()
L.remove(x)        
y = min(L)
for i in records:
    if i[1] == y:
        print(i[0])
        
# Ex 3 - Find the Runner-up score!

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    a = list(arr)
    
for i in a:
    while(a.count(i)>1):
        a.remove(i)
        
x = max(a)
        
for i in a:
    if i == x:
        a.remove(i)
        
    
print(max(a))

# Ex 4 - Finding the percentage

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

x = 0

for i in student_marks[query_name]:
    x += i
    
mean = x/len(scores)
            
print(format(mean, '.2f'))

# Ex 5 - Tuples

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
a = (tuple(integer_list))
print(hash(a))

# Ex 6 - Lists

if __name__ == '__main__':
    N = int(input())
    l=[]
    for _ in range(N):
        inp=list(input().split())
        if "insert" in inp:
            l.insert(int(inp[1]),int(inp[2]))
        if "print" in inp:
            print(l)
        if "remove" in inp:
            l.remove(int(inp[1]))
        if "append" in inp:
            l.append(int(inp[1]))
        if "sort" in inp:
            l.sort()
        if "pop" in inp:
            l.pop()
        if "reverse" in inp:
            l.reverse()

###STRINGS###

# Ex 1 - sWAP cASE

def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

# Ex 2 - String Split and Join

def split_and_join(line):
    a = line.split(' ')
    b = '-'.join(a)
    return b

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
    
# Ex 3 - What's Your Name?

def print_full_name(first, last):
    return print('Hello ' + first + ' ' + last + '! You just delved into python.')

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
    
# Ex 4 - Mutations

def mutate_string(string, position, character):
    a = list(s)
    a[int(i)] = c
    b = ''.join(a)
    return b
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
    
# Ex 5 - String Validators


if __name__ == '__main__':
    s = input()
    
print (any(i.isalnum() for i in s))
print (any(i.isalpha() for i in s))
print (any(i.isdigit() for i in s))
print (any(i.islower() for i in s))
print (any(i.isupper() for i in s))

# Ex 6 - Text Wrap

import textwrap

def wrap(s,w):
    a = textwrap.wrap(s,w)
    b = ''
    for i in a:
        b += i + '\n'
    
    return b
            
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

# Ex 7 - String Formatting

def print_formatted(number):
    w = len(format(n, 'b'))
    for i in range(1, number+1): 
        print(str(i).rjust(w),
              format(i, 'o').rjust(w),
              format(i, 'X').upper().rjust(w),
              format(i, 'b').rjust(w))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

# Ex 8 - Capitalize!

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    for i in s.split():
        a=i
        i=i.capitalize()
        s=s.replace(a,i)

    return s
    

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
    
# Ex 9 - Find a string

def count_substring(string, sub_string):
    c = 0
    d = ''
    for i in range(len(string)):
        if i+(len(sub_string)-1) >= len(string):
            break
        for j in range(len(sub_string)):
            d += string[i+j]
        if d == sub_string:
            c +=1
        d = ''
    return c



if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
    
# Ex 10 - The minion Game

def minion_game(string):
    s = string.upper().strip()
    K = 'Kevin'
    S = 'Stuart'
    cs = 0
    ck = 0
    for i in range(len(s)):
        if s[i] in 'AEIOU':
            ck += len(s) - i
        else:
            cs += len(s) - i
    if ck > cs:
        print(K, ck)
    elif cs > ck:
        print(S, cs)
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)
    
# Ex 11 - Alphabet Rangoli

def print_rangoli(size):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    s = abc[:size]
    sp = (size*2)-2
    it = s[-1]
    l = []
    for i in range(n-1,-1,-1):
        v = sp * '-' + it + it[-2::-1] + sp * '-'
        print(v)
        l.append(v)
        sp = sp - 2
        it += '-' + s[i-1]
    
    for i in range(len(l)-2,-1,-1):
        print(l[i])
    
    
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
    
# Ex 12 - Designer Door Mat

def door(n,m):
    if n*3 != m:
        TypeError
    si = (m-3)//2
    wi = (m-7)//2
    it = '.|.'
    l = []
    W = 'WELCOME'
    for i in range((n-1)//2):
        v = si * '-' + it + si * '-'
        print(v)
        l.append(v)
        si = si - 3
        it += '.|..|.'
        i = i
    w = wi * '-' + W + wi * '-'
    print(w)
    for i in range(len(l)-1,-1,-1):
        print(l[i])
    
    
    
if __name__ == '__main__':   
    n,m = map(int,input().split())
    door(n,m)
    
# Ex 13 - Merge the Tools!

def merge_the_tools(string, k):
    
    if len(string) % k != 0:
        TypeError
    
    s = string.upper().strip()
    l = []

    for i in range(0, len(s), k):
        l.append(s[i:k+i])

    a = ''
    nl = []
    for i in l:
        for j in i:
            if j not in a:
                a += j
        nl.append(a)
        a = ''

    for i in nl:
        print(i)
    

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
    
# Ex 14 - Text Alignment

#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
    


### SETS ###
    
# Ex 1 - Introduction to sets

def average(array):
    s = set(arr)
    avg = sum(s)/len(s)
    return "{:.3f}".format(avg)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
    
# Ex 2 - No Idea!

if __name__ == '__main__':
    n,m = map(int,input().split())
    arr = list(map(int, input().split()))
    A = set(list(map(int, input().split())))
    B = set(list(map(int, input().split())))
    
    if len(arr) != n:
        raise TypeError
    if len(A) != m:
        raise TypeError
    if len(B) != m:
        raise TypeError
        
    c = 0
    for i in arr:
        if i in A:
            c += 1
        if i in B:
            c -= 1
    print(c)
    
# Ex 3 - Set.add()

n = int(input())
countries = []
for i in range(n):
    countries.insert(i, input())
s = set(countries)
print(len(s))

# Ex 4 - Symmetric Difference

M = int(input())
A = set(list(map(int, input().split())))
N = int(input())
B = set(list(map(int, input().split())))


l = []

a = A.difference(B)
b = B.difference(A)

for i in  a:
    l.append(i)
for i in b:
    l.append(i)
    
l.sort()

for i in l:
    print(i)
    
# Ex 5 - Set.union() Operation

n = int(input())
A = set(list(map(int, input().split())))
b = int(input())
B = set(list(map(int, input().split())))

U = A.union(B)
print(len(U))

# Ex 6 - Set.intersection() Operation


n = int(input())
A = set(list(map(int, input().split())))
b = int(input())
B = set(list(map(int, input().split())))

U = A.union(B)
print(len(U))


# Ex 7 - Set.difference() Operation

n = int(input())
A = set(list(map(int, input().split())))
b = int(input())
B = set(list(map(int, input().split())))

U = A.difference(B)
print(len(U))

# Ex 8 - Set.symmetric_difference() Operation

n = int(input())
A = set(list(map(int, input().split())))
b = int(input())
B = set(list(map(int, input().split())))

U = A.symmetric_difference(B)
print(len(U))

# Ex 9 - Check Strict Superset

A = set(list(map(int, input().split())))
n = int(input())
l = []
for i in range(n):
    B = set(list(map(int, input().split())))
    l.append(B)

f = None

for i in l:
    for j in i:
        if j in A and len(A) > len(i):
            continue
        else:
            f = False
            
if f == False:
    print(f)
else:
    print(True)
    
# Ex 10 - Set .discard(), .remove() & .pop()

n = int(input())
s = set(map(int, input().split()))
N = int(input())

for i in range(N):
    l = list(input().split())
    if l[0] == 'remove':
        s.remove(int(l[1]))
    if l[0] == 'discard':
        s.discard(int(l[1]))
    if l[0] == 'pop':
        s.pop()
 
c = 0
for i in s:
    c += i
    
print(c)

# Ex 11 - Set Mutations

n = int(input())
A = set(map(int, input().split()))
N = int(input())

for i in range(N):
    l = list(input().split())
    s = set(map(int, input().split()))
    if l[0] == 'intersection_update':
        A.intersection_update(s)
    if l[0] == 'update':
        A.update(s)
    if l[0] == 'symmetric_difference_update':
        A.symmetric_difference_update(s)
    if l[0] == 'difference_update':
        A.difference_update(s)
 
 
c = 0
for i in A:
    c += i
    
print(c)
    
# Ex 12 - Check Subset

n = int(input())
for i in range(n):
    l1 = int(input())
    a = set(map(int, input().split()))
    l2 = int(input())
    b = set(map(int, input().split()))
    if len(a) == l1 and len(b) == l2 and l1 <= l2:
        w = True
        for i in a:
            if i not in b:
                w = False
        print(w)
    else:
        print(False)
        
# Ex 13 - The Captain's Room

k = int(input())
A = list(map(int, input().split()))
d = {}

for i in A:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

for j in d:
    if d[j] != k:
        print(j)
        

### COLLECTIONS ###

# Ex 1 - collections.Counter()

from collections import Counter
n = int(input())
l = list(map(int, input().split()))
s = list(Counter(l).keys())
a = list(Counter(l).values())
c = int(input())
ls = []
lp = []

for i in range(c):
    lc = list(map(int, input().split()))
    ls.append(lc[0])
    lp.append(lc[1])

k = 0

for i in range(len(ls)):
    if ls[i] in s:
        ind = s.index(ls[i])
    else:
        continue
    if a[ind] > 0:
        k += lp[i]
        a[ind] = (a[ind])-1

print(k)

# Ex 2 - Word Order

n = int(input())
d = {}
l = []
for i in range(n):
    w = str(input())
    l.append(w)

for i in l:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(len(d))

for i in d:
    print(d[i], end = ' ')
    
# Ex 3 - Company Logo

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    s = input()

d = {}
for i in range(len(s)):
    if s[i] in d:
        d[s[i]] += 1
    else:
        d[s[i]] = 1
        
sd = dict(sorted(d.items(), key=lambda item: (-item[1], item[0])))
e = list(sd.keys())

for i in sd.keys():
    print(i + ' ' + str(sd[i]))
    if i == e[2]:
        break
    
# Ex 4 - Collections.OrederedDict()

from collections import OrderedDict
n = int(input())
d = OrderedDict()
l = []
for i in range(n):
    a = list(map(str, input().split()))
    l.append(a)
    
v = []
for i in l:
    v.append(int(i[-1]))

for i in range(len(l)):
    a = ' '.join(l[i][:-1])
    if a in d:
        d[a] += v[i]
    else:
        d[a] = v[i]
        
for i in d.keys():
    print(i + ' ' + str(d[i])) 
    
# Ex 5 - Collections.namedtuple()

from collections import namedtuple
n = int(input())
stud = namedtuple('stud' , str(input()))
marks = 0
for i in range(n):
    x = stud(*input().split())
    marks += int(x.MARKS)

mean = marks/n

print(f"{mean:.2f}")

# Ex 6 - Collections.deque()

from collections import deque
d = deque()
n = int(input())

for i in range(n):
    l = list(input().split())
    if l[0] == 'append':
        d.append(int(l[1]))
        continue
    if l[0] == 'appendleft':
        d.appendleft(int(l[1]))
        continue
    if l[0] == 'pop':
        d.pop()
        continue
    if l[0] == 'popleft':
        d.popleft()
        
for x in d:
    print(x, end = ' ')
 
# Ex 7 - 

### DATE AND TIME ###

# Ex 1 - Calendar Module

import datetime
mm, dd, yyyy = map(int, input().split())
d = datetime.date(yyyy,mm,dd)
dicti = {0:'MONDAY',1:'TUESDAY',2:'WEDNESDAY',3:'THURSDAY',4:'FRIDAY',5:'SATURDAY',6:'SUNDAY'}
wd = d.weekday()
print(dicti[wd])

# Ex 2 - 


### EXCEPTIONS ###

# Ex 1 - Errors and Exceptions

n = int(input())
for i in range(n):
    try:
        a,b = map(int, input().split())
        print(int(a)//int(b))
    except (ValueError,ZeroDivisionError) as v:
        print ("Error Code:",v)

### BUILT-INS ###
        
# Ex 1 - ginortS

w = input()
l = list(w)
odds, evens, lowe, uppe = '' , '' , '' , ''
for i in l:
    if i.isupper():
        uppe += i
    if i.islower():
        lowe += i
    try:
        if int(i)%2 == 0:
            evens += i
        elif int(i)%2 != 0:
            odds += i   
    except:
        continue
r = sorted(lowe)+sorted(uppe)+sorted(odds)+sorted(evens)
print(''.join(r))

# Ex 2 - Zipped!

n, x = map(int, input().split())
l = []
for i in range(x):
    l.append(list(map(float, input().split())))
voti = list(zip(*l))
for i in voti:
    print(sum(i)/x)
    
# Ex 3 - Athlete Sort

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())


ordered = sorted(arr, key=lambda x: x[k])
for i in ordered:
    print(*i)


### PYTHON FUNCTIONALS ###
    
# Ex 1 - Map and Lambda Function

cube = lambda x: x**3

def fibonacci(n):
    f = []
    if n >= 1:
        f.append(0) 
    if n >= 2:
        f.append(1) 
    for i in range(2, n):
        nextt = f[-1] + f[-2]  
        f.append(nextt)  

    return f

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))



### REGEX AND PARSING CHALLENGES ###
    
# Ex 1 - Regex and Parsing

regex_pattern = r"[,.]" # Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))


# Ex 2 - Re.findall() & Re.finditer()

import re

n = input()
x = re.findall(r'(?<=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])[aeiouAEIOU]{2,}(?=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])', n)

if x:
    print(*x, sep='\n')
else:
    print(-1)
    

# Ex 3 - Detecting Floating Point Number

import re
n = int(input())
for i in range(n):
    num = input()
    a = bool(re.search(
        r'^[+-]?[0-9]*\.[0-9]+$',num))
    print(a)

# Ex 4 - Re.start() & Re.end()

import re

s = input()
k = input()
count = 0
l = []
for i in range(len(s) - len(k) - 1):
    m = re.search(k, s[i:])
    if m is not None:
        count += 1
        start = m.start() + i
        end = m.end() - 1 + i
        if (start,end) not in l:
            l.append((start, end))

if count > 0:
    print(*l,sep='\n')
else:
    print((-1,-1))
    
# Ex 5 - Group(), Groups() & Groupdict()

import re

s = input()

m = re.findall(r'([0-9a-zA-Z])\1+' , s)
if m != []:
    print(m[0])
else:
    print(-1)
    
# Ex 6 - Validating phone numbers

import re

n = int(input())
for i in range(n):
    num = input()
    if len(num) != 10 or not num.isdigit():
        print('NO')
        continue
    m = bool(re.search(r'^[7-9][0-9]{1,9}',num))
    if m == True:
        print('YES')
    else:
        print('NO')

# Ex 7 - Regex Substitution

import re

l = []
n = int(input())
for i in range(n):
    k = str(input())
    l.append(k)
    
for i in range(len(l)):
    l[i] = re.sub(r"(?<=\s)&&(?=\s)", 'and', l[i])
    l[i] = re.sub(r"(?<=\s)\|\|(?=\s)", 'or' , l[i])
    
print(*l, sep = '\n')
    
# Ex 8 - Validating Roman Numerals

regex_pattern = r"^(M{0,3})(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"

import re
print(str(bool(re.match(regex_pattern, input()))))

# Ex 9 - Validating and Parsing Email Addresses

import re
import email.utils

n = int(input())
for i in range(n):
    l = list(map(str, input().split()))
    mail = l[1][1:-1]
    a = email.utils.formataddr((l[0], mail))
    b = bool(re.search(r"^[a-zA-Z][0-9a-zA-Z-._]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$", mail))
    if b == True:
        print(a)

# Ex 10 - Hex Color Code

import re
n = int(input())
code = '\n'.join([input() for _ in range(n)])
l = re.findall(r"(#[a-fA-F0-9]{3}|#[a-fA-F0-9]{6})(?=[;,)])", code)
print(*l, sep = '\n')

# Ex 11 -

### CLOSURES AND DISCLOSURES ###

# Ex 1 - Standardize mobile numbers using decorators

def wrapper(f):
    def fun(l):
        numbers = []
        for i in l:
            p = ['+91',i[-10:-5],i[-5:]]
            numbers.append( " ".join(p))
        f(numbers)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
    
# Ex 2 - Decorators 2 - Name Directory

import operator

def person_lister(f):
    def inner(people):
        sorted_ppl = sorted(people, key=lambda x: int(x[2]))
        return [f(person) for person in sorted_ppl]
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')
    

### NUMPY ###
    
# Ex 1 - Arrays

import numpy

def arrays(arr):
    arr.reverse()
    nump_arr = numpy.array(arr, float)
    return nump_arr

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

# Ex 2 - Shape and Reshape

import numpy

arr = input().strip().split(' ')
int_arr = numpy.array(arr, int)
print(numpy.reshape(int_arr, (3,3)))

# Ex 3 - Transpose and Flatten

import numpy

nxm = list(map(int, input().split()))

arr = []
for i in range(nxm[0]):
    nn = list(map(int, input().split()))
    arr.append(nn)

m = numpy.array(arr)
tarr = numpy.transpose(m)
print(tarr)
print(m.flatten())

# Ex 4 - Concatenate

import numpy

nxmxp = list(map(int, input().split()))
if len(nxmxp) != 3:
    raise TypeError

narr = []
marr = []
for i in range(nxmxp[0]):
    nn = list(map(int, input().split()))
    if len(nn) != nxmxp[2]:
        raise TypeError
    else:
        narr.append(nn)
for i in range(nxmxp[1]):
    mm = list(map(int, input().split()))
    if len(mm) != nxmxp[2]:
        raise TypeError
    else:
        marr.append(mm)
        
n = numpy.array(narr)
m = numpy.array(marr)
print(numpy.concatenate((n,m), axis = 0))

# Ex 5 - Zeros and Ones

import numpy

dim = tuple(map(int, input().split()))

z = numpy.zeros(dim, dtype = int)
o = numpy.ones(dim, dtype = int)
    
print(z,o, sep = '\n')

# Ex 6 - Eye and Identity

import numpy
numpy.set_printoptions(legacy='1.13')

dim = list(map(int, input().split()))
print(numpy.eye(dim[0],dim[1], k = 0))

# Ex 7 - Array Mathematics

import numpy

dim = list(map(int, input().split()))
arra = []
arrb = []
for i in range(dim[0]):
    a = list(map(int, input().split()))
    if len(a) != dim[1]:
        raise TypeError
    else:
        arra.append(a)
for i in range(dim[0]):
    b = list(map(int, input().split()))
    if len(b) != dim[1]:
        raise TypeError
    else:
        arrb.append(b)
A = numpy.array(arra)
B = numpy.array(arrb)

print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)
print(A**B)

# Ex 8 - Sum and Prod

import numpy

dim = list(map(int, input().split()))
n = dim[0]
m = dim[1]

my_array = []
for i in range(n):
    l = list(map(int, input().split()))
    if len(l) != m:
        raise TypeError 
    else:
        my_array.append(l)
        
arr = numpy.array(my_array)
summ = numpy.sum(arr, axis = 0)
prod = numpy.prod(summ)
print(prod)

# Ex 9 - Min and Max

import numpy

dim = list(map(int, input().split()))
n = dim[0]
m = dim[1]

my_array = []
for i in range(n):
    l = list(map(int, input().split()))
    if len(l) != m:
        raise TypeError 
    else:
        my_array.append(l)
        
arr = numpy.array(my_array)
minn = numpy.min(arr, axis = 1)
maxx = numpy.max(minn)
print(maxx)

# Ex 10 - Floor, Ceil and Rint

import numpy
numpy.set_printoptions(legacy='1.13')

arr = list(map(float, input().split()))
a = numpy.array(arr)
print(numpy.floor(a))
print(numpy.ceil(a))
print(numpy.rint(a))

# Ex 11 - Mean, Var and Std

import numpy

dim = list(map(int, input().split()))
n = dim[0]
m = dim[1]

my_array = []
for i in range(n):
    l = list(map(int, input().split()))
    if len(l) != m:
        raise TypeError 
    else:
        my_array.append(l)
        
arr = numpy.array(my_array)
print(numpy.mean(arr, axis = 1))
print(numpy.var(arr, axis = 0))
print(round(numpy.std(arr),11))

# Ex 12 - Dot and Cross

import numpy

n = int(input())
A = []
B = []
for i in range(n):
    l = list(map(int, input().split()))
    if len(l) != n:
        raise TypeError
    else:
        A.append(l)
for i in range(n):
    l = list(map(int, input().split()))
    if len(l) != n:
        raise TypeError
    else:
        B.append(l)
            
a = numpy.array(A)
b = numpy.array(B)

print(numpy.dot(a,b))

# Ex 13 - Inner and Outer

import numpy

a = numpy.array([list(map(int, input().split()))])
b = numpy.array([list(map(int, input().split()))])

print(numpy.inner(a,b)[0][0])
print(numpy.outer(a,b))

# Ex 14 - Polynomials

import numpy

a = list(map(float, input().split()))
x = int(input())

print(numpy.polyval(a,x))

# Ex 15 - Linear Algebra

import numpy

n = int(input())
A = []
for i in range(n):
    l = list(map(float, input().split()))
    if len(l) != n:
        raise TypeError
    else:
        A.append(l)
        
a = numpy.array(A)
print(round(numpy.linalg.det(a),2))


#################
#               #
#     PART 2    #
#               #
#################



### CHALLENGES ###

# Ex 1 - Birthday Cake Candles

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    a = max(candles)
    count = 0
    for i in candles:
        if i == a:
            count += 1
            
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()

# Ex 2 - Kangaroo

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    if x1 < x2 and v1 < v2:
        rr = 'NO'
        return rr
    elif x1 > x2 and v1 > v2:
        rr = 'NO'
        return rr
    elif x1 != x2 and v1 == v2:
        rr = 'NO'
        return rr
    elif (x2-x1) == (v1-v2):
        return 'YES'
    one = x1+v1
    two = x2+v2
    if one == max(one,two):
        bigger , smaller = one , two
    else:
        bigger , smaller = two , one
    for i in range(10000):
        if bigger == one:
            bigger += v1
            one += v1
            smaller += v2
            two += v2
        else:
            bigger += v2
            two += v2
            smaller += v1
            one += v1
        if bigger == smaller:
            return 'YES'
        if smaller > bigger:
            return 'NO'
    return 'NO'   
    

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    print(result)

# Ex 3 - Viral Advertising

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    a = 5
    count = 0
    l = 0
    for i in range(n):
        l = a//2
        count += l
        a = l*3
    return count
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

# Ex 4 - Recursive Digit Sum (Runtime Error)

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    a = n * k
    l = [int(i) for i in a]
    s = sum(l)
    while s >= 10:
        a = str(s)
        l = [int(i) for i in a]
        s = sum(l)
    return s

if __name__ == '__main__':
    
    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    print(result)

# Ex 5 - Insertion Sort - Part 1

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(k, n):
    m = n[-1]
    for i in range(1,k):
        if n[-i-1] > m:
            n[-i] = n[-i-1]
            print(*n)
            if i+1 == k:
                n[-k] = m
                print(*n)
        elif n[-i-1] < m:
            n[-i] = m
            print(*n)
            break

        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

# Ex 6 - Insertion Sort - Part 2

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(k,n):
    for i in range(1,len(n)):
        for j in range(i):
            if n[j] > n[i]:
                n[i], n[j] = n[j], n[i]
        print(*n)
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)


   







