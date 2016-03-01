import numpy as np
import pandas as pd
import sys
import math
from StringIO import StringIO
script_name = sys.argv[0]

# Input files/directories
input_file1 = sys.argv[1]
input_file2 = sys.argv[3:]
output_file = sys.argv[2]
matrices = []

def sigmoid(t):
    """converts scores to log odds"""
    return 1/(1+math.exp(-t))

def makematrix(input):
    """converts psiblast PSSM into dataframe"""
    for f in input:
        array = np.genfromtxt(f, usecols=range(2,22), skip_header=3, skip_footer=5)
        matrix = pd.DataFrame(array, columns=range(1,21))
        matrices.append(matrix.applymap(sigmoid))
makematrix(input_file2)

def read_seqs(filename):
    """Reads file and puts structures in list"""
    from Bio import SeqIO
    structures = []
    count = 1
    for seq_record in SeqIO.parse(filename, "fasta"):
        if count%2 == 0:
            structures.append(str(seq_record.seq))
        count += 1

    for s in structures:
        targets(s)
    write_file(output_file)

target_values = []
def targets(s):
    """Iterates through structures and assigns target value"""
    for res in s:
        if res in "PL":
            target = "+1"
        else:
            target = "-1"
        target_values.append(target)
    return target_values

def write_file(output):
    with open(output, 'a') as f:
        tarcount = 0
        for m in matrices:
            cols = m.columns.values.tolist()
            for index, row in m.iterrows():
                values = [str(cols[i])+':'+str(row[i+1]) for i in range(0, 20)]
                f.write(str(target_values[tarcount])+' '+' '.join(values)+'\n')
                tarcount += 1

read_seqs(input_file1)