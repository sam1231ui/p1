#!/usr/bin/env python
# coding: utf-8

# In[93]:


list2 = [1,2,3,4,5]
print (list2)
list2.append(2)
print(list2)
del list2[1]
print(list2)


# In[107]:


mytuple = ("1","2","3")
print(mytuple)
x = input("enter the vale to be accessed")
if x in mytuple:
    print("value",x)
else:
    print("no, the value is no in tuple")
    
 


# In[110]:


mydict = {1:"sam",2:"swo",3:"hank"}
print(mydict)
del mydict[2]
print(mydict)


# In[ ]:




