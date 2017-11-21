#this is the sequence to count
#mySequence = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

#tell the user what is happening.
print('This programm will display the GC content of a DNA sequence ')

mySequence = input('Enter your DNA sequence ')
#count the number of C in sequence
numC = mySequence.count('C')

#count the number of G
numG = mySequence.count('G')

#find the total number of bases.
total = len(mySequence)

#calculate the percentage.
percentGC = (numG + numC)/total *100

#the format method allows me to format the float with any number of decimal
#places. I can easily add more placeholders and variables.
print('The GC content of the sequence is {0:.1f}%'.format(percentGC))
print(round(percentGC, 2))
