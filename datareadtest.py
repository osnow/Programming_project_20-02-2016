import sys

script_name = sys.argv[0]

# Input files/directories
input_file = sys.argv[1]

# Output files/directories
output_file = sys.argv[2]

target_values = []
residues = []

def read_seqs(filename):
    from Bio import SeqIO
    seqs = []
    structures = []
    count = 1 
    for seq_record in SeqIO.parse(filename, "fasta"):
        if count%2 == 0:
            structures.append(str(seq_record.seq))
        else:
            seqs.append(str(seq_record.seq))
        count += 1
    for s in structures:
        targets(s)
    for a in seqs:
        aminos(a)
    
    write_data(output_file)
        
def targets(s):
    for res in s:
        if res in "PL":
            target = "+1"
        else:
            target = "-1"
        target_values.append(target)
    return target_values

def aminos(a):     
    aminoacids = {'A':1, 'C':2, 'E':3, 'D':4, 'G':5, 'F':6, 'I':7, 'H':8, 'K':9, 'M':10,\
    'L':11, 'N':12, 'Q':13, 'P':14, 'S':15, 'R':16, 'T':17, 'W':18, 'V':19, 'Y':20}
    for AA in a:
        residues.append(aminoacids[AA])
    return residues
    
def write_data(output):
    f = open(output,"w")  
    paired = zip(target_values, residues)
    for a, b in paired:
        f.write(a + ' ' + str(b) + ":1\n")  
    f.close()
    
read_seqs(input_file)

        
        
    
