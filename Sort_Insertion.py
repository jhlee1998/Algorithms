# -*- coding: utf-8 -*-
"""Sort_Insertion

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1g0HRF4_8gQwLoluYa-sTIYhwIENls43y
"""

list1 = [3, 2, 1, 9, 6, 5, 7, 2, 1, 0]

for x in range(1, len(list1)):
    for y in range(x-1, -1, -1):
      if list1[y+1] < list1[y]:
        peter = list1[y]
        list1[y] = list1[y+1]
        list1[y+1] = peter
        
        print(x, y, list1)