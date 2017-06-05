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
f_output = open(output_file,'a')
while True:
    temp_line = f_input.readline()
    if re.search('length',temp_line):
        le = re.search('\d*$',temp_line)
        id_reads = re.search('SRR\d+',temp_line)
        length = id_reads.group()+'|'+le.group()+'\n'
        f_output.write(length)
        break
    if len(temp_line) == 0:
        break

NK=0;N=0;D=0;DK=0        
while True:
    temp_line = f_input.readline()
    if len(temp_line) == 0:
        break

    if temp_line[0] == '''#''':
        pass
    else:
	temp_list=temp_line.strip().split('\t')
	if re.match('N',temp_list[1]):
  	    if int(temp_list[3])>69:
                N=N+1
            else:
                NK=NK+1
        elif re.match('D',temp_list[1]):
	    if int(temp_list[3])>69: 
                  D=D+1
            else:
	        DK=DK+1

line='N'+':'+str(N)+'\n'+'D'+':'+str(D)+'\n'+'NK'+':'+str(NK)+'\n'+'DK'+':'+str(DK)+'\n'
f_output.write(line)
f_input.close()
f_output.close()

