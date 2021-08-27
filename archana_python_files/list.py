#!/usr/bin/env python
# coding: utf-8

# In[1]:


abc = ["abhi", 10, True, 80.56]


# In[3]:


print(abc)


# In[4]:


a = 45
b = 50

abc = ["abhi", 10, True, 80.56, a,b]


# In[5]:


print(abc)


# In[ ]:





# In[6]:


c = [2 ** i for i in range(10)]


# In[7]:


print(c)


# In[9]:


d = [2 * i for i in range(10)]


# In[10]:


d


# In[ ]:





# In[ ]:





# In[11]:


f = [1,2,3,4,5]


# In[24]:


empty_list = []


# In[25]:


for i in f:
    if i % 2 != 0:
        empty_list.append(i*5)


# In[26]:


print(empty_list)


# In[ ]:





# In[ ]:





# In[30]:


new_list = [n * 5 for n in f if n % 2 != 0]


# In[28]:


print(new_list)


# In[ ]:





# In[ ]:





# In[ ]:





# In[31]:


g = [2,4,6,8]


# In[36]:


empty_list = []
for i in g:
    if i % 2 != 0:
        empty_list.append(i*5)


# In[34]:


print(empty_list)


# In[ ]:




