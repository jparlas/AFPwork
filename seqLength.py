my_dna = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"

#find the location of GAATTC. The length will be ONE more (since the index is found)
frag1_length = my_dna.find("GAATTC") + 1

#find the length of the second fragment by subtracting the len of the the first from the total
frag2_length = len(my_dna) - frag1_length

#print out each fragment length
print("length of fragment one is " + str(frag1_length))
print("length of fragment two is " + str(frag2_length))