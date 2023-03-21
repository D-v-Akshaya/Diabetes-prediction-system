from tkinter import *
from tkinter.font import Font
from PIL import ImageTk,Image
import mdata_set_models as d

root= Tk()
root.title("Home page")
root['bg']='#D8DEE7'
#f= ('Times roman',20)


class Fun_frams:
    def femaleFun(self,parent=root):
        def predicte():
            i=False
            if i==False:
                try:
                    preg=int(pregnancies.get())
                    glu=float(glucose.get())
                    BP =float(bp.get())
                    sk=float(skinthickness.get())
                    ins=float(insulin.get())
                    h=int(height.get())
                    w=int(weight.get())
                    bmi=(int(w)/(int(h)*int(h)))*10000
                    diaprefun=float(diapre.get())
                    a=int(age.get()) 
                    
                    i=True
                except:
                    i=False
                    warningl=Label(f3,text='''Enter Glucose level,
                        insulin level,
                        Blood pressure
                             & 
                        Skin Thickness in integer please!!!!''',bg='red')
                    warningl.grid(row=0,column=6,rowspan=5)
                    glucose.delete(0,END)
                    insulin.delete(0,END)
                    bp.delete(0,END)
                    skinthickness.delete(0,END)
                else:
                    
                    predic=d.Data_analysis()
                    outcome=predic.predicte(preg,glu,BP,sk,ins,bmi,diaprefun,a)
                    if int(outcome)==1:
                        outcomel=Label(f3,text=f'''Sorry
                        There are 77.2728% chanses that {name.get()} ,
                        you are Diabetic''',font=('itallic',10))
                        outcomel.grid(row=10,column=2,columnspan=4)
                    else:
                        outcomel=Label(f3,text=f'''CONGRATULATION!!!!!
                        There are 77.2728%  Chanses that {name.get()} ,
                        You are Non-Diabetic''',font=('itallic',10))
                        outcomel.grid(row=10,column=2,columnspan=4)
        def clear_fun():
            name.delete(0,END)
            age.delete(0,END)
            height.delete(0,END)
            weight.delete(0,END)
            g=1
            f3.destroy()




        f3=Frame(parent,bg='#E6DBAC')
        f3.grid(row=3,column=1, columnspan=2,padx=5,pady=5)
        #No.of pregnencies
        pregl=Label(f3,text='No. of pregnancies :')
        pregl.grid(row=0,column=2)
        pregnancies=Entry(f3)
        pregnancies.grid(row=0,column=3)
        #glucose 
        glucosel=Label(f3,text='Glucose level :')
        glucosel.grid(row=1,column=2)
        glucose=Entry(f3)
        glucose.grid(row=1,column=3)
        #insulin
        insulinl=Label(f3,text='Insulin level:')
        insulinl.grid(row=2,column=2)
        insulin=Entry(f3)
        insulin.grid(row=2,column=3)
        #calculating BMI
        w = (weight.get())
        h = (height.get())
        bmi=(int(w)/(int(h)*int(h)))*10000
        Label(f3,text=f'Calculated BMI from given height and weight is {bmi} ').grid(row=3,column=2,columnspan=3)
        #bloodpressure
        bpl=Label(f3,text='Blood Pressure:')
        bpl.grid(row=5,column=2)
        bp=Entry(f3)
        bp.grid(row=5,column=3)
        #skin thickness
        skinthicknessl=Label(f3,text='Skin thickness :')
        skinthicknessl.grid(row=7,column=2)
        skinthickness=Entry(f3)
        skinthickness.grid(row=7,column=3)
        #Diabetes predegree function
        diaprel=Label(f3,text='Daibetes predegree function')
        diaprel.grid(row=7,column=4)
        diapre=Entry(f3)
        diapre.grid(row=7,column=5)
        #botton Calculate
        calculate=Button(f3,text="Predict",command=predicte)
        calculate.grid(row=9,column=2,pady=20)
        #Clear botton
        clear=Button(f3,text="Clear",command=clear_fun)
        clear.grid(row=9,column=4)

    def maleFun(self,parent=root):
        f4=Frame(parent,bg='#800000')
        f4.grid(row=3,column=1, columnspan=2,padx=5,pady=5)
        Label(f4,text="    ",bg='#800000').grid(row=0,column=0)
        Label(f4,text='''#######Sorry##########
         This prediction system is only for female
          Kindly Exit or Clear and tryagain for any female ''',font=('itallic',10)).grid(row=1,column=1,columnspan=3,rowspan=4)
        Label(f4,text=''' We may sugess that if you have below mentioned symtomes
        please visite a doctor:
         * urinate often at 
         * are very thirsty
         * lose weight without trying
         * are very hungry
         * have blurry vision
         * have numb or tingling hands or feet
         * feel very tired
         * have very dry skin
         * have sores that heal slowly
         * have more infection than usual''',justify='left').grid(row=5,column=1)
        def clear_fun():
           name.delete(0,END)
           age.delete(0,END)
           height.delete(0,END)
           weight.delete(0,END)
           g=1
           f4.destroy()
        clear=Button(f4,text="Clear",command=clear_fun)
        clear.grid(row=6,column=4)
        


def next1_fun():
    i=False
    if i==False:
        try:
            int(age.get())
            int(height.get())
            int(weight.get())
            i=True
        except:
            i=False
            warningl=Label(f1,text='''Enter Age ,
                Height , Weight in integer please!!!!''',bg='red')
            warningl.grid(row=8,column=4)
            age.delete(0,END)
            height.delete(0,END)
            weight.delete(0,END)
        else:
            if g.get()==1:
                f=Fun_frams()
                f.maleFun()
            else:
                f=Fun_frams()
                f.femaleFun()
            

                
        

