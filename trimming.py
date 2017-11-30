# open the input file
file = open("DNAinput.txt")

# open the output file
output = open("trimmed.txt", "w")

# go through the input file one line at a time
for dna in file:

    # calculate the position of the last character
    last_position = len(dna)

    # get the substring from the 15th character to the end
    trimmed_dna = dna[14:last_position]

    # print out the trimmed sequence
    output.write(trimmed_dna)

    # print out the length to the screen
    print("processed sequence with length {0}".format(len(trimmed_dna)))