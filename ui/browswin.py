# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'browse.ui'
#
# Created: Fri Nov 11 12:22:06 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!
from xlrd import open_workbook
import xlwt
import subprocess
import sys
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    h=[]
    hashmapl={}
    filenames=""
    prn=[]
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(1172, 654)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(450, 310, 101, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setPointSize(14)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(630, 440, 121, 41))
	self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(910, 440, 121, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setItalic(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
	self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(260, 10, 1261, 81))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(440, 580, 1261, 81))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(120, 550, 331, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setPointSize(18)
        font.setItalic(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(590, 50, 311, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setPointSize(18)
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.line_2 = QtGui.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(70, 560, 1351, 20))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(80, 0, 151, 121))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8("../icons/wce.gif")))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(1100, 530, 241, 211))
        self.label_6.setText(_fromUtf8(""))
        self.label_6.setPixmap(QtGui.QPixmap(_fromUtf8("../icons/logoit.jpg")))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.line = QtGui.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(0, 120, 1351, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(280, 330, 161, 61))
	self.pushButton.clicked.connect(lambda :self.fileSelect(True))
	self.pushButton_2.clicked.connect(lambda :self.main())
	self.pushButton_3.clicked.connect(lambda :self.showgraph())
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setItalic(True)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(440, 340, 589, 41))
        self.lineEdit.setText(_fromUtf8(""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
	self.pushButton_3.setVisible(False)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#f47004;\">Address :</span></p></body></html>", None))
        self.pushButton_2.setText(_translate("Form", "Get result", None))
	self.pushButton_3.setText(_translate("Form", "Show Graph", None))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#e3a806;\">WALCHAND COLLEGE OF ENGINEERING, SANGLI</span></p></body></html>", None))
        self.label_7.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#e3a806;\">Department of Information Technology</span></p></body></html>", None))
        self.label_8.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#000000;\">Developed &amp; Maintained by -</span></p></body></html>", None))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#e3a806;\">( An Autonomous Institute )</span></p></body></html>", None))
        self.pushButton.setText(_translate("Form", "Browse  File", None))
	#self.pushButton.clicked.connect(self.fileSelect(True))
        
    def fileSelect(self,tripped):
	#filenames=""
    	#filenames = str(glob.glob('*.npy')[0])
	self.pushButton_3.setVisible(False)
    	if tripped==True:
        	self.filenames = QtGui.QFileDialog.getOpenFileName()
    		self.lineEdit.setText(_translate("Form", self.filenames, None))
		#a=filenames
    	return
    
    


#fuction to calculate total marks of each student 
    def cal_total(self,values):
	total=[]
	for i in range(4,len(values)):
		try:
			total.append(sum(values[i][j] for j in range(2,len(values[i]))))
		except:
			print ("Invalid Input")
		#lambda :subprocess.call(['python','invalid.py'])
		#os.system('invalid.py')
			subprocess.Popen(['python','invalid.py'])
			return
	return total



#fuction to find CO's used in paper
    def coset(self,values):
	s=set(values[1][i] for i in range(2,len(values[1])))
	return s


#fuction to create dictionary for calcutating total mark assing to each student 
    def hashtot(self,h):
	hshmap={}
	for i in range(len(h)):
		hshmap[h[i]]=0.0
	return hshmap


#fuction to create dictionary for hashmap 
    def hashmap(self,a,s):
	hshmap={}
	for i in range(len(s)):
		l1=[]
		for  j in range(a):
			l1.append(0.0)    #initializing all values with 0.0
		hshmap[s.pop()]=l1
	return hshmap


#fuction to calculate marks assing to each CO
    def cal_mekassign(self,values,cotot):
	for i in range(2,len(values[1])):
		cotot[values[1][i]]=cotot[values[1][i]]+values[0][i]
	return cotot


#fuction to calculate COwise marks of each student using hashmap
    def cal_comrk(self,values):
	for i in range(4,len(values)):
		for j in range(2,len(values[i])):
			self.hashmapl[values[1][j]][i-4]=self.hashmapl[values[1][j]][i-4]+values[i][j]
	return self.hashmapl




#fuction to write all co column and total col with lable
    def info_write(self,sheet1,a,info,token):
	row=sheet1.row(3)
	row.write(a,token)
	for rnum in range(4,len(info)+4):
		row=sheet1.row(rnum)
		row.write(a,info[rnum-4])


#fuction to calculate discrimination index
    def discrimination(self,total):
	l=float(len(total))
	avg=sum(total)/l
	nl=len([i for i in total if i>=avg])
	nu=l-nl
	uli=(nl-nu)/(l/2)
	return uli


#fuction to calculate difficulty index
    def difficulty(self,total,cotot):
	tmrk=0.0
	for k,v in cotot.items():
		tmrk=tmrk+v
	p=(float(sum(total))/(tmrk*len(total)))*100
	return p



#fuction to write output on Excel file
    def writeonfile(self,values,total,cotot,nm):
	book = xlwt.Workbook()
	sheet1 = book.add_sheet("PySheet1")
	for rnum in range(len(values)):
		row=sheet1.row(rnum)
		for i in range(len(values[rnum])):
			row.write(i,values[rnum][i])

	#write total marks of ech student and average of class		
	self.info_write(sheet1,len(values[1]),total,"Total")
	row=sheet1.row(len(values)+3)
        row.write(2,"Average Marks")
	row.write(3,sum(total)/float(len(total)))

	#Write roll no of topper in subject
	row=sheet1.row(len(values)+4)
        row.write(2,"Topper in subject")
	row.write(3,values[total.index(max(total))+4][0])
	
	#Write p value for each CO
	hmap=self.hashmapl
	a=len(values[1])
	b=len(values)+4
	for key,val in hmap.items():
		a=a+1
		b=b+1
		self.info_write(sheet1,a,val,key)
		row=sheet1.row(b)
		row.write(2,("P value for ",key))
                #row.write(3,(((len([i for i in val if i >= sum(val)/float(len(val))])/float(len(total)))*100)))	
		row.write(3,((len([i for i in val if i >= (cotot[key]/2.0)])/float(len(val)))*100))
	
	p=self.difficulty(total,cotot)
	uli=self.discrimination(total)
	print (p)
	print(uli)
	b=b+1
	if(((p>20.00 and p<30.00) and (uli>0.15)) or ((p>70.00 and p<80.00)and(uli>0.15)) or ((p>30.00 and p<70.00)and(uli>0.25))):
		row=sheet1.row(b)
		row.write(2,"Quality of Paper")
		row.write(3,"suitable")
	else:
		row=sheet1.row(b)
		row.write(2,"Quality of Paper")
		row.write(3, "Not suitable")

	#save file                	
	book.save(nm+"Result.xlsx")
	#self.lineEdit.setText(_translate("Form", "", None))			
	#self.filenames=""
	self.pushButton_3.setVisible(True)
	subprocess.Popen(['python','success.py'])


#fuction to show the graph
    def showgraph(self):
	x = range(len(self.prn))
 	
	for i in range(len(self.h)):
		plt.plot(x,self.hashmapl[self.h[i]],label=self.h[i])

	plt.grid(True)

	plt.xlabel('Students')
	plt.ylabel('CO Marks')
	plt.title('Marks')

	plt.legend()
	plt.xticks(x,self.prn,rotation=90)
	plt.show()
	


#main fuction
    def main(self):
	self.prn=[]
	#reading data from inpute file
	url=str(self.filenames)
	try:
		wb = open_workbook(url)
	except:
		subprocess.Popen(['python','invalid.py'])
		return

	for s in wb.sheets():
		values = []     #store whole sheet in values variable
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

	for i in range(4,len(values)):
		self.prn.append(values[i][0])
	#call to calculate total of each student
	total=self.cal_total(values) 
	
	#call to find CO's used in paper
	s=self.coset(values)
	self.h=list(s)

	#call to calcuate marks assing to each CO
	cotot=self.hashtot(self.h)
	cotot=self.cal_mekassign(values,cotot)
	#print(cotot)
	#call to create dictionary for hashmaping	
	self.hashmapl=self.hashmap(len(values)-4,s)
	
	#call to calculate COwise marks of each student
	self.hashmapl=self.cal_comrk(values)
	
	
	nm=url.split(".")
	#call to write Output in file
	self.writeonfile(values,total,cotot,nm[0])
	#self.showgraph()


#main()
#import ic_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.showMaximized()
    sys.exit(app.exec_())

