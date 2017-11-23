my_dna = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
exon1 = my_dna[0:63]
exon2 = my_dna[90:]
print('Original sequence: {0} \n'.format(my_dna))
print('Coding exon 1: {0} \nCoding exon 2: {1}'.format(exon1, exon2))
