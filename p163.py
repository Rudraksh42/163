from tkinter import *
from tkinter import messagebox 

root = Tk()
root.geometry("900x900")
root.configure(bg = "sky blue")
root.title("If and else")

q1_radiobutton = StringVar(value = "0")
q1_label = Label(root , text = "Are you having Chest pain, chest tightness, chest pressure and chest discomfort (angina) " , bg = "sky blue", font= 15)
q1_label.pack()
q1_yes = Radiobutton(root , variable =  q1_radiobutton , text= "yes"   ,value = "yes" , bg = "sky blue", font= 15)
q1_yes.pack()
q1_no = Radiobutton(root , variable =  q1_radiobutton , text= "no"   ,value = "no" , bg = "sky blue", font= 15)
q1_no.pack()

q2_radiobutton = StringVar(value = "0")
q2_label = Label(root , text = "Are you having Shortness of breath." , bg = "sky blue", font= 15)
q2_label.pack()
q2_yes = Radiobutton(root , variable =  q2_radiobutton , text= "yes"   ,value = "yes" , bg = "sky blue", font= 15)
q2_yes.pack()
q2_no = Radiobutton(root , variable =  q2_radiobutton , text= "no"   ,value = "no" , bg = "sky blue", font= 15)
q2_no.pack()

q3_radiobutton = StringVar(value = "0")
q3_label = Label(root , text = "Are you having Pain in the neck, jaw, throat, upper belly area or back." , bg = "sky blue" , font= 15)
q3_label.pack()
q3_yes = Radiobutton(root , variable =  q3_radiobutton , text= "yes"   ,value = "yes" , bg = "sky blue", font= 15)
q3_yes.pack()
q3_no = Radiobutton(root , variable =  q3_radiobutton , text= "no"   ,value = "no" , bg = "sky blue", font= 15)
q3_no.pack()

q4_radiobutton = StringVar(value = "0")
q4_label = Label(root , text = "Are you having Pain, numbness, weakness or coldness in the legs or arms if the blood vessels in those body areas are narrowed." , bg = "sky blue", font= 15)
q4_label.pack()
q4_yes = Radiobutton(root , variable =  q4_radiobutton , text= "yes"   ,value = "yes" , bg = "sky blue", font= 15)
q4_yes.pack()
q4_no  = Radiobutton(root , variable =  q4_radiobutton , text= "no"   ,value = "no" , bg = "sky blue", font= 15)
q4_no.pack()

q5_radiobutton = StringVar(value = "0")
q5_label = Label(root , text = "Are you having Fainting (syncope) or near fainting or Dizziness." , bg = "sky blue", font= 15)
q5_label.pack()
q5_yes = Radiobutton(root , variable =  q5_radiobutton , text= "yes"   ,value = "yes" , bg = "sky blue", font= 15)
q5_yes.pack()
q5_no  = Radiobutton(root , variable =  q5_radiobutton , text= "no"   ,value = "no" , bg = "sky blue", font= 15)
q5_no.pack()




def hospital():
    score = 0
    if q1_radiobutton.get() == "yes":
        score = score + 20
        print(score)
        
    if q2_radiobutton.get() == "yes":
        score = score + 20
        print(score)
        
    if q3_radiobutton.get() == "yes":
        score = score + 20
        print(score)
        
    if q4_radiobutton.get() == "yes":
            score = score + 20
            print(score)
            
    if q5_radiobutton.get() == "yes":
            score = score + 20
            print(score)
        
    if score <= 20:
        messagebox.showinfo("Report", "You Dont Need To Visit A Doctor")
    elif score >20 and score <=40 :
        messagebox.showinfo("Report", "You Perhapes Visit a Doctor")
    else:
        messagebox.showinfo("Report", "You Should Definately Visit A Doctor")
        
        
btn = Button(root  , text = "Click me to Generate the report" , bg = "Sky Blue" , command = hospital)  
btn.pack()   
root.mainloop()