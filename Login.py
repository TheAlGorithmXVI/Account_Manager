#An Account Manager...
import ttkbootstrap as ttk
import csv
from ttkbootstrap.constants import *
from tkinter import messagebox
from colored import style
######################################
#Account_Manager.destroy()---> completely destroy the loop process
#Account_Manager.quit()----> the loop process is still running
######################################
#Configuring pages of the platform...
######################################
def Main_Menu(app):
    global Request , Sign_Up , Sign_In , Exit_From_Main_Menu
    Request = ttk.Label(app , text = "با سلام. لطفا عمل مورد نظر خود را انتخاب نمایید" , font = ("Calibri" , 10 , "bold"))
    Request.grid(row = 3 , column = 0 , padx = 250 , pady = 70)
    Sign_Up = ttk.Button(app , text = "ایجاد حساب کاربری" , width = 20 , style = "success.Link.TButton" , command = Main_Menu_Mechanism1)
    Sign_Up.grid(row = 4 , column = 0 , padx = 270)
    Sign_In = ttk.Button(app , text = "ورود به حساب کاربری" , width = 20 , style = "success.Link.TButton" , command = Main_Menu_Mechanism2)
    Sign_In.grid(row = 5 , column = 0 , padx = 270)
    Exit_From_Main_Menu = ttk.Button(app , text = "خروج از پلتفرم" , width = 20 , style = "success.Link.TButton" , command = Main_Menu_Mechanism3)
    Exit_From_Main_Menu.grid(row = 6 , column = 0 , padx = 270)

def Identity(app):
    global fne , lne , eae , fnl , lnl , eal , Next_From_Identity , Back_From_Identity , Close_From_Identity
    fnl = ttk.Label(app , text = "لطفا نام خود را وارد نمایید" , font = ("Calibri" , 10))
    fnl.grid(row = 0 , column = 0 , padx = 270 , pady = 10)
    fne= ttk.Entry(app , width = 30)
    fne.grid(row = 1 , column = 0 , padx = 270)
    lnl = ttk.Label(app , text = "لطفا نام خانوادگی خود را وارد نمایید" , font = ("Calibri" , 10))
    lnl.grid(row = 2 , column = 0 , padx = 270 , pady = 10)
    lne= ttk.Entry(app , width = 30)
    lne.grid(row = 3 , column = 0 , padx = 270)
    eal = ttk.Label(app , text = "لطفا نشانی رایانامه خود را وارد نمایید" , font = ("Calibri" , 10))
    eal.grid(row = 4 , column = 0 , padx = 270 , pady = 10)
    eae= ttk.Entry(app , width = 30)
    eae.grid(row = 5 , column = 0 , padx = 270)
    Next_From_Identity = ttk.Button(app , text = "مرحله بعدی" , width = 10 , style = "success.Link.TButton" , command = Identity_Mechanism1)
    Next_From_Identity.grid(row = 7 , column = 0 , padx = 150)
    Back_From_Identity = ttk.Button(app , text = "بازگشت به منوی اصلی" , width = 30 , style = "success.Link.TButton" , command = Identity_Mechanism2)
    Back_From_Identity.grid(row = 8 , column = 0 , padx = 150)
    Close_From_Identity = ttk.Button(app , text = "خروج از پلتفرم" , width = 30 , style = "success.Link.TButton" , command = Identity_Mechanism3)
    Close_From_Identity.grid(row = 9 , column = 0 , padx = 150)

def Username_Password(app):
    global unl , une , pl , pe , cl , ce , Back_From_Username_Password , Username_Password_Submission , Close_From_Username_Password
    unl = ttk.Label(app , text = "لطفا نام کاربری خود را وارد نمایید" , font = ("Calibri" , 10))
    unl.grid(row = 0 , column = 0 , padx = 270 , pady = 10)
    une = ttk.Entry(app , width = 30)
    une.grid(row = 1 , column = 0 , padx = 270)
    pl = ttk.Label(app , text = "لطفا رمز عبور خود را وارد نمایید" , font = ("Calibri" , 10))
    pl.grid(row = 2 , column = 0 , padx = 270 , pady = 10)
    pe = ttk.Entry(app , width = 30)
    pe.grid(row = 3 , column = 0 , padx = 270)
    cl = ttk.Label(app , text = "لطفا رمز عبور خود را تایید نمایید" , font = ("Calibri" , 10))
    cl.grid(row = 4 , column = 0 , padx = 270 , pady = 10)
    ce = ttk.Entry(app , width = 30)
    ce.grid(row = 5 , column = 0 , padx = 270)
    Username_Password_Submission = ttk.Button(app , text = "ارسال" , width = 10 , style = "success.Link.TButton" , command = Username_Password_Mechanism1)
    Username_Password_Submission.grid(row = 6 , column = 0)
    Back_From_Username_Password = ttk.Button(app , text = "بازگشت به صفحه قبل" , width = 20 , style = "success.Link.TButton" , command = Username_Password_Mechanism2)
    Back_From_Username_Password.grid(row = 7 , column = 0 , pady = 20)
    Close_From_Username_Password = ttk.Button(app , text = "خروج از پلتفرم" , width = 30 , style = "success.Link.TButton" , command = Username_Password_Mechanism3)
    Close_From_Username_Password.grid(row = 8 , column = 0)
    
