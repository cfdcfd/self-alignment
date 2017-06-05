#!/bin/bash
sedinfo(){
for file in $1/*
do
if [[ $file =~ ([A-Z]{3}[0-9]{3}) ]]; then
    a=${BASH_REMATCH[1]}
    sed -i 's/>/>'$a'/g' $file 
fi
done
}
dir=/mnt/work/chengfd/data_contig/T2D/contig

sedinfo $dir
