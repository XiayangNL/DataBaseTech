#!/usr/bin/python

import sys


f=open(sys.argv[1], 'r');

ll = f.readlines()

poses = open('poses.txt', 'w')
edges = open('edges.txt', 'w')
switches = open('switches.txt', 'w')

for l in [x for x in ll if x.startswith('VERTEX_SE2')]:    
    l=l.split()
    s = ' '.join(l[1:]) + '\n'
    poses.write(s)


for l in [x for x in ll if x.startswith('EDGE_SE2 ')]:    
    l=l.split()
    s = ' '.join(l[1:]) + '\n'
    edges.write(s)


    
for l in [x for x in ll if x.startswith('EDGE_SE2_SWITCHABLE')]:    
    l=l.split()
    s = ' '.join(l[1:]) + '\n'
    edges.write(s)

for l in [x for x in ll if x.startswith('EDGE_SE2_MAXMIX')]:    
    l=l.split()
    s = ' '.join(l[1:]) + '\n'
    edges.write(s)


for l in [x for x in ll if x.startswith('VERTEX_SWITCH')]:    
    l=l.split()
    s = l[-1] + '\n'
    switches.write(s)

