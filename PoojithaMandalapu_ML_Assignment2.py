#!/usr/bin/env python
# coding: utf-8

# In[9]:


stars = int(input('Enter number of stars:'))

#looping to print * in incremental pattern
for i in range (stars):
    print('*'*(i+1))

#looping to print * in decremental pattern
for j in range (stars):
    print('*'*(stars-j-1))


# In[10]:


my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

count=len(my_list)

#looping to print the odd indices by incrementing by 2
for i in range(1, count,2):
    print(my_list[i])


# In[8]:


x = [23, 'Python', 23.98]

#declaring an empty list
l=[]

#looping to append the type of elements in list with type() built-in function
for i in x:
    l.append(type(i))
print(l)


# In[11]:


def sample_list(l):
    
    #declaring an empty list
    l2=[]
    
    #looping to append the unique list in l2 empty list
    for i in l:
        if i not in l2:
            l2.append(i)
    return l2

print('The unique list from the given sample list is:', sample_list([1,2,3,3,3,3,4,5]))


# In[1]:


enter_string = input('Enter a string to calculate count of upper and lower case characters:')

upper_case_count = 0
lower_case_count = 0

#looping to count the lower and upper case characters using built-in functions
for letter in enter_string:
    if letter.islower():
        lower_case_count+=1
        
    elif letter.isupper():
        upper_case_count+=1
        
print('No. of Upper-case characters:', upper_case_count)
print('No. of Lower-case characters:', lower_case_count)


# In[ ]:





# In[ ]:




