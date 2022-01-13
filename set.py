#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#20CS020 Devasya Joshi
#Set
    
    #a. Write a Python program to add member(s) in a set and clear a set
set1 = {2, 4, 6}
set1.add(8)
print(set1)

    #b.  Write a Python program to remove an item from a set if it is present in the set.
languages = {"Pyhton", "Java", "C++", "HTML"}
languages.remove("Java")
print(languages)

    #c.  Write a Python program to create an intersection, Union, difference of sets.
set1 = {0, 1, 3, 4, 6}
set2 = {2, 1, 3, 5, 7}
print("Union: ", set1 | set2)
print("Intersection: ", set1 & set2)
print("Difference: ", set1 - set2)

    #d. Write a Python program to find maximum and the minimum value in a set.
num_set = {23, 45, 67, 89}
print("Max value: ", max(num_set))
print("Min value: ", min(num_set))

    #e. Write a Python program to find the most common elements and their counts from list, tuple, dictionary.
def most_frequent(List):
    counter = 0
    num = List[0]
     
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
 
    return num
 
List = [2, 1, 2, 2, 1, 3]
print(most_frequent(List))

