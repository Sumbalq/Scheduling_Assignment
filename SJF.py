a = []
burst=[]
wait=[]
wtotal=0
number = int(input('Enter total no of processes: '))
arrivaltime=(int(input('Enter p_arrival time: ')))
for i in range(number):
    a.append([])
    a[i].append(int(input('Enter p_number: ')))
    #pbust = 
    burst.append(int(input('Enter p_bust time: ')))
j=1
for i in range(number):
    p=i
    for j in range(number):
        if burst[j]<burst[p]:
            p=j
        temp=burst[i]
        burst[i]=burst[p]
        burst[p]=temp
        temp=a[i]
        a[i]=a[p]
        a[p]=temp
wait.append(0)
j=0
for i in range(number):
    wait.append(0)
    for j in range(i):
        wait[i]+=burst[i]
    wtotal+=wait[i]
print ('ProcessNumber\tArrivalTime\tBurstTime\tWaiting Time')
for i in range(number):
    print (a[i])
    print('\t\t')
    print(arrivaltime)
    print('\t\t')
    print(burst[i])
    print('\t\t')
    print(wait[i])
    
print ('Total waiting time: ')
print(wtotal)
print ('Average waiting time: ')
print(wtotal/number)
