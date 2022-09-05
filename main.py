#def f1(f2, x):
    #a = f2(x)
    #return a

#b = f1(lambda y: y * 4, 3)
#print(b)
#l = [1, 2, 3, 4, 5]
# c =sorted(l)
#print((sorted(l))[-2])

#s = ['abc', 'xyz', 'aba', '1221']
#c=0
#for j in s:
 #   z = j.split(",")
    # print(z[0][-1])
    # print(type(z))

  #  if (z[0][0] == z[0][-1])and(len(j)>1):
   #         c +=1
    #        print(c)
     #       print(z)

# sort_list_last=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# print(sorted(sort_list_last, key=lambda y:y[1]))
#
# if len(sort_list_last)>=1:
#     print("not empty")
# print(sort_list_last.copy())
# s = "The quick brown fox jumps over the lazy dog"
# n=3
# c=0
# l=s.split(" ")
# print(l)
# for i in l:
#     if len(i)>n:
#         c +=1
# print(c)

# str="The quick brown fox jumps over the lazy dog"
# word_len=[]
# txt = str.split(" ")
# for x in txt:
#     if len(x) > n:
#         word_len.append(x)
#         #c +=1
# print(word_len)
# print(c)


# l1=[1,2,3,4,5]
# l2=[5,6,7,8,9]
# l3=l1+l2
# print(l3)
# s = set(l3)
# if len(l3)>len(s):
#     print("duplicate")
# l1=[1,2,3,4,5,6,7]
# del l1[5],l1[4],l1[0]
# print(*l1)
# from random import shuffle
# color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# shuffle(color)
# print(color)
#
# for i in range(1,31):
#     if (i<=5) or (i>=25 and i<=30):
#         print(i*i)
# l1=[1,2,3,4,5]
# l2=[5,6,7,8,9,3]
# for i in l1:
#     for j in l2:
#         if i==j:
#             print(i)
# lst1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
# lst2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]
# x=list(set(lst1) & set(lst2))
# print(x)
# lst1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
# for i in lst1:
#     print(f'{i} index is' , lst1.index(i))
# s = ['a', 'b', 'c', 'd']
# str1 = ''.join(s)
# print(str1)
# import itertools
# original_list = [[2,4,3],[1,5,6], [9], [7,9,0]]
# new_merged_list = list(itertools.chain(*original_list))
# print(new_merged_list)
# import random
# color_list = ['Red', 'Blue', 'Green', 'White', 'Black']
# print(random.choice(color_list))
# my_list = [10,10,10,10,20,20,20,20,40,40,50,50,30]
# dt={}
# for i in my_list:
#     dt[i]=my_list.count(i)
# print(dt)
# sub_set = False
# l = [2,4,3,5,7]
# s = [4,3]
# for i in range(len(l)):
#     if l[i] == s[0]:
#         n = 1
#         while (n < len(s)) and (l[i + n] == s[n]):
#             n += 1
#
#         if n == len(s):
#             sub_set = True
# # print(sub_set)
# from itertools import combinations
# l1 = [10, 20, 30]
# subs = []
# for i in range(0,len(l1)+1):
#     t= [list(x) for x in combinations(l1,i)]
#     if len(t)>0:
#         subs.extend(t)
# print(subs)
# print(i)
# x={'a':'b','a':'c'}
# print(x['a'])
# import re
# text = '''Hi, today 17-jan-2222 16.feb.2222 18/mar/2222 19.12.2222
#             abc@gmail.com xyz$ymail.net def&gmail.com ghi#ymail.net'''
# pattern = re.compile(r'\d{2}[-\./]([a-z]{3}|\d{2})[-\./]\d{4}')
# pattern1 = re.compile(r'[a-z]+([@]|[&]|\$|[#])[a-z]+\.[a-z]{3}')
# matches = pattern.finditer(text)
# matches1 = pattern1.finditer(text)
# for match in matches:
#     print(match.group())
# for match1 in matches1:
#     print(match1.group())

# a =3
# c=0
# for i in range(1,a+1):
#     if a%i==0:
#         c+=1
#         print({i})
#         print(c)
#     else:
#         print({i})
# if c>2:
#     print("not prime")
# else:
#     print("prime")


#def last2(str):
    # Screen out too-short string case.
#     if len(str) < 2:
#         return 0
#     # last 2 chars, can be written as str[-2:]
#     last2 = str[len(str) - 2:]
#     count = 0
#     print(last2)
#     # Check each substring length 2 starting at i
#     for i in range(len(str) - 2):
#         sub = str[i:i + 2]
#         if sub == last2:
#             count = count + 1
#     return count
#
# print(last2('hixxhi'))
# print(last2('xaxxaxaxx'))
# print(last2('axxxaaxx'))

# def array_count9(nums):
#   c=0
#   for i in nums:
#     if i==9:
#       c=c+1
#     return c
# array_count9([1, 2, 9])
# array_count9([1, 9, 9])
# print(array_count9([1, 9, 9, 3, 9]))
# s=[1,2,3,4,5]
# a=""
# for i in s:
#     a+=str(i)
# print(a)
# if '123' in a:
#     print("yes")
from collections import deque
#Remove numbers greater than 50
number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
new_list =[]
for i in list(number_list):
    if i>50:
        number_list.remove(i)
print(number_list)
#Reverse Dictionary mapping
dict = {'A': 65, 'B': 66, 'C': 67, 'D': 68}
new_dict ={}
for k,v in dict.items():
    new_dict[v]= k
print(new_dict)
#convert lowercase char to uppercase of string
str = 'string'
print(str.upper())
print(str.capitalize())
#Count the Number of matching characters in a pair of string
str1 = 'hello'
str2 = 'wishhello'
c = 0
for i in str1:
    f = str2.rfind(i)
    if f >=0:
        c +=1
print(c)
#Program for Find minimum sum of factors of number
num=12
lst=[]
for i in range(1,num):
    if num%i==0:
        lst.append(i+num/i)
lst.sort()
print(int(lst[0]))
#Demostate Deque implementation in python
n_list = [1,2,3,4]
de_q = deque(n_list)
print(de_q)
de_q.append(5)
print(de_q)
de_q.appendleft(0)
print(de_q)
de_q.pop()
print(de_q)
de_q.popleft()
print(de_q)
de_q.insert(4,8)
print(de_q)
de_q.insert(7,9)
print(de_q)
print(de_q.count(8))
de_q.extend([6,7,10])
print(de_q)
de_q.extendleft([-1,-2,-3])
print(de_q)
de_q.rotate(5)
print(de_q)
de_q.reverse()
print(de_q)
#Program to Split the array and add the first part to the end
import array as ar
l = [1,2,3,4,5,6,7,8,9]
a = ar.array('i',l)
print(type(a))
b = a[:3]
print(b)
c = a[3:]
print(c)
d = c+b
print(d)
l2 = []
for j in range(0,3):
     l2.append(j)
print(j)

l1 = []
for i in range(3,len(a)+1):
     l1.append(i)
print(l1)
for k in list(l2):
    l1.append(k)
print(l1)
#sort list of dictionaries by values in Python using lambda function
dict = {'d':4,'e':5,'a':1,'b':2,'f':6,'c':3}
dict2 = sorted(dict.items(),key= lambda x:x[1])
print(dict2)









