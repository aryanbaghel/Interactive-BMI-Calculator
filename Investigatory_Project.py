from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import math
import csv


root = Tk()
root.title('GetFit')
root.geometry("1600x800+120+120")

filepath = "food.csv"
File = open(filepath)
Reader = csv.reader(File)
Data = list(Reader)
del(Data[0])

list_of_entries = []
for x in list(range(0,len(Data))):
	list_of_entries.append(Data[x][0])

var = StringVar(value=list_of_entries)


def insert():
    Id = entry_id.get()
    name = entry_name.get()
    age = entry_age.get()
    gender = entry_gender.get()
    height = entry_height.get()
    weight = entry_weight.get()
    neck = entry_neck.get()
    hip = entry_hip.get()
    waist = entry_waist.get()
    activity = entry_activity.get()
    goals = entry_goals.get()
    target = entry_target.get()
    difficulty = entry_difficulty.get()
    
    if (Id=="" or name=="" or age=="" or gender=="0" or height=="" or weight=="" or neck=="" or hip=="" or waist=="" or activity=="" or goals=="" or target == "" or difficulty==""):
        MessageBox.showinfo("Insert Status","All Fields are required")
    else:
        connection=mysql.connect(host="localhost", user="root", password="12345678", database="Member_Details")
        cursor=connection.cursor()
        cursor.execute("insert into members values('"+ Id + "','"+ name +"','"+ age +"','"+ gender +"','" + height +"','" + weight +"','" + neck +"','" + hip +"','" + waist +"','"+ activity +"','"+ goals +"','"+ target +"','"+ difficulty +"')")
        cursor.execute("commit")
        
                       
        entry_id.delete(0,'end')
        entry_name.delete(0,'end')
        entry_age.delete(0,'end')                   
        entry_height.delete(0,'end')
        entry_weight.delete(0,'end')
        entry_neck.delete(0,'end')
        entry_hip.delete(0,'end')
        entry_waist.delete(0,'end')  
        entry_target.delete(0,'end')

        genderM.deselect()
        genderF.deselect() 
        activityS.deselect()
        activityL.deselect()
        activityM.deselect()
        activityV.deselect()
        activityE.deselect()   
        goalsWL.deselect()
        goalsWG.deselect()
        goalsWM.deselect()
        difficultyE.deselect()
        difficultyM.deselect()
        difficultyH.deselect()
        difficultyEH.deselect()                 
                       
        MessageBox.showinfo("Insert Status","Inserted Succesfully")               
        connection.close()
        
def delete():
    if (entry_id.get() == ""):
        MessageBox.showinfo("Delete Status","Id is complusary for the data to be deleted")
    else:
        connection=mysql.connect(host="localhost", user="root", password="12345678", database="Member_Details")
        cursor=connection.cursor()
        cursor.execute("delete from members where id ='"+ entry_id.get() +"'")
        cursor.execute("commit")
        
                       
        entry_id.delete(0,'end')
        entry_name.delete(0,'end')
        entry_age.delete(0,'end')                   
        entry_height.delete(0,'end')
        entry_weight.delete(0,'end')
        entry_neck.delete(0,'end')
        entry_hip.delete(0,'end')
        entry_waist.delete(0,'end') 
        entry_target.delete(0,'end')

        genderM.deselect()
        genderF.deselect()
        activityS.deselect()
        activityL.deselect()
        activityM.deselect()
        activityV.deselect()
        activityE.deselect()
        goalsWL.deselect()
        goalsWG.deselect()
        goalsWM.deselect()
        difficultyE.deselect()
        difficultyM.deselect()
        difficultyH.deselect()
        difficultyEH.deselect()
                       
                       
        MessageBox.showinfo("Delete Status","Deleted Succesfully")               
        connection.close()
        
