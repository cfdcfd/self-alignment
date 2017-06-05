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

NK=0;N=0;D=0;DK=0;N_score=0;D_score=0;PK=0;        
temp_cp=0;
temp_len=0;flag=0
while True:
    temp_line = f_input.readline()
    if len(temp_line) == 0:
        break

    if flag==0 and temp_line[0] == '''#''':
        f_output.write('#\n')
        flag=1
    elif flag==1 and temp_line[0] == '''#''': 
        pass
    else:
        flag=0
	temp_list=temp_line.strip().split('\t')
	if temp_cp==0:
	    temp_cp=temp_list[1]
            temp_len=int(temp_list[3])
	elif temp_cp==temp_list[1]:
            temp_cp=0
            temp_len+=int(temp_list[3])
	    if re.match('N',temp_list[1]):
  	        if temp_len>135:
                    N=N+1
                    f_output.write(temp_line)
                else:
                    NK=NK+1
            elif re.match('D',temp_list[1]):
	        if temp_len>135: 
                    D=D+1
                    f_output.write(temp_line)
                else:
	            DK=DK+1
        else:
            temp_len=int(temp_list[3])
            temp_cp=temp_list[1]

line='N'+'\t'+str(N)+'\n'+'D'+'\t'+str(D)+'\n'+'NK'+'\t'+str(NK)+'\n'+'DK'+'\t'+str(DK)+'\n'
f_output.write(line)
f_input.close()
f_output.close()

