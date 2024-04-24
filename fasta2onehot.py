#!/usr/bin/env python
# coding: utf-8

"""
@author: Rodrigo Monjaraz-Ruedas (monroderik@gmail.com)

Convert a fasta file with SNPs or DNA sequences and a txt file with populations names per sample into a One-Hot Encoding file needed for VAE analysis for Species Delimitation

Usage: python fasta2onehot.py fasta_file.fasta populations_file.txt output_prefix

requirements:
- python 3.9.7
- Biopython 1.79

"""

import sys
import re
from Bio import SeqIO

# Get arguments 
fasta_file=open(sys.argv[1])
pops_file=open(sys.argv[2])
prefix=sys.argv[3]

#create a list for storing our pops and open the file
pops=[]
for line in pops_file:
    parts = line.split("\t")
    pops.append(parts[1].strip())


# Set the one hot arguments
replacements=[("A", "1.0,0.0,0.0,0.0 "),
("C", "0.0,1.0,0.0,0.0 "),
("G", "0.0,0.0,1.0,0.0 "),
("T", "0.0,0.0,0.0,1.0 "),
("R", "0.5,0.0,0.5,0.0 "),
("Y", "0.0,0.5,0.0,0.5 "),
("S", "0.0,0.5,0.5,0.0 "),
("W", "0.5,0.0,0.0,0.5 "),
("K", "0.0,0.0,0.5,0.5 "),
("M", "0.5,0.5,0.0,0.0 "),
("N", "0.0,0.0,0.0,0.0 "),
("-", "0.0,0.0,0.0,0.0 "),
("\\?", "0.0,0.0,0.0,0.0 ")]


# Read fasta file, replace nucleotides and print IDs to a list
samples=[]
sequences=[]
for seq_record in list (SeqIO.parse(fasta_file, "fasta")):
    sequence = str(seq_record.seq).upper()
    for pat,repl in replacements:
        sequence = re.sub(pat, repl, sequence)
    sequences.append(sequence.strip())
    samples.append(seq_record.id)


# Write result to a txt file
with open(prefix + "_one-hot.txt", 'w') as out_file:
    result = '\n'.join(' '.join(map(str,row)) for row in zip(samples,pops,sequences))
    out_file.write(result)

print('\n' + 'Fasta succesfully converted!!!!!' + ' File saved as ' + prefix + "_one-hot.txt" '\n')

sys.exit()