def update():
    Id1 = entry_id.get()
    name2 = entry_name.get()
    age3 = entry_age.get()
    gender9 = entry_gender.get()
    height4 = entry_height.get()
    weight5 = entry_weight.get()
    neck6 = entry_neck.get()
    hip7 = entry_hip.get()
    waist8 = entry_waist.get()
    activity = entry_activity.get()
    goals = entry_goals.get()
    target = entry_target.get()
    difficulty = entry_difficulty.get()
     
    
    if (Id1=="" or name2=="" or age3=="" or gender9=="0" or height4=="" or weight5=="" or neck6=="" or hip7=="" or waist8=="" or activity=="" or goals=="" or target == "" or difficulty==""):
        MessageBox.showinfo("Update Status","All Fields are required")
    else:
        connection = mysql.connect(host="localhost", user="root", password="12345678", database="Member_Details")
        cursor = connection.cursor()
        cursor.execute("update members set name='"+ name2 +"', age='"+ age3 +"',gender='"+ gender9  +"',height='" + height4 +"',weight='" + weight5 +"',neck='" + neck6 +"',hip='" + hip7 +"',waist='" + waist8 +"',activity_level='" + activity +"',fitness_goals='" + goals +"',target_weight='" + target +"',difficulty='" + difficulty +"' where Id='"+ Id1 +"'")
        cursor.execute("commit")
        
                       
        entry_id.delete(0,'end')
        entry_name.delete(0,'end')
        entry_age.delete(0,'end')                   
        entry_height.delete(0,'end')
        entry_weight.delete(0,'end')
        entry_neck.delete(0,'end')
        entry_hip.delete(0,'end')
        entry_waist.delete(0,'end') 
        entry_target.delete(0,'end')

        genderM.deselect()
        genderF.deselect()
        activityS.deselect()
        activityL.deselect()
        activityM.deselect()
        activityV.deselect()
        activityE.deselect()
        goalsWL.deselect()
        goalsWG.deselect()
        goalsWM.deselect()
        difficultyE.deselect()
        difficultyM.deselect()
        difficultyH.deselect()
        difficultyEH.deselect()
                       
                       
        MessageBox.showinfo("Update Status","Updated Succesfully")               
        connection.close()  
        
def show_info():
    if (entry_id.get() == ""):
        MessageBox.showinfo("Fetch Status","Id is complusary for the data to be shown")
    else:
        connection=mysql.connect(host="localhost", user="root", password="12345678", database="Member_Details")
        cursor=connection.cursor()
        cursor.execute("select * from members where Id ='"+ entry_id.get() +"'")
        
        rows=cursor.fetchall()
        
        for row in rows:
            entry_name.insert(0,row[1])
            entry_age.insert(0,row[2])

            if (row[3]=="Male"):               
                genderM.select()
                
            elif (row[3]=="Female"):
                genderF.select() 
                           
            entry_height.insert(0,row[4])
            entry_weight.insert(0,row[5])
            entry_neck.insert(0,row[6])
            entry_hip.insert(0,row[7])
            entry_waist.insert(0,row[8]) 

            if (row[9]=="Sedentary"):
                activityS.select()
            elif (row[9]=="Lightly Active"):
                activityL.select()
            elif (row[9]=="Moderately Active"):
                activityM.select()
            elif (row[9]=="Very Active"):
                activityV.select()
            elif (row[9]=="Extra Active"):
                activityE.select()

            if(row[10]=="Weight Loss"):
                goalsWL.select()
            elif(row[10]=="Weight Gain"):
                goalsWG.select()
            elif(row[10]=="Weight Maintenance"):
                goalsWM.select()

            entry_target.insert(0,row[11])

            if(row[12]=="Easy"):
                difficultyE.select()
            elif(row[12]=="Moderate"):
                difficultyM.select()
            elif(row[12]=="Hard"):
                difficultyH.select()
            elif(row[12]=="Extremely Hard"):
                difficultyEH.select()
            
        
        connection.close()
     