def Gate(app):
    global gunl , gpl , gune , gpe , Gate_Submit , Close_From_Gate , Return_Main_Menu
    gunl = ttk.Label(app , text = "لطفا نام کاربری خود را وارد نمایید" , font = ("Calibri" , 10))
    gunl.grid(row = 3 , column = 0 , padx = 270 , pady = 10)
    gune = ttk.Entry(app , width = 30)
    gune.grid(row = 4 , column = 0 , padx = 270)
    gpl = ttk.Label(app , text = "لطفا رمز عبود خود را وارد نمایید" , font = ("Calibri" , 10))
    gpl.grid(row = 5 , column = 0 , padx = 270)
    gpe = ttk.Entry(app , width = 30)
    gpe.grid(row = 6 , column = 0 , padx = 270)
    Gate_Submit = ttk.Button(app , text = "ورود به حساب کاربری" , width = 20 , style = "success.Link.TButton" , command = Gate_Mechanism1)
    Gate_Submit.grid(row = 7 , column = 0 , padx = 270)
    Close_From_Gate = ttk.Button(app , text = "خروج از پلتفرم" , width = 20 , style = "success.Link.TButton" , command = Gate_Mechanism2)
    Close_From_Gate.grid(row = 8 , column = 0 , padx = 270)
    Return_Main_Menu = ttk.Button(app , text = "بازگشت به منوی اصلی" , width = 30 , style = "success.Link.TButton" , command = Gate_Mechanism3)
    Return_Main_Menu.grid(row = 9 , column = 0 , padx = 270)

def Verification_Result_Successfull(app):
    global Result_Successfull , Which_Operation1 , VRS_Main_Menu , VRS_Close
    Result_Successfull = ttk.Label(app , text = "کاربر گرامی با موفقیت وارد پلتفرم گردید" , font = ("Calibri" , 10))
    Result_Successfull.grid(row = 2 , column = 0 , padx = 270 , pady = 50)
    Which_Operation1 = ttk.Label(app , text = "لطفا یکی از گزینه های زیر را انتخاب نمایید" , font = ("Calibri" , 10))
    Which_Operation1.grid(row = 3 , column = 0 , padx = 270 , pady = 20)
    VRS_Main_Menu = ttk.Button(app , text = "بازگشت به منوی اصلی" , width = 30 , style = "success.Link.TButton" , command = VRS_Mechanism1)
    VRS_Main_Menu.grid(row = 4 , column = 0 ,padx = 270 , pady = 20)
    VRS_Close = ttk.Button(app , text = "خروج از پلتفرم" , width = 30 , style = "success.Link.TButton" , command = VRS_Mechanism2)
    VRS_Close.grid(row = 5 , column = 0 , padx = 270 , pady = 20)

def Verification_Result_Unsuccessfull(app):
    global Result_Unsuccessfull , Which_Operation2 , VRU_Main_Menu , VRU_Close , VRU_Try_Again
    Result_Unsuccessfull = ttk.Label(app , text = "متاسفانه کاربری با مشخصات وارد شده در سیستم یافت نشد" , font = ("Calibri" , 10))
    Result_Unsuccessfull.grid(row = 2 , column = 0 , padx = 240 , pady = 50)
    Which_Operation2 = ttk.Label(app , text = "لطفا یکی از گزینه های زیر را انتخاب نمایید" , font = ("Calibri" , 10))
    Which_Operation2.grid(row = 3 , column = 0 , padx = 240 , pady = 20)
    VRU_Try_Again = ttk.Button(app , text = "تلاش مجدد" , width = 30 , style = "success.Link.TButton" , command = VRU_Mechanism1)
    VRU_Try_Again.grid(row = 4 , column = 0 ,padx = 270 , pady = 20)
    VRU_Main_Menu = ttk.Button(app , text = "بازگشت به منوی اصلی" , width = 30 , style = "success.Link.TButton" , command = VRU_Mechanism2)
    VRU_Main_Menu.grid(row = 5 , column = 0 ,padx = 270 , pady = 20)
    VRU_Close = ttk.Button(app , text = "خروج از پلتفرم" , width = 30 , style = "success.Link.TButton" , command = VRU_Mechanism3)
    VRU_Close.grid(row = 6 , column = 0 , padx = 270 , pady = 20)
    
