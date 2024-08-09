#!/usr/bin/env python
# coding: utf-8

# # All  numpy code that i have learned 

# In[12]:


import numpy as np

## creat a numpy 2D array
a= np.array([[2,3],
           [4,5],
            [6,7]])
print(a)


# In[6]:


a.ndim


# In[8]:


a.itemsize


# In[9]:


a.shape


# In[10]:


## create a array with the given range
b=np.arange(5)


# In[11]:


print(b)


# In[13]:


## add the value of two arrays
c=np.arange(5)
d=np.add(b,c)
print(d)


# In[14]:


##add character of two string arrays
str_arr1= np.array(['country','name'])
str_arr2= np.array(['bangladesh','anik'])
new_strarr=np.char.add(str_arr1,str_arr2)
print(new_strarr)


# In[15]:


##centerized any string
print(np.char.center('anik', 20, fillchar = '-'))


# In[16]:


## capitalize 
print (np.char.capitalize('anik'))

## make the tile 
print(np.char.title("bangladesh is independent now"))

##lower case
print(np.char.lower('ANIK'))


# In[17]:


##Split
print(np.char.split('bangladesh is independent now'))
print(np.char.splitlines('hurrah! \n bangladesh is independent now'))


# In[18]:


## Replace with differenct word

print(np.char.replace('Bangladesh was independent now','was','is'))


# In[ ]:





# # Array manipulation

# In[22]:


# Reshape (convert 1D array into 3D array)

array= np.arange(9).reshape(3,3)
print(array)


# In[23]:


## transpose matrix 
print(np.transpose(array))


# In[42]:


## creat 6*6 array with zero values
z= np.zeros((6,6),dtype=int)
z


# In[49]:


#Stacking Along Rows
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arrnew1 = np.hstack((arr1, arr2))

print(arrnew1)

#Stacking Along Columns
arrnew2 = np.vstack((arr1, arr2))

print(arrnew2)


# In[55]:


## Sorting a array
x= np.array([25,5,6,98,10])
print(np.sort(x))


# In[59]:


## Copy array
a= np.array([1,2,3])
b= a.copy()
print(b)

## copy with view array

c= a.view()
print(c)
d=a
print(d)


# # NumPy Searching Arrays

# In[54]:


arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)

print(x)

##binary search 
y= np.searchsorted(arr,4)
print(y)


# # Arithmetic operation

# In[24]:


## add the value of two array
array1= np.array([10,10,10])
new_array= np.add(array,array1)
print(new_array)


# In[25]:


## subtract two array
new_array2= np.subtract(array,array1)
print(new_array2)


# In[26]:


## multiply two array
new_array= np.multiply(array,array1)
print(new_array)


# In[27]:


## divide two array
new_array= np.divide(array,array1)
print(new_array)


# In[28]:


## slice a array
slice_array= np.arange(10)
sliced= slice(2,10,2)
sliced


# # Iterating over array

# In[29]:


for x in array:
    print(x)


# In[31]:


for x in np.nditer(array):
    print(x)


# In[34]:


##joining two arrays

a= np.array([1,2,3,4])
b=np.array([5,6,7,8])
print(np.concatenate((a,b)))


# # split the array

# In[52]:


split_arr=np.arange(9)
new_arr=np.split(split_arr,3)
print(new_arr)
# Splitting NumPy Arrays in correct way
newsplitarray=np.array_split(split_arr,4)
print(newsplitarray)


# # Histogram

# In[41]:


from matplotlib import pyplot as plt
a= np.array([20,87,65,5,78,56,32,42,56])
plt.hist(a,bins=[0,20,40,60])
plt.title("histogram")
plt.show()


# # find the missing values

# In[44]:


## creating a array with some nan values
Z= np.random.rand(10,10)
Z[np.random.randint(10,size=5),np.random.randint(10,size=5)]=np.nan
Z


# In[46]:


## finding the missing values
print("Total number of missing values is\n", np.isnan(Z).sum())
print("Index of missing values:\n",np.argwhere(np.isnan(Z)))


# In[47]:


## filtering the missing value and put zero
inds= np.where(np.isnan(Z))
Z[inds]=0
Z


# # NumPy ufunc

# In[60]:


## cumutative sum

a= np.array([1,2,3])
b= np.array([4,5,6])
c= np.cumsum(a)
print(c)


# In[62]:


## Finding LCM (Lowest Common Multiple)
n1= 4
n2= 6
lcm= np.lcm(n1,n2)
print(lcm)

## find the LCM of array
arr = np.array([3, 6, 9])

x = np.lcm.reduce(arr)

print(x)


# In[64]:


## Finding GCD (Greatest Common Denominator

n1=4
n2=6
gcd=np.gcd(n1,n2)
print(gcd)

## finding the GCD of array
arr = np.array([20, 8, 32, 36, 16])

x = np.gcd.reduce(arr)

print(x)


# # Trigonometric Functions

# In[65]:


## finding sin value
arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])

x = np.sin(arr)

print(x)


# In[66]:


## Convert Degrees Into Radians

arr = np.array([90, 180, 270, 360])
x = np.deg2rad(arr)
print(x)


# In[67]:


##Radians to Degrees

arr = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])
x = np.rad2deg(arr)
print(x)


# In[68]:


## Finding Angles
x= np.arcsin(.5)
print(x)


# In[69]:


## Hypotenues
h=3
b=5
p=np.hypot(h,b)
print(p)


# # NumPy Set Operations

# In[70]:


## find the unique elements

arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
x= np.unique(arr)
print(x)


# In[74]:


##finding the union of two sets
a= np.array([1,2,3])
b= np.array([4,5,6])
union= np.union1d(a,b)
print("the union is \n",union)

##finding the intersection
intersection= np.intersect1d(a,b)
print("the intersection is \n",intersection)



# In[75]:


pwd


# In[ ]:




