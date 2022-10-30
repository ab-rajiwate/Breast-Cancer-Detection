#from PIL import Image, ImageTk
from processing import single_result, multiple_result
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox as mbox
def main_screen():
	root=Tk()
	root.title("Breast Cancer Detection Program")
	width, height = root.winfo_screenwidth(), root.winfo_screenheight()
	root.geometry('%dx%d+0+0' % (width,height))
	#root.geometry("1250x700+40+10")
	root.minsize(400,400)
	root.configure(bg='pink')
	s=Label(text="Breast Cancer Detection",bg="white",fg="black",padx=70,pady=20,font=("Calibri(Body)",20,"bold"),relief=GROOVE,borderwidth=3)
	s.grid(rowspan=1,columnspan=1,row=4,column=3,padx=300)

	#Functions
	def show_help():
		help_screen()

	def predict_result():
		if Address['text'] != "None":
			show_Results['text'] = multiple_result(Address['text'])
			Address['text'] = 'None'

		else:
			data = []
			data.append(int(Clump_ThicknessE.get()))
			data.append(int(Uniformity_of_Cell_SizeE.get()))
			data.append(int(Uniformity_of_Cell_ShapeE.get()))
			data.append(int(Marginal_AdhesionE.get()))
			data.append(int(Single_Epithelial_Cell_SizeE.get()))
			data.append(int(Bare_NucleiE.get()))
			data.append(int(Bland_ChromatinE.get()))
			data.append(int(Normal_NucleoliE.get()))
			data.append(int(MitosesE.get()))

			if max(data) >= 11 or min(data) <= 0:
				mbox.showinfo("ALERT","The inputed data is out of specified range")
			else:
				val = single_result(data)
				show_Results['text'] = "ID: "+str(IDE.get()) + val 



	
	def upload_file():
		root.filename = filedialog.askopenfilename(initialdir='/home/ab_rajiwate/Documents/', title= 'Select a CSV file',filetypes=(["csv files","*.csv"],))
		if len(root.filename) != 0:
			Address['text'] = root.filename

	#image=Image.open("BreastCancerRibbon.jpg")
	#image = image.resize((400, 200), Image.ANTIALIAS)
	#photo=ImageTk.PhotoImage(image)
	#ilabel=Label(image=photo)
	#ilabel.grid(row=0,column=3)

	Clump_Thickness=Label(root,text="Clump Thickness 1-10",font=("Calibri(Body)",10,"bold"),bg = 'pink')
	Uniformity_of_Cell_Size=Label(root,text="Uniformity of Cell Size 1-10",font=("Calibri(Body)",10,"bold"),bg = 'pink')
	Uniformity_of_Cell_Shape=Label(root,text="Uniformity of Cell Shape 1-10",font=("Calibri(Body)",10,"bold"),bg = 'pink')
	Marginal_Adhesion=Label(root,text="Marginal Adhesion 1-10",font=("Calibri(Body)",10,"bold"),bg = 'pink')
	Single_Epithelial_Cell_Size=Label(root,text="Single Epithelial Cell Size 1-10",font=("Calibri(Body)",10,"bold"),bg = 'pink')
	Bare_Nuclei=Label(root,text="Bare Nuclei 1-10",font=("Calibri(Body)",10,"bold"),bg = 'pink')
	Bland_Chromatin=Label(root,text="Bland Chromatin 1-10",font=("Calibri(Body)",10,"bold"),bg = 'pink')
	Normal_Nucleoli=Label(root,text="Normal Nucleoli 1-10",font=("Calibri(Body)",10,"bold"),bg = 'pink')
	Mitoses=Label(root,text="Mitoses 1-10",font=("Calibri(Body)",10,"bold"),bg = 'pink')
	ID=Label(root,text="Patient/Sample ID",font=("Calibri(Body)",10,"bold"),bg = 'pink')
	Address = Label(root,text="None",font=("Calibri(Body)",10,"bold"),bg = 'pink')

	#Grid
	Clump_Thickness.grid(row=1,column=0,pady=10,padx=0)
	Uniformity_of_Cell_Size.grid(row=2,column=0,pady=10,padx=0)
	Uniformity_of_Cell_Shape.grid(row=3,column=0,pady=10,padx=0)
	Marginal_Adhesion.grid(row=4,column=0,pady=10,padx=0)
	Single_Epithelial_Cell_Size.grid(row=5,column=0,pady=10,padx=0)
	Bare_Nuclei.grid(row=6,column=0,pady=10,padx=0)
	Bland_Chromatin.grid(row=7,column=0,pady=10,padx=0)
	Normal_Nucleoli.grid(row=8,column=0,pady=10,padx=0)
	Mitoses.grid(row=9,column=0,pady=10,padx=0)
	ID.grid(row=10,column=0,pady=10,padx=0)
	Address.grid(row=11,column=1,pady=10,padx=0)


	#Variables
	Clump_Thicknessv=IntVar()
	Uniformity_of_Cell_Sizev=IntVar()
	Uniformity_of_Cell_Shapev=IntVar()
	Marginal_Adhesionv=IntVar()
	Single_Epithelial_Cell_Sizev=IntVar()
	Bare_Nucleiv=IntVar()
	Bland_Chromatinv=IntVar()
	Normal_Nucleoliv=IntVar()
	Mitosesv=IntVar()
	IDv = IntVar()



	#Entry
	Clump_ThicknessE=Entry(root,textvariable=Clump_Thicknessv,font=("Calibri(Body)",10,"bold"))
	Uniformity_of_Cell_SizeE=Entry(root,textvariable=Uniformity_of_Cell_Sizev,font=("Calibri(Body)",10,"bold"))
	Uniformity_of_Cell_ShapeE=Entry(root,textvariable=Uniformity_of_Cell_Shapev,font=("Calibri(Body)",10,"bold"))
	Marginal_AdhesionE=Entry(root,textvariable=Marginal_Adhesionv,font=("Calibri(Body)",10,"bold"))
	Single_Epithelial_Cell_SizeE=Entry(root,textvariable=Single_Epithelial_Cell_Sizev,font=("Calibri(Body)",10,"bold"))
	Bare_NucleiE=Entry(root,textvariable=Bare_Nucleiv,font=("Calibri(Body)",10,"bold"))
	Bland_ChromatinE=Entry(root,textvariable=Bland_Chromatinv,font=("Calibri(Body)",10,"bold"))
	Normal_NucleoliE=Entry(root,textvariable=Normal_Nucleoliv,font=("Calibri(Body)",10,"bold"))
	MitosesE=Entry(root,textvariable=Mitosesv,font=("Calibri(Body)",10,"bold"))
	IDE = Entry(root,textvariable=IDv,font=("Calibri(Body)",10,"bold"))



	Clump_ThicknessE.grid(row=1,column=1)
	Uniformity_of_Cell_SizeE.grid(row=2,column=1)
	Uniformity_of_Cell_ShapeE.grid(row=3,column=1)
	Marginal_AdhesionE.grid(row=4,column=1)
	Single_Epithelial_Cell_SizeE.grid(row=5,column=1)
	Bare_NucleiE.grid(row=6,column=1)
	Bland_ChromatinE.grid(row=7,column=1)
	Normal_NucleoliE.grid(row=8,column=1)
	MitosesE.grid(row=9,column=1)
	IDE.grid(row=10,column=1)

	Results=Label(root,text="Results",font=("Calibri(Body)",10,"bold"), bg = 'pink')
	Results.grid(row=12,column=0)
	show_Results = Label(root,text='',font=("Calibri(Body)",10,"bold"), bg = 'pink')
	show_Results.grid(row=13,column=0)

	#Button
	Button(text="Upload File",command = upload_file ,font=("Calibri(Body)",10,"bold")).grid(row=11,column=0,pady=10)
	Button(text="Predict",command = predict_result,font=("Calibri(Body)",10,"bold")).grid(column=3,pady=10)
	Button(text="Help",command=show_help,font=("Calibri(Body)",10,"bold")).grid(column=3,pady=10)
	Button(text="Quit",command=quit,font=("Calibri(Body)",10,"bold")).grid(column=3,pady=10)
	root.mainloop()

def help_screen():
	sub_root=Tk()
	sub_root.title("Breast Cancer Detection Program")
	sub_root.geometry("1100x550+150+100")
	sub_root.minsize(400,400)
	sub_root.configure(bg='grey')

	Label(sub_root,text='''Welcome. This Help/Instruction tab will quickly and efficiently solve all your doubts and guide you on how to format a data in CSV [Comma Seperated Value] file.
	\n1. First of all, you will need to open a Excel file on your system..
	\n2. After opening the file it is "imperative" to leave  the first row blank. Never fill any data in first row.
	\n3. The data that is inputed must be in the order that is defined as follows: 
		\na. Column 1 : Patient Name or Patient ID or Sample ID
		\nb. Column 2 : Clump Thickness [Range 1-10]
		\nc. Column 3 : Uniformity of Cell Size [Range 1-10]
		\nd. Column 4 : Marginal Adhesion [Range 1-10]
		\ne. Column 5 : Single Epithelial Cell Size [Range 1-10]
		\nf. Column 6 : Bare Nuclei [Range 1-10]
		\ng. Column 7 : Bland Chromatin [Range 1-10]
		\nh. Column 8 : Normal Nucleoli [Range 1-10]
		\ni. Column 9 : Mitoses [Range 1-10]
	\n4. After you have inserted all the data, save the file as .csv file.
	\n5. Upload the file and click on the "Predict" button. The application will preidict the given values and create a new csv file with the results stored into it.
	''').pack()
if __name__ == '__main__':
	main_screen()