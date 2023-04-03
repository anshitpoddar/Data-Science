# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 12:56:36 2023---classwork of idsup lab

@author: anshi
"""
'''
L=[1,2,3,4,5,6,7,8,9,10]
# --------------------adding elements in different ways
L.append(11)
L.insert(1,100)
L1=[40,50]
L.extend(L1)

#-------------------- removing elements and lists
L.pop(1)
L.insert(9,3) #-------------for remove 
L.remove(3)

L.clear() #--------clears the list
L.delete()#--------deletes the whole list
'''
'''
#-------------appending and adding only even numbers in the list
E=[]
for i in L:
    if i % 2==0:
        E.append(i)
print(E)

#-----------------------sum of list using list
a=(1,2,3,4,5)
b=(6,7,8,9,10)
def addy(c,d):
   s=[i+j for i,j in zip(c,d)]
   print(s)
addy(a,b)    
  '''
  
  