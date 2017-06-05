#!/bin/bash
blastn -query ./reads_t2d/SRR341590.fasta -db ./LM.fa -outfmt 7 -max_target_seqs 500 -num_threads 30 -out ./blast_t2d/SRR341590_DLM >> time_LM
