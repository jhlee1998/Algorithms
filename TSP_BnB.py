# -*- coding: utf-8 -*-
"""TSP_BnB

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Q09y3OhsCBO39oWGJxjHHzqtuER8ZQc9
"""

import numpy as np

def bound(input, s):
  best = [1 * np.inf]
  sum = 0
  gone = 0
  will_go = 0
  total_city = "01234"

  for x in range(len(s)-1):
    gone += input[int(s[x])][int(s[x+1])]
    #print(gone)
    remain_city = total_city.translate('s[x]')
    #print(remain_city)
    
  for a in total_city:
    q = input[int(a)]
    q.remove(0)
    will_go += min(q)
  #print(will_go)
  bound_1 = gone + will_go
  #print(bound_1)
  return bound_1

data = [[0, 14, 4, 10, 20], 
        [14, 0, 7, 8, 7], 
        [4, 5, 0, 7, 16], 
        [11, 7, 9, 0, 2], 
        [18, 7, 17, 4, 0]]
start = "01"
z = bound(data, start)
print(z)