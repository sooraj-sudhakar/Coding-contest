# -*- coding: utf-8 -*-
"""
Fractal analytics: Decoding program

in_string : is the input encoded string
rows : number of rows given as input

The program can work for any test case

"""

import numpy

in_string='mnes__ya_____mi' 
rows=3
columns=len(in_string)//rows
in_string=[i for i in in_string]
txt_matrix=numpy.zeros((rows,columns),dtype=str)
mat_dimension=txt_matrix.shape

i=0
for j in range(0,mat_dimension[0]):
    for k in range(0,mat_dimension[1]):
        if i<len(in_string)+1:
            txt_matrix[j][k]=in_string[i]
            i=i+1
        
temp=[]   
for i in range(0,mat_dimension[1]):
    out=list(txt_matrix.diagonal(offset=i))
    temp.extend(out)

out_string=''.join(temp)
out_string=out_string.replace('_',' ')
out_string=out_string.strip()
print(out_string)
