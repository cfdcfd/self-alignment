#!/bin/bash
allFiles() {
for file in $1/*
do
{
filename=`echo $file | cut -d / -f 6`
python filter.py -i $file -o $2/$filename
} 
done
}

dir2=/home/chengfd/python/blast_result
dir1=/mnt/work/chengfd/blast_result
allFiles $dir1 $dir2
