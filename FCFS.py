a = []

tw = 0

number = int(input('Enter no of processes: '))

for i in range(number):

    a.append([])

    a[i].append(input('Enter process name: '))

    a[i].append(int(input('Enter parrival time: ')))

    tw += a[i][1]
    a[i].append(int(input('Enter p_burst time: ')))

a.sort(key = lambda a:a[1])


print ('Process_Name\tArrival_Time\tBurst_Time')

for i in range(number):
    
    print (a[i][0])
    print ('\t\t')
    print (a[i][1])
    print('\t\t')
    print(a[i][2])
    

print ('Total_waiting_time: ')
print(tw)

print ('Average_waiting_time: ')
print(tw/number)
#   S c h e d u l i n g _ A s s i g n m e n t  
 