import sys

f1 = open(sys.argv[1])
f2 = open(sys.argv[2])
s1 = set([i.rstrip() for i in f1])
s2 = set([i.rstrip() for i in f2])
d = s1-s2
for i in list(d):
    print i
