# -*- coding: utf-8 -*-
"""
Count frequencies of various alphabets (Convert upper case into lower case and input given by user),
plot the results for this as a bar chart with x-axis being the letter and y-axis as the corresponding
frequency
"""


alphabets=input("enter the string").lower()
print("string in lowercase:",alphabets);

d={}
for ele in alphabets:
    if ele in d:
        d[ele]+=1
    else:
        d[ele]=1
        
print("items with there number of ocurrences")
import matplotlib.pyplot as plt
names=list(d.keys())
values=list(d.values())
plt.bar(names,values)