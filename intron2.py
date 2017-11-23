my_dna = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"

#store exon1 values into new variable
exon1 = my_dna[0:63]

#store exon2 values into new variable
exon2 = my_dna[90:]

#determine length
coding_length = len(exon1 + exon2)
total_length = len(my_dna)

#calculate and print the percentage
print('The percentage of DNA that is coding is: {0:.2f}%'.format(coding_length/total_length*100))
