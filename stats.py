#!/usr/bin/env python
#coding:utf-8
# 脚本用于初步统计比对结果
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

dict_SRR = {}
while True:
    temp_line = f_input.readline()
    if len(temp_line) == 0:
        break
    temp_list = temp_line.strip().split('\t')
    temp_key = temp_list[1].split('|')
    key_temp = temp_key[3]
    if dict_SRR.has_key(key_temp):
        dict_SRR[key_temp] = dict_SRR[key_temp] + 1
    else:
        dict_SRR[key_temp] = 1

for key in dict_SRR:
    line_out = key + '\t' + str(dict_SRR[key]) + '\n'
    f_output.write(line_out)

if input_file != '':
    f_input.close()
 
if output_file != '':
    f_output.close()
     
