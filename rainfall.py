print('This app will do things to rainfall data')
print('----------------------------------------')
rainFall = []
monthlyFall = input('Enter the monthly rainfall sep by comma eg 5,6,7,8')
rainFall = monthlyFall.split(',')

#go through each element of the list
#and convert it to an integer

for i in range(len(rainFall)):
    rainFall[i] = int(rainFall[i])

total = 0
for x in rainFall:
    total += x

maxFall = max(rainFall)
minFall = min(rainFall)
averageFall = total/len(rainFall)

print('The highest rainfall was {0} \n'
      'The lowest rainfall was {1} \n'
      'The average was {2}'.format(maxFall, minFall, averageFall))


