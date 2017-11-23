my_dna = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"

#store exon1 values into new variable
exon1 = my_dna[0:63]

#store intro values into new variable
intron = my_dna[63:90]

#store exon2 values into new variable
exon2 = my_dna[90:]

#print out coding and non coding sections
print('Original sequence: {0} \n'.format(my_dna))
print("Coding DNA: {0}\nNon Coding DNA: {1}\nCoding DNA: {2}".format(exon1, intron.lower(),exon2))