def tellplan():
    def BMIii():
        weight = entry_weight.get()
        height = entry_height.get()
        weight=float(weight)
        height=float(height)
        BMI=((weight)/((height)*(height)))
        if BMI<18:
            list.insert(END,"BMI = " + str(BMI) + " - You are underweight")
        elif BMI>18 and BMI<25:
            list.insert(END,"BMI = " + str(BMI) + " - You are of normal weight")
        elif BMI>25 and BMI<30:
            list.insert(END,"BMI = " + str(BMI) + " - You are overweight")
        elif BMI>30:
            list.insert(END,"BMI = " + str(BMI) + " - You are obese")

        
    
    def bodyfat():
        list.insert(END,"\n")
        flag=0
        if (entry_gender.get() == "Male"):
            weight = entry_weight.get()
            height = entry_height.get()
            neck = entry_neck.get()
            waist = entry_waist.get()

            weight = float(weight)
            height = float(height)
            neck = float(neck)
            waist = float(waist)
             

            meas=math.log((waist-neck),10)
            meas1=math.log(height*100,10)
            bf=(495/(1.0324-(0.19077*(meas))+(0.15456*(meas1))))-450
            list.insert(END, "Your body fat percentage is " + str(bf) + "%")
            if bf>1 and bf<10:
                list.insert(END, "You are chiseled")
                flag=0
            if bf>10 and bf<15:
                list.insert(END, "You have an athletic physique")
                flag=0
            if bf>15 and bf<22.5:
                list.insert(END, "You have an average  physique")
                flag=0
            if bf>22.5 and bf<30:
                list.insert(END, "You are overweight")
                flag=0
            if bf>30 and bf<100:
                list.insert(END, "You are obese")
                flag=0
            if bf<0 or bf>99.9:
                list.insert(END, "Please enter correct measurements")
                flag=1
        elif (entry_gender.get() == "Female"):
            weight = entry_weight.get()
            height = entry_height.get()
            neck = entry_neck.get()
            hip = entry_hip.get()
            waist = entry_waist.get()

            weight = float(weight)
            height = float(height)
            neck = float(neck)
            hip = float(hip)
            waist = float(waist)
            
            meas=math.log((hip+waist-neck),10)
            meas1=math.log(height*100,10)
            bf=(495/(1.29579-(0.35004*(meas))+(0.22100*(meas1))))-450
            list.insert(END, "Your body fat percentage is" + str(bf) + "%")
            if bf>1 and bf<15:
                list.insert(END, "You are chiseled")
                flag=0
            if bf>15 and bf<22.5:
                list.insert(END, "You have an athletic physique")
                flag=0
            if bf>22.5 and bf<27.5:
                list.insert(END, "You have an average  physique")
                flag=0
            if bf>27.5 and bf<35:
                list.insert(END, "You are overweight")
                flag=0
            if bf>35 and bf<99.9:
                list.insert(END, "You are obese")
                flag=0
            if bf<0 or bf>99.9:
                list.insert(END, "Please enter correct measurements")
                flag=1


    def totdailee():
        
        weight = entry_weight.get()
        height = entry_height.get()
        gender = entry_gender.get()
        activity = entry_activity.get()
        age = entry_age.get()
        goals = entry_goals.get()
        target = entry_target.get()
        difficulty = entry_difficulty.get()

        weight = float(weight)
        height = float(height)
        age = int(age)
        target = float(target)
        
        
        if (activity == "Sedentary"):
            act=1.2
        elif (activity == "Lightly Active"):
            act=1.375
        elif (activity == "Moderately Active"):
            act=1.55
        elif (activity == "Very Active"):
            act=1.725
        elif (activity == "Extra Active"):
            act=1.9
        list.insert(END,"\n")
        if (gender == "Male"):
            BMR=(10*weight)+((6.25*height)*100)-(5*age)+5
            TDEE=(BMR*act)
            list.insert(END, "the total calories you should consume are : " + str(TDEE) +" KCAL")
        elif (gender == "Female"):
            BMR=(10*weight)+((6.25*height)*100)-(5*age)-161
            TDEE=BMR*act
            list.insert(END, "the total calories you should consume are : " + str(TDEE) + " KCAL")
        if (goals=="Weight Loss"):

            if (difficulty=="Easy"):
                reqdcal=TDEE-300
                time=((weight-target)*7800)/(300*7)
                list.insert(END, "You need to consume " + str(reqdcal) + " KCAL everyday")
                list.insert(END, "You will achieve your target weight in " + str(int(time)) + " weeks")
            elif (difficulty=="Moderate"):
                reqdcal=TDEE-500
                time=((weight-target)*7800)/(500*7)
                list.insert(END, "You need to consume " + str(reqdcal) + " KCAL everyday")
                list.insert(END, "You will achieve your target weight in " + str(int(time)) + " weeks")
            elif (difficulty=="Hard"):
                reqdcal=TDEE-700
                time=((weight-target)*7800)/(700*7)
                list.insert(END, "You need to consume " + str(reqdcal) + " KCAL everyday")
                list.insert(END, "You will achieve your target weight in " + str(int(time)) + " weeks")
            elif (difficulty=="Extremely Hard"):
                reqdcal=TDEE-900
                time=((weight-target)*7800)/(900*7)
                list.insert(END, "You need to consume " + str(reqdcal) + " KCAL everyday")
                list.insert(END, "You will achieve your target weight in " + str(int(time)) + " weeks")
        elif (goals=="Weight Gain"):
            reqdcal=TDEE+700
            time=((target-weight)*7000)/(700*7)
            list.insert(END, "You need to consume " + str(reqdcal) + " KCAL everyday")
            list.insert(END, "You will achieve your target weight in " + str(int(time)) + " weeks")
        elif (goals=="Weight Maintenance"):
            list.insert(END, "You need to consume " + str(TDEE) + " KCAL everyday")
    list.insert(END,"\n")
            
    BMIii()
    bodyfat()
    totdailee()

    entry_id.delete(0,'end')
    entry_name.delete(0,'end')
    entry_age.delete(0,'end')                   
    entry_height.delete(0,'end')
    entry_weight.delete(0,'end')
    entry_neck.delete(0,'end')
    entry_hip.delete(0,'end')
    entry_waist.delete(0,'end')
    entry_target.delete(0,'end')

    genderM.deselect()
    genderF.deselect()
    activityS.deselect()
    activityL.deselect()
    activityM.deselect()
    activityV.deselect()
    activityE.deselect()
    goalsWL.deselect()
    goalsWG.deselect()
    goalsWM.deselect()
    difficultyE.deselect()
    difficultyM.deselect()
    difficultyH.deselect()
    difficultyEH.deselect()


