from xlrd import open_workbook
import xlwt
a='/home/sanket/Desktop/pr4/ui/dummyip.xlsx'

#fuction to calculate total marks of each student 
def cal_total(values):
	total=[]
	for i in range(4,len(values)):
		total.append(sum(values[i][j] for j in range(2,len(values[i]))))
	return total



#fuction to find CO's used in paper
def coset(values):
	s=set(values[1][i] for i in range(2,len(values[1])))
	return s


#fuction to create dictionary for calcutating total mark assing to each student 
def hashtot(h):
	hshmap={}
	for i in range(len(h)):
		hshmap[h[i]]=0.0
	return hshmap


#fuction to create dictionary for hashmap 
def hashmap(a,s):
	hshmap={}
	for i in range(len(s)):
		l1=[]
		for  j in range(a):
			l1.append(0.0)    #initializing all values with 0.0
		hshmap[s.pop()]=l1
	return hshmap


#fuction to calculate marks assing to each CO
def cal_mekassign(values,cotot):
	for i in range(2,len(values[1])):
		cotot[values[1][i]]=cotot[values[1][i]]+values[0][i]
	return cotot


#fuction to calculate COwise marks of each student using hashmap
def cal_comrk(values,hashmapl):
	for i in range(4,len(values)):
		for j in range(2,len(values[i])):
			hashmapl[values[1][j]][i-4]=hashmapl[values[1][j]][i-4]+values[i][j]
	return hashmapl	




#fuction to write all co column and total col with lable
def info_write(sheet1,a,info,token):
	row=sheet1.row(3)
	row.write(a,token)
	for rnum in range(4,len(info)+4):
		row=sheet1.row(rnum)
		row.write(a,info[rnum-4])


#fuction to calculate discrimination index
def discrimination(total):
	l=float(len(total))
	avg=sum(total)/l
	nl=len([i for i in total if i>=avg])
	nu=l-nl
	uli=(nl-nu)/(l/2)
	return uli


#fuction to calculate difficulty index
def difficulty(total,cotot):
	tmrk=0.0
	for k,v in cotot.items():
		tmrk=tmrk+v
	p=(float(sum(total))/(tmrk*len(total)))*100
	return p



#fuction to write output on Excel file
def writeonfile(values,total,hashmapl,cotot):
	book = xlwt.Workbook()
	sheet1 = book.add_sheet("PySheet1")
	for rnum in range(len(values)):
		row=sheet1.row(rnum)
		for i in range(len(values[rnum])):
			row.write(i,values[rnum][i])

	#write total marks of ech student and average of class		
	info_write(sheet1,len(values[1]),total,"Total")
	row=sheet1.row(len(values)+3)
        row.write(2,"Average Marks")
	row.write(3,sum(total)/float(len(total)))

	#Write roll no of topper in subject
	row=sheet1.row(len(values)+4)
        row.write(2,"Topper in subject")
	row.write(3,values[total.index(max(total))+4][0])
	
	#Write p value for each CO
	a=len(values[1])
	b=len(values)+4
	for key,val in hashmapl.items():
		a=a+1
		b=b+1
		info_write(sheet1,a,val,key)
		row=sheet1.row(b)
		row.write(2,("P value for ",key))
                #row.write(3,(((len([i for i in val if i >= sum(val)/float(len(val))])/float(len(total)))*100)))	
		row.write(3,((len([i for i in val if i >= (cotot[key]/2.0)])/float(len(val)))*100))
	
	p=difficulty(total,cotot)
	uli=discrimination(total)
	print (p)
	print(uli)
	b=b+1
	if(((p>20.00 and p<30.00) and (uli>0.15)) or ((p>80.00 and p<90.00)and(uli>0.15)) or ((p>30.00 and p<70.00)and(uli>0.25))):
		row=sheet1.row(b)
		row.write(2,"Quality of student")
		row.write(3,suitable)
	else:
		row=sheet1.row(b)
		row.write(2,"Quality of student")
		row.write(3, "Not suitable")

	#save file                	
	book.save("Result.xlsx")			



#main fuction
def main():
	#reading data from inpute file
	wb = open_workbook('onlinedummy.xlsx')
	for s in wb.sheets():
		values = []     #store whole sheet in values variriable
		for row in range(s.nrows):
			col_value = []
			for col in range(s.ncols):
				value=(s.cell(row,col).value)
				if(row>1 and row <=3):
					try : value = str(value)
					except :pass
				elif(col>=2):
					try : value = float(value)
					except :pass
				else:
					try : value = str(value)
					except :pass
					
				col_value.append(value)
			values.append(col_value)

	print (values)
'''	#call to calculate total of each student
	total=cal_total(values) 
	
	#call to find CO's used in paper
	s=coset(values)
	h=list(s)
	print h

	#call to calcuate marks assing to each CO
	cotot=hashtot(h)
	cotot=cal_mekassign(values,cotot)
	#print(cotot)
	#call to create dictionary for hashmaping	
	hashmapl=hashmap(len(values)-4,s)
	
	#call to calculate COwise marks of each student
	hashmapl=cal_comrk(values,hashmapl)
	#print hashmapl

	#call to write Output in file
	writeonfile(values,total,hashmapl,cotot)

'''
main()
