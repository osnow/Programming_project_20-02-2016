from Bio import SeqIO

def read(filename):
    seqs = []
    struct = []
    count = 1 
    for seq_record in SeqIO.parse(filename, "fasta"):
        if count%2 == 0:
            struct.append(str(seq_record.seq))
        else:
            seqs.append(str(seq_record.seq))
        count += 1

    target_values = []
    for struc in struct:
        for res in struc:
            if res in "PL":
                target = "+1"
            else:
                target = "-1"
            target_values.append(target)
        
    aminos = []
    for seq in seqs:
        for AA in seq:
            aminos.append(AA)

    paired = zip(target_values, aminos)

    for a, b in paired:
        print a, b+":", 1
            

    


read("2seq.txt")
        
        
    
