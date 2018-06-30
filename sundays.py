import calendar
a=int(input("Enter the year: "))
i=1
#while i in range(1,13):
k=0
while i<13:
	j=1
	while j<32:
		try:
			l=calendar.weekday(a,i,j)
			if(l==6):
				k+=1
		except ValueError:
			l=0
		j+=1
	i+=1
print "Number of Sundays=",k
	
