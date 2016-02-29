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
    namecount = 1
    for seq_record in SeqIO.parse(filename, "fasta"):
        f = open('protseq'+str(namecount)+'.txt', 'w')
        if count%2 != 0:
            f.write('>'+str(seq_record.id)+ '\n' + str(seq_record.seq)+'\n')
            namecount += 1
        f.close()
        count += 1

read_seqs(input_file)