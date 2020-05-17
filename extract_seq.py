#!/usr/bin/python
import sys

def get_ids(idfile):
    ids = open(idfile).read().rstrip().split('\n') #Everything is charged in the memory in this way
    return ids

def print_seqs(ids, dbfile):
    with open(dbfile, 'r') as fdb: #In this way we read the file line by line instead of charging everything at the same time
        for line in fdb:
            if line[0] == ">":
                #pid = line.split('|')[1]
                pid = line[1:].rstrip()
            if pid in ids:
                print line.rstrip()


if __name__ == '__main__':
    idfile = sys.argv[1]
    dbfile = sys.argv[2]
    ids = get_ids(idfile)
    print_seqs(ids, dbfile)
