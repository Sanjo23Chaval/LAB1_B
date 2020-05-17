#!/usr/bin/python
import sys
import math


def get_blast(filename):
    f_list=[]
    d={}
    f = open(filename)
    for line in f:
        v=line.rstrip().split()
        d[v[0]]=d.get(v[0],[])
        d[v[0]].append([float(v[1]),int(v[2])])
    for k in d.keys():
        d[k].sort()
        f_list.append(d[k][0])
    return f_list

def get_data(filename):
    ldata=[]
    f = open(filename)
    for line in f:
        v=line.rstrip().split()
        ldata.append([float(v[1]),int(v[2])])
    return ldata

def get_cm(data,th):
    cm = [[0.0,0.0],[0.0,0.0]]
    for i in data:
        if i[0]<th and i[1]==1:
            cm[0][0]=cm[0][0] + 1
        if i[0]>=th and i[1]==1:
            cm[1][0]=cm[1][0] + 1
        if i[0]<th and i[1]==0:
            cm[0][1]=cm[0][1]+1
        if i[0]>th and i[1] ==0:
            cm[1][1] = cm[1][1]+1
    return cm

def get_acc(m):
    return float(m[0][0]+m[1][1])/(sum(m[0])+sum(m[1]))

def mcc(m):
  d=(m[0][0]+m[1][0])*(m[0][0]+m[0][1])*(m[1][1]+m[1][0])*(m[1][1]+m[0][1])
  return (m[0][0]*m[1][1]-m[0][1]*m[1][0])/math.sqrt(d)

if __name__== "__main__":
    filename=sys.argv[1]
    #th=float(sys.argv[2])
    data = get_blast(filename)
    for i in range(20):
        th=10**-i
        cm= get_cm(data,th)
        print 'TH:',th,'ACC:',get_acc(cm),'MCC:',mcc(cm), 'CM:',cm
