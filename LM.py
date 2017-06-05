#!/bin/python
f=open('LM.fa','r')
f1=open('condictNLM','r')
f2=open('condictDLM','r')
import pickle
Ddict=pickle.load(f2)
Ndict=pickle.load(f1)
N=0;D=0;
Pdict={}
for key in Ddict:
    if key in Ndict:
        pass
    elif 'D' in key:
        D+=1
        Pdict[key]=Ddict[key]

for key in Ndict:
    if key in Ddict:
        pass
    elif 'N' in key:
        N+=1
        Pdict[key]=Ndict[key]

print N,D
f3=open('condictP','w')
pickle.dump(Pdict,f3)
'''import re 
p=re.compile(r'\wLM\S+')
f4=open('LM_pick.fa','w')
flag=0
while True:
    a=f.readline()
    if len(a)==0:
        break

    if a[0]=='>':
        re_dict=p.search(a)
        if re_dict.group() in Pdict:
            f4.write(a)
            flag=1
        else:
            flag=0
    elif flag==1:
        f4.write(a)
'''
f.close()
f1.close()
f2.close()
f3.close()
'''f4.close()'''