#############################################################
#Mechanism Methods...
def Main_Menu_Mechanism1():
    Request.grid_forget()
    Sign_Up.grid_forget()
    Sign_In.grid_forget()
    Exit_From_Main_Menu.grid_forget()
    Identity(Account_Manager)

def Main_Menu_Mechanism2():
     Request.grid_forget()
     Sign_Up.grid_forget()
     Sign_In.grid_forget()
     Exit_From_Main_Menu.grid_forget()
     Gate(Account_Manager)
    
def Main_Menu_Mechanism3():
    Account_Manager.destroy()

#*********
def Identity_Mechanism1():
    global FNE , LNE ,EAE
    FNE = fne.get()
    LNE = lne.get()
    EAE = eae.get()
    if len(FNE) == 0 or len(LNE) == 0 or len(EAE) == 0:
        messagebox.showerror("اخطار" , "کاربر گرامی: لطفا تمامی قسمت های مذکور را تکمیل نمایید")
    else:
        fnl.grid_forget()
        fne.grid_forget()
        lnl.grid_forget()
        lne.grid_forget()
        eal.grid_forget()
        eae.grid_forget()
        Next_From_Identity.grid_forget()
        Back_From_Identity.grid_forget()
        Close_From_Identity.grid_forget()
        Username_Password(Account_Manager)  

def Identity_Mechanism2():
    fnl.grid_forget()
    fne.grid_forget()
    lnl.grid_forget()
    lne.grid_forget()
    eal.grid_forget()
    eae.grid_forget()
    Next_From_Identity.grid_forget()
    Back_From_Identity.grid_forget()
    Close_From_Identity.grid_forget()
    Main_Menu(Account_Manager)

def Identity_Mechanism3():
    Account_Manager.destroy()

#*********
def Username_Password_Mechanism1():
    global UNE , PE , CE
    UNE = une.get()
    PE = pe.get()
    CE = ce.get()
    if len(UNE) <= 7:
        messagebox.showerror("اخطار" , "نام کاربری باید حداقل شامل 8 کاراکتر باشد")
    else:
        Permission = 0
        with open("DataBase.csv" , "r" , newline = "") as database:
            db = csv.reader(database)
            DB = list(db)
            for i in DB:
                if str(i[3]) == str(UNE):
                    Permission = 1
                    break
            database.close()

            if Permission == 1:
                messagebox.showerror("اخطار" , "نام کاربری مد نظر شما قبلا انتخاب گردیده است. لطفا نام کاربری دیگری وارد نمایید")
                une.delete(0 , ttk.END)
                pe.delete(0 , ttk.END)
                ce.delete(0 , ttk.END)
            if Permission == 0:
                if len(PE) <= 7:
                    messagebox.showerror("اخطار" , "رمز عبور باید دارای حداقل 8 کاراکتر باشد")
                    pe.delete(0 , ttk.END)
                    ce.delete(0 , ttk.END)
                else:
                    Upper = {"A" , "B" , "C" , "D" , "E" , "F" , "G" , "H" , "I" , "J" , "K" , "L" , "M" , "N" , "O" , "P" , "Q" , "R" , "S" , "T" , "U" , "V" , "W" , "X" , "Y" , "Z"}
                    Lower = {"a" , "b" , "c" , "d" , "e" , "f" , "g" , "h" , "i" , "j" , "k" , "l" , "m" , "n" , "o" , "p" , "q" , "r" , "s" , "t" , "u" , "v" , "w" , "x" , "y" , "z"}
                    Numbers = {"0" , "1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9"}
                    Exceptionals = {"~" , "!" , "@" , "#" , "$" , "%" , "^" , "&" , "*" , "(" , ")" , "+" , "=" , "[" , "]" , "{" , "}" , "/"  , ","}
                    upper_count = 0
                    lower_count = 0
                    numbers_count = 0
                    exceptional_count = 0

                    for character in PE:
                        if character in Upper:
                            upper_count += 1
                        if character in Lower:
                            lower_count += 1
                        if character in Numbers:
                            numbers_count += 1
                        if character in Exceptionals:
                            exceptional_count += 1

                    if upper_count == 0 or lower_count == 0 or numbers_count == 0 or exceptional_count == 0:
                        messagebox.showerror("اخطار" , "رمز عبور انتخابی باید شامل حروف کوچک و حروف بزرگ و اعداد و کاراکترهای استثنایی باشد")  
                    else:
                        if PE != CE:
                            messagebox.showerror("اخطار" , "عدم مطابت رمزهای عبور مشاهده گردید")
                        else:
                            with open("DataBase.csv" , "a" , newline = "" , encoding = "utf-8") as record:
                                Record = csv.writer(record)
                                Record.writerow([FNE , LNE , EAE , UNE , PE])
                                record.close()
                            messagebox.showinfo("گزارش" , "کاربر گرامی: ثبت نام شما با موفقیت انجام گردید")
                            unl.grid_forget()
                            une.grid_forget()
                            pl.grid_forget()
                            pe.grid_forget()
                            cl.grid_forget()
                            ce.grid_forget()
                            Username_Password_Submission.grid_forget()
                            Back_From_Username_Password.grid_forget()
                            Close_From_Username_Password.grid_forget()
                            Main_Menu(Account_Manager)        

