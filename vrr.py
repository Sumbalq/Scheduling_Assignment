p=[]
remainb=[]
twait=[]
finish=[]
t=0
no=int(input('Enter the total number of processes: '))
quantum=int (input('Enter quantum time: '))

for i in range(no):
	p.append([])
	p[i].append(input('process name: '))
	p[i].append(int(input('arrival time: ')))
	p[i].append(int(input('burst time: ')))
	p[i].append(p[i][2]) #remaining burst time
	t+=p[i][2] #total burst time
	p[i].append(0) #finish time
	p[i].append(0) #time left afet which it will go to i/o
	p[i].append(0) #remaining quantum time
	p[i].append(-1) #time it will take to come back

p.sort(key=lambda p:p[1])
j=0
now=p[j][1]
for i in range(no):
	if (p[i][0]%3==0):
		p[i][5]=10
while t>0:
	for i in range(no):	#First checks the auxiliary queue
		if p[i][7]==now and p[i][6]!=0: #burst time is not zero
			t=t-a[i][6] #subtract from total time
			now = p+a[i][6]
			p[i][3]=p[i][3]-p[i][6]
			p[i][7]=-1
			p[i][6]=0
			p[i][5]=5
			if p[i][3]==0:
				a[i][4]=now


    	if (p[j][0]%2)!=0 :
                 if p[j][3]<=quantum and p[j][3]!=0 and p[j][1]<=now:
                        t=t-p[j][3]
                        now=now+p[j][3]
                        a[j][4]=now
                        a[x][3]=0
                elif p[j][3]>=quantum and p[j][1]<=now:
                         p[j][3]=p[j][3]-quantum
                         now=now+quantum
                         t=t-quantum
			
	elif (p[j][0]%2)==0 and p[j][7]==-1:
		if p[j][3]<=quantum and p[j][3]!=0 and p[j][1]<=now:
			if p[j][5]>quantum or p[j][5]<=p[j][3]:
				t=t-p[j][3]
				now=now+p[j][3]
				p[j][4]=now
				p[j][3]=0			
			elif p[j][5]<=quantum:
				t=t-p[j][5]
				now=now+p[j][5]
				p[j][7]=5+now
				p[j][6]=quantum-p[j][5]
		elif p[j][3]>quantum and p[j][3]!=0 and p[j][1]<=now:
			if p[j][5]>quantum:
				t=t-quantum
				now=now+quantum
				p[j][5]=p[j][5]-quantum
			else:
				t=t-p[j][5]
				now=now+p[j][3]
				p[j][7]=now+5
				p[j][6]=quantum-p[j][5]		

			
		if (j+1)<no:
			j=j+1
		else:
			j=0
	
print ('Process       Arrival time      Burst time       waiting time')

for i in range(no):
	print (a[i][0])
	print(' \t\t')
	print(a[i][1])
	print(' \t\t')
	print(a[i][2])
	print(' \t\t')
	print(a[i][4]-a[i][1]-a[i][2])
