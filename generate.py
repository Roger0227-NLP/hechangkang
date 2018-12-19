# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 15:45:14 2018

@author: Administrator
"""

def generate(self,text,d):
    l=[]
    #    s=""
    for t in text:
        length=len(l)
        if t in d.keys():
            tmp=len(d[t])
            for v in range(tmp):
                for i in l:
                    s1=l[i]+d[t][v]
                    l.append(s1)
        else:
            for j in l:
                s2=l[j]+t
                l.append(s2)
        for r in range(length):
            l.remove(l[r])
    #        l=l[length:-1]
    return l