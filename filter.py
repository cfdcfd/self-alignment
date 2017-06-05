#!/usr/bin/env python
#coding:utf-8
def usage():
    print '''
-i input_file
-o output_file
-h help
'''
import sys,getopt
opts,agrs = getopt.getopt(sys.argv[1:],'hi:o:')
input_file = ''
output_file = ''
for op,value in opts:
    if op == '-i':
        input_file = value
        f_input = open(input_file,'r')
    elif op == '-o':
        output_file = value
        f_output = open(output_file,'w')
    elif op == '-h':
        usage()
        sys.exit()

num_orig = 1
num_filter = 0
temp_SRR = []
temp_line = f_input.readline()
temp_list = temp_line.strip().split('|')
length = int(temp_list[1])
temp_1 = []
temp_148 = []
while True:
    temp_line = f_input.readline()
    if len(temp_line) == 0:
        break
    temp_list = temp_line.strip().split('\t')

    if temp_SRR == []:
        temp_SRR = temp_list
    elif temp_list[0] != temp_SRR[0]:
        for value1 in temp_1:
            for value2 in temp_148:
                if value1[1] == value2[1]:
                    if abs(int(value1[8])-int(value2[8]))<800:
                        line1 = '\t'.join(value1) + '\n'
                        line2 = '\t'.join(value2) + '\n'
                        f_output.write(line1)
                        f_output.write(line2)
                        temp_1 = []
                        temp_148 = []
                        num_filter = num_filter + 1

        temp_SRR = temp_list   
        num_orig = num_orig + 1
        temp_1 = []
        temp_148 = []

    if float(temp_list[11])<10:
        pass
    elif int(temp_list[6]) < (length/4):
        temp_1 = temp_1+[temp_list]
    elif int(temp_list[7]) > (length*3/4):
        temp_148 = temp_148+[temp_list]

for value1 in temp_1:
    for value2 in temp_148:
        if value1[1] == value2[1]:
            if abs(int(value1[8])-int(value2[8]))<800:
                line1 = '\t'.join(value1) + '\n'
                line2 = '\t'.join(value2) + '\n'
                f_output.write(line1)
                f_output.write(line2)
                num_filter = num_filter + 1

if input_file != '':
    f_input.close()
 
if output_file != '':
    f_output.close()
     
print length,num_orig,num_filter,temp_SRR[0]
 
 
 
 
 
 
 
 
