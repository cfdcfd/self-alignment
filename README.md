建立比对库进行比对后的分类实验

预处理
python filter_0.py -i /mnt/work/chengfd/data_contig/T2D/blast_t2d/SRR341581 -o /mnt/work/chengfd/data_contig/T2D/filter/SRR341581
python filter.py -i /mnt/work/chengfd/data_contig/T2D/filter_0/SRR341581 
python filter_0.py -i /mnt/work/chengfd/data_contig/T2D/filter_0/SRR341581 -o /mnt/work/chengfd/data_contig/T2D/filter/SRR341581
python filter.py -i /mnt/work/chengfd/data_contig/T2D/filter_0/SRR341581 -o /mnt/work/chengfd/data_contig/T2D/filter/SRR341581
python filter_sum.py -i test_blast -o test1
python filter_sum.py -i /mnt/work/chengfd/data_contig/T2D/blast_t2d/SRR341581_sum -o SRR341581_sumDN


DLM26个 NLM24个
1、	建库（NLM和DLM的比重？）1.61/1.40=1.15
formatdb -i sumcontig.fa -p F -o T
10
2、	比对
time blastn -query ./reads_t2d/SRR341724.fasta -db ./sumcontig.fa -outfmt 7 -max_target_seqs 500 -num_threads 30 -out ./blast_t2d/SRR341724_sum > time_3
3、	统计比对结果
time python statsLM.py -i ./blastnlm/SRR341626_NLM -o ./test_result2
判别reads有效的原则：
1、比对长度>60
2、双端比对
3、计算权重