def show_nutrient():
    index = list1.curselection()[0]
    carbohydrates1.config(text = Data[index][1])
    proteins1.config(text = Data[index][2])
    fats1.config(text = Data[index][3])
	
    return None


Id = Label(root,text='Enter your id : ',font=('bold',15))
name = Label(root,text='Enter your name :',font=('bold',15))
age = Label(root,text='Enter your age :',font=('bold',15))
height = Label(root,text='Enter your height(in m) :',font=('bold',15))
weight = Label(root,text='Enter your weight(in kg) :',font=('bold',15))
neck = Label(root,text="Enter your neck measurements(in cm) : ",font=('bold',15))
hip = Label(root,text="Enter your hip measurements(in cm) : ",font=('bold',15))
waist = Label(root,text="Enter your waist measurements(in cm) : ",font=('bold',15))
target = Label(root,text="Enter your target weight : ",font=('bold',15))

gender = Label(root,text='Select you gender :',font=('bold',15))
activity = Label(root,text="Select your activity level :",font=('bold',15))
goals = Label(root,text="Select your fitness goal :",font=('bold',15))
difficulty = Label(root,text="Select the difficulty :",font=('bold',15))

proteins = Label(root,text='Proteins :',font=('bold',15))
carbohydrates = Label(root,text='Carbohydrates :',font=('bold',15))
fats = Label(root,text='Fats :',font=('bold',15))
proteins1 = Label(root,text="",font=('bold',15))
carbohydrates1 = Label(root,text="",font=('bold',15))
fats1 = Label(root,text="",font=('bold',15))




Id.place(x=20,y=30)
name.place(x=20,y=60)
age.place(x=20,y=90)
height.place(x=20,y=120)
weight.place(x=20,y=150)
neck.place(x=20,y=180)
hip.place(x=20,y=210)
waist.place(x=20,y=240)
target.place(x=20,y=508)

gender.place(x=20,y=270)
activity.place(x=20,y=318)
goals.place(x=20,y=433)
difficulty.place(x=20,y=544)

fats.place(x=1125,y=440)
proteins.place(x=1125,y=490)
carbohydrates.place(x=1125,y=540)
fats1.place(x=1170,y=440)
proteins1.place(x=1200,y=490)
carbohydrates1.place(x=1250,y=540)


entry_gender=StringVar()
entry_activity=StringVar()
entry_goals=StringVar()
entry_difficulty=StringVar()


