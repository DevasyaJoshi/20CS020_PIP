#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#20CS020 Devasya Joshi 

#Dictionary
#a. Write a python script to check whether a given key already exists in a dictionary
Dict = {'Mon':1,'Tue':2,'Wed':3,'Thu':4}
print("The given dictionary : ", Dict)

check_key = "Mon"

if check_key in Dict:
   print(check_key,"is Present.")
else:
   print(check_key, " is not Present.")
   
#b. Write a Python script to merge two Python dictionaries.
Dict_1 = {1: 'a', 2: 'b'}
Dict_2 = {3: 'c', 4: 'd'}

print({**Dict_1, **Dict_2})

#c. Write a Python program to sum all the items in a dictionary.
my_dict = {'data1':100,'data2':-54,'data3':247}
print(sum(my_dict.values()))

#d. Write a Python script to add a key to a dictionary
d = {0: 10, 1: 20}   
print(d)
d.update({2: 30})
print(d)

#e. Write a Python script to concatenate following dictionaries to create a new one.
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
print({**dic1, **dic2, **dic3})

