#!/usr/bin/env python
#coding:utf-8
def usage():
	print '''
-i input_file
-o output_file
-h help
'''

import sys,getopt
import re
opts,agrs = getopt.getopt(sys.argv[1:],'hi:o:')
input_file = ''
output_file = ''
for op,value in opts:
    if op == '-i':
        input_file = value
    elif op == '-o':
        output_file = value
    elif op == '-h':
        usage()
        sys.exit()

f_input = open(input_file,'r')
f_output = open(output_file,'w')

contig_dict={}
while True:
    temp_line = f_input.readline()
    break

NK=0;N=0;D=0;DK=0;N_score=0;D_score=0;PK=0;        
temp_cp=0;
temp_len=0;
while True:
    temp_line = f_input.readline()
    if len(temp_line) == 0:
        break

    if temp_line[0] == '''#''':
        pass
    else:
	temp_list=temp_line.strip().split('\t')
        key=temp_list[1]
            
        if key in contig_dict:
            contig_dict[key]+=1
        else:
            contig_dict[key]=0
            contig_dict[key]+=1

import pickle
pickle.dump(contig_dict,f_output)
f_input.close()
f_output.close()

