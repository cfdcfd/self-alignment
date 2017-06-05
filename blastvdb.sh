#!/bin/bash

blastvdb(){
for file in $1/*.fasta
do
echo $file
outfile=${file%*.fasta}_DLM
#outfile=${outfile##*/}
echo $outfile
time blastn -query $file -db ../LM.fa -outfmt 7 -max_target_seqs 500 -num_threads 30 -out $outfile >> time_LM
done
}
dir1=/mnt/work/chengfd/data_contig/T2D/reads/DLM1
blastvdb $dir1
