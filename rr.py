p=[]
finish=[]
twait=[]
remainburst=[]
total=0
number=int (input('Enter the total number of processes: '))
quantum=int (input('Enter time quantum: '))

for i in range(number):
	p.append([])
	p[i].append(input('enter process name: '))
	p[i].append(int(input('enter arrival time: ')))
	p[i].append(int(input('enter burst time: ')))
	p[i].append(p[i][2]) #remaining burst time
	total+=p[i][2] #total burst time
	p[i].append(0) #finish time

p.sort(key=lambda p:p[1])

j=0
now=p[j][1]
while total>0:
	if p[j][3]<quantum and p[j][3]!=0 and p[j][1]<=now:
		total=total-p[j][3]
		now=now+p[j][3]
		p[j][4]=now
		p[j][3]=0
	elif p[j][3]>=quantum and p[j][1]<=now:
		p[j][3]=p[j][3]-quantum
		now=now+quantum
		total=total-quantum
		if p[j][3]==0:
			p[j][4]=now
	if (j+1)<number:
		j=j+1
	else:
		j=0

print ('Process          Arrival time        Burst time        waiting time')
for i in range(number):
	print (p[i][0])
	print(' \t\t')
	print(p[i][1])
	print(' \t\t')
	print(p[i][2])
	print(' \t\t')
	print(p[i][4]-p[i][1]-p[i][2])
