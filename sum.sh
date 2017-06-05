#!/bin/bash
find -name "DLF*.fa" -exec cat {} \; >> DLF.fa
find -name "DLM*.fa" -exec cat {} \; >> DLM.fa
find -name "DOF*.fa" -exec cat {} \; >> DOF.fa
find -name "DOM*.fa" -exec cat {} \; >> DOM.fa
find -name "NLF*.fa" -exec cat {} \; >> NLF.fa
find -name "NLM*.fa" -exec cat {} \; >> NLM.fa
find -name "NOF*.fa" -exec cat {} \; >> NOF.fa
find -name "NOM*.fa" -exec cat {} \; >> NOM.fa