h1=Label(root, text="\t\t\t Welcome to Daibetes prediction !!!!!\t\t\t", font=('time roman',20),bg='#ffc0cb')
h1.grid(row=0,column=0,columnspan=4)
f0=Frame(root,bg='#A52A2A')
f0.grid(row=2,column=0,rowspan=2)
infol=Label(f0,text='''DIABETES
 Diabetes is a very common disease in the world.
 But people may never realize, how did they get diabetes
 and what will happen to them and what will they go through. 
 It may not be your problem but you have to show respect and 
 care for the one who has diabetes. It can help them and also 
 benefited you to know more about it and have a better 
 understanding of it. Diabetes is a metabolic disorder which 
 is identified by the high blood sugar level. Increased blood 
 glucose level damages the vital organs as well as other organs of the human’s
 body causing other potential health ailments.

 Types of Diabetes
 Diabetes  Mellitus can be described in two types:

 1) Type 1 \n
   Diabetes Mellitus is classified by a deficiency of insulin in the blood.
   The deficiency is caused by the loss of insulin-producing beta cells in 
   the pancreas. This type of diabetes is found more commonly in children. 
   An abnormally high or low blood sugar level is a characteristic of this 
   type of Diabetes.
   Most patients of type 1 diabetes require regular administration of insulin.
   Type 1 diabetes is also hereditary from your parents. 
   You are most likely to have type 1 diabetes if any of your parents had it. 
   Frequent urination, thirst, weight loss, 
   and constant hunger are common symptoms of this.
 
 2) Type 2 
   Diabetes Mellitus is characterized by the inefficiency of body tissues 
   to effectively respond to insulin because of this it may be combined by 
   insulin deficiency. Type 2 diabetes mellitus is the most common type 
   of diabetes in people.
   People with type 2 diabetes mellitus take medicines to improve the body’s 
   responsiveness to insulin or to reduce the glucose produced by the liver. 
   This type of diabetes mellitus is generally attributed to lifestyle factors 
   like – obesity, low physical activity, irregular and unhealthy diet, excess 
   consumption of sugar in the form of sweets, drinks, etc.
''',justify='left')
infol.pack()


f1=Frame(root,bg="black",height=800)
f1.grid(row=2,column=1, columnspan=2,padx=5,pady=5)
Label(f1,text=" ",bg='black').grid(row=0)
Label(f1,text="Enter the Information  ",bg='black',font=('bold'),foreground='white').grid(row=1,column=0,columnspan=2)
Label(f1,text=" ",bg='black').grid(row=2)
Label(f1,text=" ",bg='black').grid(row=3)
#Name 
namel=Label(f1,text="Enter your name : ")
namel.grid(row=4,column=0,pady=5)
name=Entry(f1,width=20)
name.grid(row=4,column=1,pady=5)
#Age
agel=Label(f1,text='Enter the age : ')
agel.grid(row=4,column=3,pady=5)
age = Entry(f1,width=10)
age.grid(row=4,column=4,pady=5)
#Gender
gender=Label(f1,text="Gender :",width=10)
gender.grid(row=8,column=0,padx=0,pady=5)
g = IntVar()
male = Radiobutton(f1, text="Male", variable=g, value=1,width=5)
male.grid(row=8,column=1,padx=0,pady=5)
female = Radiobutton(f1, text="Female",variable=g, value=2,width=5)
female.grid(row=8,column=2,padx=0,pady=5)
#BMI
heightl=Label(f1,text='Height :')
heightl.grid(row=9,column=0)
height=Entry(f1,width=10)
height.grid(row=9,column=1)
Label(f1,text='cm',width=2).grid(row=9,column=2)
weightl=Label(f1,text='Weight :')
weightl.grid(row=9,column=3)
weight=Entry(f1,width=10)
weight.grid(row=9,column=4)
Label(f1,text='kg',width=2).grid(row=9,column=5)
Label(f1,text=" ",bg='black').grid(row=10)
Label(f1,text=" ",bg='black').grid(row=11)
Label(f1,text=" ",bg='black').grid(row=12)

next1=Button(f1,text="next",command=next1_fun,font=('bold'))
next1.grid(row=14,column=2,pady=20)

f2=Frame(root,bg='pink')
f2.grid(row=2,column=3,rowspan=2)
Label(f2,text='''The Pie Diagram of Outcomes Diabetes Diagnosis ''',font='bold').grid()
image1 = Image.open(r"pie.png")
test = ImageTk.PhotoImage(image1)
label1 =Label(f2,image=test).grid()
Label(f2,text='''Recomemded Doctores
 * Dr.Ram kundra                                                              .
                  Mobile:0000009780
 * Dr.Geeta kumar
                  Mobile:0000001234 
 * Dr.Sachi Agarval
                  Mobile:0000005678
 * Dr.Neha Jadhav
                  Mobile:0000009780
 * Dr.Sneha Salunkhe
                  Mobile:0000001234 
 * Dr.Sahana Yusif
                  Mobile:0000005678
''',foreground="blue",justify='left').grid()

vis=d.Data_analysis()
#LabelFrame(f2,text=vis.pie())

Button(root,text='Exit',command=root.destroy).grid(row=4,column=2)


root.mainloop()

