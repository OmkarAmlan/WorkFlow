import os
import init
import login as lg
import cipher
import tasks
import time
import pandas as pd
from tkinter import *
from PIL import ImageTk, Image
import customtkinter as ctk
from CTkTable import *

file_path = 'secret.key'
if os.path.exists(file_path)==False:
    init.generate_key()

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")
root=ctk.CTk()
root.title("WorkFlow")
#Add custom icon here
# root.iconbitmap("favicon.ico")
root.geometry("750x500")
root.wm_attributes('-transparentcolor','black')

bg = PhotoImage(file = "Assets/bg.png") 
labelbg = ctk.CTkLabel( root,text="", image = bg) 
labelbg.pack(fill="both") 

frame=ctk.CTkFrame(root)
frame.place(relx=0.315,rely=0.25)

def landing():
    name_var=ctk.StringVar()
    passw_var=ctk.StringVar()
    
    def signup():
        username=name_var.get()
        password=cipher.cipher(passw_var.get())
        name_var.set("")
        passw_var.set("")
        action = lg.create_account(username,password)
        create_success_label=ctk.CTkLabel(frame,text='Account Created Successfully!',font=('calibre',10, 'bold'))
        create_nameerror_label=ctk.CTkLabel(frame,text='Username is not available!',font=('calibre',10, 'bold'))
        create_passerror_label=ctk.CTkLabel(frame,text='Weak Password!',font=('calibre',10, 'bold'))
        if(action==0):
            create_passerror_label.grid(row=3)
            create_passerror_label.after(2500,create_passerror_label.destroy())
        elif(action==1):
            create_success_label.grid(row=3)
            create_success_label.after(2500,create_success_label.destroy())
        else:
            create_nameerror_label.grid(row=3)
            create_nameerror_label.after(2500,create_nameerror_label.destroy())
    
    def login():
        username=name_var.get()
        password=cipher.cipher(passw_var.get())
        name_var.set("")
        passw_var.set("")
        check=lg.master_password_check(username,password)
        access=ctk.CTk()
        login_passerror_label=ctk.CTkLabel(frame,text='Incorrect Password!',font=('calibre',10, 'bold'))
        if check==1:
            access.title("WorkFlow")
            #Add custom icon here
            # access.iconbitmap("favicon.ico")
            access.geometry("750x500")
            access.wm_attributes('-transparentcolor','black')
            
            
            #Have to figure out this block
            results = tasks.view_task(username)
            df=pd.DataFrame(results)
            
            bg2 = ImageTk.PhotoImage(file = "Assets/bg2.png",master=access) 
            labelbg2 = ctk.CTkLabel( access,text="", image = bg2) 
            labelbg2.pack(fill="both")
            frame_access=ctk.CTkFrame(access)
            frame_access2=ctk.CTkFrame(access)
            frame_access3=ctk.CTkFrame(access)
            frame_access4=ctk.CTkFrame(access)
            frame_access5=ctk.CTkFrame(access)
            frame_access6=ctk.CTkFrame(access)
            frame_access7=ctk.CTkFrame(access)
            
            complete_tasks=tasks.view_task_complete(username)
            complete_tasks_df=pd.DataFrame(complete_tasks)
            
            table_comp = CTkTable(frame_access7,row=min(len(complete_tasks_df),5),column=4,values=complete_tasks,width=2)
            table_comp.pack()
            
            view_numbers_comp=ctk.CTkLabel(frame_access7,text="Viewing "+str(min(len(complete_tasks_df),4))+" complete tasks of "+str(len(complete_tasks_df))+" tasks.")
            view_numbers_comp.pack()
            
            frame_access7.place(relx=0.5,rely=0.55,anchor="center")
            
            description_task=ctk.CTkEntry(frame_access3, placeholder_text="Describe your task",font=('calibre',10,'normal'),width=350)
            description_task.grid(row=0,column=1,sticky="e")
            task_name=ctk.CTkEntry(frame_access4,placeholder_text="Task",font=('calibre',10,'normal'),width=75)
            task_name.grid(row=0,column=2,sticky="e")
            rating_task=ctk.CTkOptionMenu(master=frame_access5,  values=["High", "Medium", "Low"],width=90)
            rating_task.grid(row=0,column=3,sticky="e")
            
            add_success_label=ctk.CTkLabel(frame_access6,text="Task added successfully!",font=('calibre',15,'bold'),height=25,width=100)
            
            def new_task():
                desc=description_task.get()
                task=task_name.get()
                rating=rating_task.get()
                tasks.add_task(username,task,desc,rating)
                frame_access6.place(relx=0.07,rely=0.18)
                add_success_label.pack()
                add_success_label.after(2500,frame_access6.destroy)
                
            btn_add=ctk.CTkButton(frame_access,text='Add Task',command=new_task,width=90)
            btn_add.grid(row=0,column=0)
            
            def focus():
                timer=ctk.CTk()
                timer.title("WorkFlow")
                #Add custom icon here
                # root.iconbitmap("favicon.ico")
                timer.geometry("300x250")
                timer.wm_attributes('-transparentcolor','black')
                
                bg4 = ImageTk.PhotoImage(file = "Assets/bg4.png",master=timer) 
                labelbg4 = ctk.CTkLabel(timer,text="", image = bg4) 
                labelbg4.pack(fill="both")
                
                hour=ctk.StringVar()
                minute=ctk.StringVar()
                second=ctk.StringVar()
                
                # setting the default value as 0
                hour.set("00")
                minute.set("00")
                second.set("00")
                
                frame_focus=ctk.CTkFrame(timer)
                hour_entry=ctk.CTkEntry(frame_focus,textvariable=hour,width=33,font=("caliber",18,"bold"))
                minute_entry=ctk.CTkEntry(frame_focus,textvariable=minute,width=33,font=("caliber",18,"bold"))
                second_entry=ctk.CTkEntry(frame_focus,textvariable=second,width=33,font=("caliber",18,"bold"))
                frame_focus.place(relx=0.33,rely=0.3)
                hour_entry.grid(row=0,column=0)
                minute_entry.grid(row=0,column=1)
                second_entry.grid(row=0,column=2)
                
                def submit():
                    try:
                        temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
                    except:
                        print("Please input the right value")
                    while temp >-1:
                        mins,secs = divmod(temp,60) 
                        hours=0
                        if mins >60:
                            hours, mins = divmod(mins, 60)
                        
                        hour.set("{0:2d}".format(hours))
                        minute.set("{0:2d}".format(mins))
                        second.set("{0:2d}".format(secs))
                        timer.update()
                        time.sleep(1)
                        if (temp == 0):
                            timer.destroy()
                        
                        temp -= 1
                        
                def end_focus():
                    timer.destroy()
                
                btn = ctk.CTkButton(timer, text='Set Time Countdown',command= submit)
                btn.place(x=80,y=120)
                
                btn2 = ctk.CTkButton(timer, text='End Focus',command=end_focus)
                btn2.place(x=80,y=150)              

                timer.mainloop()
            
            def view_tasks():
                view=ctk.CTk()
                view.title("WorkFlow")
                view.geometry("750x500")
                
                bg3 = ImageTk.PhotoImage(file = "Assets/bg3.png",master=view) 
                labelbg3 = ctk.CTkLabel( view,text="", image = bg3) 
                labelbg3.pack(fill="both")
                
                frame_view=ctk.CTkFrame(view)
                frame_view.place(relx=0.5,rely=0.5,anchor="center")
            
                table = CTkTable(frame_view,row=min(len(df),8),column=4,values=results,width=1)
                table.pack()
                
                view_numbers=ctk.CTkLabel(frame_view,text="Viewing "+str(min(len(df),8))+" incomplete tasks of "+str(len(df))+" tasks.")
                view_numbers.pack()
                
                frame_view2=ctk.CTkFrame(view)
                frame_view2.place(relx=0.75,rely=0.9,anchor="center")
                
                task_input_entry=ctk.CTkEntry(frame_view2)
                task_input_entry.grid(row=0,column=0)
                label_update=ctk.CTkLabel(view,text="Table Updated!")
                
                def accept_task():
                    task_input=task_input_entry.get()
                    tasks.update_table(username,task_input)
                    label_update.place(relx=0.15,rely=0.8)
                    label_update.after(2500,label_update.destroy())
                
                btn_done=ctk.CTkButton(frame_view2,text="Mark done",command=accept_task)
                btn_done.grid(row=0,column=1)
                
                view.mainloop()
                
            
            focus_btn=ctk.CTkButton(frame_access2,text = 'Focus Mode',command=focus)
            view_btn=ctk.CTkButton(frame_access2,text='View Tasks',command=view_tasks)
            focus_btn.grid(row=0,column=0)
            view_btn.grid(row=0,column=1)
            frame_access.place(relx=0.81,rely=0.1)
            frame_access2.place(relx=0.55,rely=0.85)
            frame_access3.place(relx=0.31,rely=0.1)
            frame_access4.place(relx=0.07,rely=0.1)
            frame_access5.place(relx=0.18,rely=0.1)
            
            root.destroy()
            access.mainloop()
        else:
            login_passerror_label.grid(row=3)
        

    name_label = ctk.CTkLabel(frame, text = 'Username', font=('calibre',10, 'bold'))
    name_entry = ctk.CTkEntry(frame,textvariable = name_var, font=('calibre',10,'normal'))
    passw_label = ctk.CTkLabel(frame, text = 'Password', font = ('calibre',10,'bold'))
    passw_entry=ctk.CTkEntry(frame, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*')
    sub_btn=ctk.CTkButton(frame,text = 'Login', command = login)
    btn_signup=ctk.CTkButton(frame,text='Sign Up',command = signup)
    
    name_label.grid(row=0,column=0)
    name_entry.grid(row=0,column=1)
    passw_label.grid(row=1,column=0)
    passw_entry.grid(row=1,column=1)
    sub_btn.grid(row=2,column=0)
    btn_signup.grid(row=2,column=1)
    
landing()
root.mainloop()