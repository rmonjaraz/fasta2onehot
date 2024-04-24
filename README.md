# fasta2onehot
---
Convert a fasta file with SNPs or DNA sequences and a txt file with populations names per sample into a One-Hot Encoding file needed for VAE analysis for Species Delimitation

---

## Input
**Fasta File** - Multiple sequence alignment in Fasta format
**Population file** - A txt file (tab delimited), first column is the sample name (same as in the Fasta file), second column is the population that sample belongs to.
*Example:*
sample1 Pop1
sample2 Pop1
sample3 Pop2
sample4 Pop2

**prefix** - Any name for labaling the output file

---
## Usage
`python fasta2onehot.py fasta_file.fasta populations_file.txt output_prefix`

---
## Requirements
- python 3.9.7
- Biopython 1.79

---
## License
The code within this repository is available under a 3-clause BSD license. See the License.txt file for more information.

---
## Citation
If you use this script for your own research, please provide the link to this software repository in your manuscript:
https://github.com/rmonjaraz/fasta2onehot
