sequence = 'ACTAGCAACCTCAAACAGACACCATGGTGCACCTGACTCCTGTGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCC'

#def main():
#    lijst1, lijst2 = getsequentie()
#    knipplaats(lijst1, lijst2)

#def getsequentie():
#    lijst1=[]
#    lijst2=[]
#    for regel in open ("enzymen.txt"):
#        enzym, seq = regel.split()
#        lijst1, append(enzym)
#        lijst2.append(seq.replace("^",""))
#    return lijst1, lijst2

#def knipplaats (lijst1, lijst2):
#    for i in range(len(lijst2)):
#        if (lijst2[i] in seq):
#            print ("match met", lijst1[i], "in positie", seq.index(lijst2[1]))
#            print(seq)                    

#main()

file = open("enzymen.txt", "r")
for line in file:
    enzyme, seq = line.split()
    seq = seq.replace("^","")
    if seq in sequence:
        for i in range(len(seq)):
            if (seq[i] in sequence):
                print ("match met", enzyme[i], "op positie", sequence.index(seq[i]))
                print(sequence)
      