genderM = Checkbutton(root,text="Male",variable=entry_gender,onvalue="Male",font=('bold',15))
genderF = Checkbutton(root,text="Female",variable=entry_gender,onvalue="Female",font=('bold',15))
activityS = Checkbutton(root,text="Sedentary (little or no exercise, desk job)",variable=entry_activity,onvalue="Sedentary",font=('bold',15))
activityL = Checkbutton(root,text="Lightly Active (light exercise/ sports 1-3 days/week)",variable=entry_activity,onvalue="Lightly Active",font=('bold',15))
activityM = Checkbutton(root,text="Moderately Active (moderate exercise/ sports 6-7 days/week)",variable=entry_activity,onvalue="Moderately Active",font=('bold',15))
activityV = Checkbutton(root,text="Very Active (hard exercise every day, or exercising 2 xs/day)",variable=entry_activity,onvalue="Very Active",font=('bold',15))
activityE = Checkbutton(root,text="Extra Active (hard exercise 2 or more times per day)",variable=entry_activity,onvalue="Extra Active",font=('bold',15))
goalsWL = Checkbutton(root,text="Weight Loss",variable=entry_goals,onvalue="Weight Loss",font=('bold',15))
goalsWG = Checkbutton(root,text="Weight Gain",variable=entry_goals,onvalue="Weight Gain",font=('bold',15))
goalsWM = Checkbutton(root,text="Weight Maintenance",variable=entry_goals,onvalue="Weight Maintenance",font=('bold',15))
difficultyE = Checkbutton(root,text="Easy",variable=entry_difficulty,onvalue="Easy",font=('bold',15))
difficultyM = Checkbutton(root,text="Moderate",variable=entry_difficulty,onvalue="Moderate",font=('bold',15))
difficultyH = Checkbutton(root,text="Hard",variable=entry_difficulty,onvalue="Hard",font=('bold',15))
difficultyEH = Checkbutton(root,text="Extremely Hard",variable=entry_difficulty,onvalue="Extremely Hard",font=('bold',15))


genderM.deselect()
genderF.deselect()
activityS.deselect()
activityL.deselect()
activityM.deselect()
activityV.deselect()
activityE.deselect()
goalsWL.deselect()
goalsWG.deselect()
goalsWM.deselect()
difficultyE.deselect()
difficultyM.deselect()
difficultyH.deselect()
difficultyEH.deselect()


genderM.place(x=300,y=271)
genderF.place(x=300,y=291)
activityS.place(x=300,y=321)
activityL.place(x=300,y=341)
activityM.place(x=300,y=361)
activityV.place(x=300,y=381)
activityE.place(x=300,y=401)
goalsWL.place(x=300,y=433)
goalsWG.place(x=300,y=453)
goalsWM.place(x=300,y=473)
difficultyE.place(x=300,y=544)
difficultyM.place(x=300,y=564)
difficultyH.place(x=300,y=584)
difficultyEH.place(x=300,y=604)

entry_id = Entry()
entry_name = Entry()
entry_age = Entry()
entry_height = Entry()
entry_weight = Entry()
entry_neck = Entry()
entry_height = Entry()
entry_waist = Entry()
entry_hip = Entry()
entry_target = Entry()


entry_id.place(x=300,y=30)
entry_name.place(x=300,y=60)
entry_age.place(x=300,y=90)
entry_height.place(x=300,y=120)
entry_weight.place(x=300,y=150)
entry_neck.place(x=300,y=180)
entry_hip.place(x=300,y=210)
entry_waist.place(x=300,y=240)
entry_target.place(x=300,y=508)


insert = Button(root,text='Insert',font =("italic",15),bg="white",command=insert)
delete = Button(root,text='Delete',font =("italic",15),bg="white",command=delete)
update = Button(root,text='Update',font =("italic",15),bg="white",command=update)
show_info = Button(root,text="Show Details",font=("italic",15),bg="white",command=show_info)
tell_plan = Button(root,text="Tell Plan",font=("italic",15),bg="white",command=tellplan)
show_nutrient = Button(root,text="Show Nutrient Value",font=("italic",15),bg="white",command=show_nutrient)

insert.place(x=20,y=660)
delete.place(x=70,y=660)
update.place(x=125,y=660)
show_info.place(x=185,y=660)
tell_plan.place(x=20,y=695)
show_nutrient.place(x=94,y=695)

list = Listbox(root,width=73,height=21)
list1 = Listbox(root,listvariable=var,width=35,height=21)


list.place(x=768,y=22)
list1.place(x=768,y=398)


root.mainloop()


# Code for creating tabel and database in mysql :

#     create database Member_Details
#     use Member_Details;
#     create table members(Id varchar(5) primary key,name varchar(40),age int(3),gender varchar(20),height decimal(6,2),weight decimal(5,2),neck decimal(5,2),hip decimal(5,2),waist decimal(6,2));

#     ALTER TABLE Members 
#     Add activity_level varchar(40);
#     ALTER TABLE Members 
#     Add fitness_goals varchar(40);
#     ALTER TABLE Members 
#     Add target_weight decimal(6,2);
#     ALTER TABLE Members 
#     Add difficulty varchar(40);