def Username_Password_Mechanism2():
    unl.grid_forget()
    une.grid_forget()
    pl.grid_forget()
    pe.grid_forget()
    cl.grid_forget()
    ce.grid_forget()
    Back_From_Username_Password.grid_forget()
    Username_Password_Submission.grid_forget()
    Close_From_Username_Password.grid_forget()
    Identity(Account_Manager)
def Username_Password_Mechanism3():
    Account_Manager.destroy()

#*********
def Gate_Mechanism1():
    global GUN , GP
    Allow = 0
    GUN = gune.get()
    GP = gpe.get()
    with open("DataBase.csv" , "r" , newline = "") as Verification:
        VRFY = csv.reader(Verification)
        VR = list(VRFY)
        for information in VR:
            if information[3] == GUN and information[4] == GP:
                Allow = 1
                break
        Verification.close()
    if Allow == 1:    
        gunl.grid_forget()
        gune.grid_forget()
        gpl.grid_forget()
        gpe.grid_forget()
        Gate_Submit.grid_forget()
        Close_From_Gate.grid_forget()
        Return_Main_Menu.grid_forget()
        Verification_Result_Successfull(Account_Manager)
    if Allow == 0:
        gunl.grid_forget()
        gune.grid_forget()
        gpl.grid_forget()
        gpe.grid_forget()
        Gate_Submit.grid_forget()
        Close_From_Gate.grid_forget()
        Return_Main_Menu.grid_forget()
        Verification_Result_Unsuccessfull(Account_Manager)

def Gate_Mechanism2():
    Account_Manager.destroy()

def Gate_Mechanism3():
    gunl.grid_forget()
    gune.grid_forget()
    gpl.grid_forget()
    gpe.grid_forget()
    Close_From_Gate.grid_forget()
    Gate_Submit.grid_forget()
    Return_Main_Menu.grid_forget()
    Main_Menu(Account_Manager)

#*********
def VRS_Mechanism1():
    Result_Successfull.grid_forget()
    Which_Operation1.grid_forget()
    VRS_Main_Menu.grid_forget()
    VRS_Close.grid_forget()
    Main_Menu(Account_Manager)

def VRS_Mechanism2():
    Account_Manager.destroy()

#*********
def VRU_Mechanism1():
    Result_Unsuccessfull.grid_forget()
    Which_Operation2.grid_forget()
    VRU_Try_Again.grid_forget()
    VRU_Close.grid_forget()
    VRU_Main_Menu.grid_forget()
    Gate(Account_Manager)
def VRU_Mechanism2():
    Result_Unsuccessfull.grid_forget()
    Which_Operation2.grid_forget()
    VRU_Try_Again.grid_forget()
    VRU_Close.grid_forget()
    VRU_Main_Menu.grid_forget()
    Main_Menu(Account_Manager)
def VRU_Mechanism3():
    Account_Manager.destroy()
############################################################
#Framework Configuration...  
Account_Manager = ttk.Window(themename = "cyborg")
Account_Manager.title("مدیریت حساب های کاربری")
Account_Manager.resizable(False , False)
Account_Manager.geometry("800x500+500+250")
###########################################################
#For Experimental Issues...
# Main_Menu(Account_Manager)
#Identity(Account_Manager)
#Username_Password(Account_Manager)
#Gate(Account_Manager)
#Verification_Result_Successful(Account_Manager)
#Verification_Result_Unsuccessful(Account_Manager)
###########################################################
#The Program is now ready to start...
Main_Menu(Account_Manager)
Account_Manager.mainloop()   