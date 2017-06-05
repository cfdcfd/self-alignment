#!/bin/bash
con2db(){
for file in $1/*.fa
do
formatdb -i $file -p F -o T
done
}
dir1=/mnt/work/chengfd/data_contig/T2D/contig
con2db $dir1
