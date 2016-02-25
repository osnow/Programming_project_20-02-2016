import sys

script_name = sys.argv[0]

# Input files/directories
input_file = sys.argv[1]

# Output files/directories
#output_file = sys.argv[2]

def create_dsets(filename):
    from Bio import SeqIO
    sequences = list(SeqIO.parse(filename, 'fasta'))
    divided = [sequences[x:x+14] for x in range(0, len(sequences),14)]
    #filenames = ['train1.txt','train2.txt','train3.txt','train4.txt','train5.txt','finaltest.txt']
    for i, s in enumerate(divided):
        f = open("train"+str(i+1)+".txt","w")
        for n in s:
            f.write('>'+str(n.id) + '\n' + str(n.seq) +"\n")
        f.close()

        '''with open(fname, 'w') as output:
            print seqs
            output.write(str(seq) + '\n')
            for i in seqs:
                print i.seq
                output.write(i.seq + '\n')'''

create_dsets(input_file)
