import sys

script_name = sys.argv[0]

# Input files/directories
input_file = sys.argv[1]

def read_seqs(filename):
    """Reads file and puts sequences in one list and structures in another list"""
    from Bio import SeqIO
    seqs = []
    structures = []
    count = 1
    for seq_record in SeqIO.parse(filename, "fasta"):
        f = open('protseq'+str(count)+'.txt', 'w')
        if count%2 != 1:
            f.write('>'+str(seq_record.id)+ '/n' + str(seq_record.seq)+'\n')
        f.close()
        count += 1

read_seqs(input_file)