# open file containing DNA sequence
dna_file = open("genomic_dna.txt")
# read DNA sequence from file
dna = dna_file.read()
#close file
dna_file.close()


# extract exons/introns from DNA
exon1 = dna[0:63]
intron = dna[63:90]
exon2 = dna[90:]
# create coding sequence from exons
coding_seq = exon1 + exon2


# create output file for coding sequence
coding_file = open("coding.txt", "w")
# write coding sequence to file
coding_file.write(coding_seq)
print('Coding file created - coding.txt\n')
# save and close coding sequence file
coding_file.close()

#create output file for NON coding sequence
noncoding_file = open("noncoding.txt", "w")
#write NON coding sequence to file
noncoding_file.write(intron)
print('Non coding file created - noncoding.txt')
#save and close coding sequence file
noncoding_file.close()