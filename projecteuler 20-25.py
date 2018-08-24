
# coding: utf-8

# In[5]:



f=1
for i in range(2,101):
    f=f*ile

sum_=0
while f>0:
    sum_=sum_+f%10
    f=f//10
print(sum_)


# In[9]:


def mysum(list_):
    import functools
    return functools.reduce(lambda x,y:x+y, list_)
f=1
for i in range(2,101):
    f=f*i
sum_=0
a=[int(c) for c in str(f)]
print(mysum(a))


# In[7]:


def mysum(list_):
    import functools
    return functools.reduce(lambda x,y:x+y, list_)

