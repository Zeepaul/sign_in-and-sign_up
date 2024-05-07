from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import os

#----------ĐỊNH NGHĨA CÁC BIẾN----------
FONT = 'Open Sans'
BACKGROUND_COLOR_1 = 'SlateBlue1'
BACKGROUND_COLOR_3 = 'SlateBlue3'
FONT_SIZE = 30


accountSystem = Tk()
accountSystem.rowconfigure(0, weight = 1)
accountSystem.columnconfigure(0, weight = 1)

accountSystem.geometry('1920x1080')
accountSystem.title('ACCOUNT SYSTEM')

#Liên kết giữa 2 trang sign_in và sign_up
SIGN_IN_PAGE = Frame(accountSystem)
SIGN_UP_PAGE = Frame(accountSystem)
FORGOT_PAGE = Frame(accountSystem)

for frame in (SIGN_IN_PAGE, SIGN_UP_PAGE, FORGOT_PAGE):
    frame.grid(row = 0, column = 0, sticky = 'nsew')

def show_frame(frame):
    frame.tkraise()

show_frame(SIGN_IN_PAGE) #hiện trang sign_in trước


#-----------------------------------------------------------------
#-------------------------FORGOT PASSWORD-------------------------
#-----------------------------------------------------------------

def forgot_hide():
    forgot_openeye.config(file ='images/close_eye.png')
    forgot_passwordEntry.config(show = '*')
    forgot_eyeButton.config(command = forgot_show)

def forgot_show():
    forgot_openeye.config(file ='images/open_eye.png')
    forgot_passwordEntry.config(show = '')
    forgot_eyeButton.config(command = forgot_hide)


def forgot_user_enter(event):
    if forgot_usernameEntry.get() == 'Username':
        forgot_usernameEntry.delete(0, END)


def forgot_password_enter(event):
    if forgot_passwordEntry.get() == 'New Password':
        forgot_passwordEntry.delete(0, END)

def forgot_confirmpassword_enter(event):
    if forgot_confirmpasswordEntry.get() == 'Confirm New Password':
        forgot_confirmpasswordEntry.delete(0, END)
        forgot_confirmpasswordEntry.config(show = '*')

def forgot_clear():
    forgot_usernameEntry.delete(0, END)
    forgot_passwordEntry.delete(0, END)
    forgot_confirmpasswordEntry.delete(0, END)
def change_database():
    if forgot_usernameEntry.get() == '' or forgot_passwordEntry.get() == '' or forgot_confirmpasswordEntry.get() == '':
        messagebox.showerror('Error', 'All Fields are required')
    elif forgot_passwordEntry.get() != forgot_confirmpasswordEntry.get():
        messagebox.showerror('Error', 'Password Mismatch')
    else:
        if not os.path.exists(f"database/{forgot_usernameEntry.get()}.txt"):  # Kiểm tra xem tên người dùng có tồn tại không
            messagebox.showerror("Username doesn't exist!", "Username doesn't exist!")  # Hiển thị thông báo lỗi
        elif forgot_passwordEntry.get() == forgot_confirmpasswordEntry.get():  # Kiểm tra xem mật khẩu và mật khẩu nhập lại có khớp không
            with open(f"database/{forgot_usernameEntry.get()}.txt", "w") as file:  # Mở file với tên người dùng cần đổi mật khẩu
                file.write(forgot_passwordEntry.get())  # Ghi đè mật khẩu vào dòng đầu tiên của file
            messagebox.showinfo("Reset password successful!","Reset password successful!")  # Hiển thị thông báo thành công
            forgot_clear() #Xóa các thông tin đã nhập trên màn hình
            show_frame(SIGN_IN_PAGE)
        else:
            messagebox.showerror("Passwords do not match!","Passwords do not match!")  # Hiển thị thông báo lỗi

#----------BACKGROUND IMAGE----------
forgot_bgImage = ImageTk.PhotoImage(file = 'images/sign_up.jpg')
forgot_bgLabel = Label(FORGOT_PAGE, image = forgot_bgImage)
forgot_bgLabel.place(x = 0, y = 0)

#Tạo nhãn RESET PASSWORD
forgot_heading = Label(FORGOT_PAGE, text ='RESET PASSWORD', font = (FONT, 24, 'bold'), bg = BACKGROUND_COLOR_1, fg ='white')
forgot_heading.place(x = 1145, y = 275)

#----------USERNAME----------
forgot_usernameEntry = Entry(FORGOT_PAGE, width = 23, font = (FONT, FONT_SIZE, 'bold'), bg = BACKGROUND_COLOR_1, fg ='white', bd = 0)
forgot_usernameEntry.place(x = 1025, y = 381)
forgot_usernameEntry.insert(0, 'Username')
forgot_usernameEntry.bind('<FocusIn>', forgot_user_enter)

#----------NEW PASSWORD----------
forgot_passwordEntry=Entry(FORGOT_PAGE, width=21, font=(FONT, FONT_SIZE, 'bold'), bg = BACKGROUND_COLOR_1, fg ='white', bd = 0)
forgot_passwordEntry.place(x = 1025, y = 488)
forgot_passwordEntry.insert(0, 'New Password')
forgot_passwordEntry.bind('<FocusIn>', forgot_password_enter)

forgot_openeye = PhotoImage(file='images/open_eye.png')
forgot_eyeButton = Button(FORGOT_PAGE, image = forgot_openeye, bd = 0, bg = BACKGROUND_COLOR_1, activebackground = BACKGROUND_COLOR_1, cursor ='hand2', command = forgot_hide)
forgot_eyeButton.place(x = 1490, y = 485)

#----------CONFIRM NEW PASSWORD----------
forgot_confirmpasswordEntry = Entry(FORGOT_PAGE, width = 23, font = (FONT, FONT_SIZE, 'bold'), bg = BACKGROUND_COLOR_1, fg ='white', bd = 0)
forgot_confirmpasswordEntry.place(x = 1025, y = 595)
forgot_confirmpasswordEntry.insert(0, 'Confirm New Password')
forgot_confirmpasswordEntry.bind('<FocusIn>', forgot_confirmpassword_enter)

#----------SUBMIT----------
forgot_submitButton = Button(FORGOT_PAGE, text ='Submit', font = (FONT, FONT_SIZE, 'bold'), bg = BACKGROUND_COLOR_1, fg ='white', activeforeground ='white', activebackground = BACKGROUND_COLOR_1, cursor ='hand2', bd = 0, command = change_database)
forgot_submitButton.place(x = 1210, y = 693)

#Tạo nút 'Create new account' và 'Login', chuyển người dùng đến trang sign_up hoặc sign_in
forgot_signupButton = Button(FORGOT_PAGE, text ='Creat new account', font = (FONT, 15, 'bold underline'), fg ='white', bg = BACKGROUND_COLOR_3, activeforeground ='white', activebackground = BACKGROUND_COLOR_3, cursor ='hand2', bd = 0, command = lambda : show_frame(SIGN_UP_PAGE)) #Liên kết người dùng đến trang sign_up
forgot_signupButton.place(x = 1145, y = 794)

forgot_text = Label(FORGOT_PAGE, text ='or', font = (FONT, 15, 'bold'), fg ='white', bg = BACKGROUND_COLOR_3)
forgot_text.place(x = 1337, y = 798)

forgot_signinButton = Button(FORGOT_PAGE, text ='Login', font = (FONT, 15, 'bold underline'), fg ='white', bg = BACKGROUND_COLOR_3, activeforeground ='white', activebackground = BACKGROUND_COLOR_3, cursor ='hand2', bd = 0, command = lambda : show_frame(SIGN_IN_PAGE)) #Liên kết người dùng đến trang sign_in
forgot_signinButton.place(x = 1365, y = 794)


#-----------------------------------------------------------------
#-------------------------SIGN IN---------------------------------
#-----------------------------------------------------------------


#----------FUNCTIONAL PART----------
def signin_hide(): #ấn biểu tượng mắt nhắm -> mật khẩu có dạng * và biểu tượng mắt mở hiện ra
    signin_openeye.config(file = 'images/close_eye.png') #hiện biểu tượng mắt nhắm
    signin_passwordEntry.config(show = '*') #mật khẩu có dạng *
    signin_eyeButton.config(command = signin_show) #biểu tượng mắt mở hiện ra

def signin_show(): #ấn biểu tượng mắt mở -> mật khẩu hiện bình thường và biểu tượng mắt nhắm hiện ra
    signin_openeye.config(file = 'images/open_eye.png') #hiện biểu tượng mắt mở
    signin_passwordEntry.config(show = '') #mật khẩu về trạng thái hiển thị bình thường
    signin_eyeButton.config(command = signin_hide) #biểu tượng nhắm mắt hiện ra


def signin_user_enter(event): #Khi ấn vào ô Username, chữ 'Username' bị xóa
    if signin_usernameEntry.get() == 'Username':
        signin_usernameEntry.delete(0, END)


def signin_password_enter(event): #Khi ấn vào ô password chữ 'Password' bị xóa
    if signin_passwordEntry.get() == 'Password':
        signin_passwordEntry.delete(0, END)

def signin_clear():
    signin_usernameEntry.delete(0, END)
    signin_passwordEntry.delete(0, END)

def signin():
    if signin_usernameEntry.get() == '' or signin_passwordEntry.get() == '':
        messagebox.showerror('Error', 'All Fields are required!')
    else:
        if os.path.exists(f"database/{signin_usernameEntry.get()}.txt"):  # Kiểm tra xem tên người dùng có tồn tại không
            with open(f"database/{signin_usernameEntry.get()}.txt", "r") as file:  # Mở file tương ứng với tên người dùng
                if signin_passwordEntry.get() == file.readline():  # Kiểm tra xem mật khẩu có khớp không
                    messagebox.showinfo("Login successful!","Login successful!")  # Hiển thị thông báo thành công
                    signin_clear()

                else:
                   messagebox.showerror("Invalid username or password!","Invalid username or password!")  # Hiển thị thông báo lỗi
        else:
            messagebox.showerror("Invalid username or password!","Invalid username or password!")


#----------BACKGROUND IMAGE----------
#Load background image
signin_bgImage = ImageTk.PhotoImage(file = 'images/sign_in.jpg')
signin_bgLabel = Label(SIGN_IN_PAGE, image = signin_bgImage)
signin_bgLabel.place(x = 0, y = 0)

#Tạo nhãn 'Sign in' tại tọa độ x, y
signin_heading = Label(SIGN_IN_PAGE, text='SIGN IN', font=(FONT, 35, 'bold'), bg = BACKGROUND_COLOR_1, fg='white')
signin_heading.place(x = 1200, y=267)

#----------USERNAME----------
#Tạo nhãn Username và ô nhập thông tin Username
signin_usernameEntry = Entry(SIGN_IN_PAGE, width = 23, font = (FONT, FONT_SIZE, 'bold'), bg = BACKGROUND_COLOR_1, fg='white', bd = 0) #Tạo khung nhập thông tin
signin_usernameEntry.place(x = 1020, y = 415) #Tọa độ khung
signin_usernameEntry.insert(0, 'Username')
signin_usernameEntry.bind('<FocusIn>', signin_user_enter) #Xóa chữ 'Username' khi người dùng ấn vào khung

#----------PASSWORD---------
#Tạo nhãn Password và ô nhập thông tin Password
signin_passwordEntry = Entry(SIGN_IN_PAGE, width=21, font = (FONT, FONT_SIZE, 'bold'), bg = BACKGROUND_COLOR_1, fg='white', bd=0)
signin_passwordEntry.place(x = 1020, y = 537)
signin_passwordEntry.insert(0, 'Password')
signin_passwordEntry.bind('<FocusIn>', signin_password_enter)
#Tạo nút ẩn, hiện password
signin_openeye = PhotoImage(file='images/open_eye.png')
signin_eyeButton=Button(SIGN_IN_PAGE, image = signin_openeye, bd = 0, bg = BACKGROUND_COLOR_1, activebackground = BACKGROUND_COLOR_1, cursor ='hand2', command = signin_hide)
signin_eyeButton.place(x = 1490, y = 533)

#----------FORGET PASSWORD----------
#Tạo mục "Forget Password
signin_forgetButton = Button(SIGN_IN_PAGE, text ='Forget Password?', bd = 0, bg = BACKGROUND_COLOR_3, activebackground = BACKGROUND_COLOR_3, cursor ='hand2', font = (FONT, 15, 'bold'), fg ='white', activeforeground ='white', command = lambda  : show_frame(FORGOT_PAGE))
signin_forgetButton.place(x = 1045, y = 690)

#----------LOG IN---------
signin_loginButton = Button(SIGN_IN_PAGE, text ='Login', font = (FONT, FONT_SIZE, 'bold'), bg = BACKGROUND_COLOR_1, fg ='white', activeforeground ='white', activebackground = BACKGROUND_COLOR_1, cursor ='hand2', bd = 0, command = signin)
signin_loginButton.place(x = 1325, y = 667)

#----------CREATE NEW ACCOUNT----------
#Tạo nhãn hỏi người dùng 'Don't have an account?'
signin_signupLabel=Label(SIGN_IN_PAGE, text="Don't have an account?", font = (FONT, 15, 'bold'), bg = BACKGROUND_COLOR_3, fg ='white', bd=0)
signin_signupLabel.place(x = 1040, y = 800)

#Tạo nút 'Create new account', chuyển người dùng đến trang sign_up
signin_signupButton = Button(SIGN_IN_PAGE, text ='Creat new account', font = (FONT, 15, 'bold underline'), fg ='white', bg = BACKGROUND_COLOR_3, activeforeground ='white', activebackground = BACKGROUND_COLOR_3, cursor ='hand2', bd=0, command = lambda : show_frame(SIGN_UP_PAGE)) #Liên kết người dùng đến trang sign_up
signin_signupButton.place(x = 1266, y = 794)


#--------------------------------------------------------------------
#-------------------------SIGN UP------------------------------------
#--------------------------------------------------------------------

#----------fUCNTIONAL PART----------
def signup_hide():
    signup_openeye.config(file ='images/close_eye.png')
    signup_passwordEntry.config(show = '*')
    signup_eyeButton.config(command = signup_show)

def signup_show():
    signup_openeye.config(file ='images/open_eye.png')
    signup_passwordEntry.config(show = '')
    signup_eyeButton.config(command = signup_hide)


def signup_user_enter(event):
    if signup_usernameEntry.get() == 'Username':
        signup_usernameEntry.delete(0, END)


def signup_password_enter(event):
    if signup_passwordEntry.get() == 'Password':
        signup_passwordEntry.delete(0, END)

def signup_confirmpassword_enter(event):
    if signup_confirmpasswordEntry.get() == 'Confirm Password':
        signup_confirmpasswordEntry.delete(0, END)
        signup_confirmpasswordEntry.config(show = '*')

def signup_clear():
    signup_usernameEntry.delete(0, END)
    signup_passwordEntry.delete(0, END)
    signup_confirmpasswordEntry.delete(0, END)
def connect_database():
    if signup_usernameEntry.get() == '' or signup_passwordEntry.get() == '' or signup_confirmpasswordEntry.get() == '':
        messagebox.showerror('Error', 'All Fields are required')
    elif signup_passwordEntry.get() != signup_confirmpasswordEntry.get():
        messagebox.showerror('Error', 'Password Mismatch')
    else:
        if os.path.exists(f"database/{signup_usernameEntry.get()}.txt"):  # Kiểm tra xem tên người dùng có tồn tại không
            messagebox.showerror("Username existed!", "Username existed!")  # Hiển thị thông báo lỗi
        elif signup_passwordEntry.get() == signup_confirmpasswordEntry.get():  # Kiểm tra xem mật khẩu và mật khẩu nhập lại có khớp không
            with open(f"database/{signup_usernameEntry.get()}.txt", "w") as file:  # Tạo một file mới với tên người dùng
                file.write(signup_passwordEntry.get())  # Ghi mật khẩu vào dòng đầu tiên của file
            messagebox.showinfo("Register successful!","Register successful!")  # Hiển thị thông báo thành công
            signup_clear() #Xóa các thông tin đã nhập trên màn hình
        else:
            messagebox.showerror("Passwords do not match!","Passwords do not match!")  # Hiển thị thông báo lỗi

#----------BACKGROUND IMAGE----------
signup_bgImage = ImageTk.PhotoImage(file = 'images/sign_up.jpg')
signup_bgLabel = Label(SIGN_UP_PAGE, image = signup_bgImage)
signup_bgLabel.place(x = 0, y = 0)

signup_heading = Label(SIGN_UP_PAGE, text ='SIGN UP', font = (FONT, 35, 'bold'), bg = BACKGROUND_COLOR_1, fg ='white')
signup_heading.place(x = 1200, y = 267)

#----------USERNAME----------
signup_usernameEntry = Entry(SIGN_UP_PAGE, width = 23, font = (FONT, FONT_SIZE, 'bold'), bg = BACKGROUND_COLOR_1, fg ='white', bd = 0)
signup_usernameEntry.place(x = 1025, y = 381)
signup_usernameEntry.insert(0, 'Username')
signup_usernameEntry.bind('<FocusIn>', signup_user_enter)

#----------PASSWORD----------
signup_passwordEntry=Entry(SIGN_UP_PAGE, width=21, font=(FONT, FONT_SIZE, 'bold'), bg = BACKGROUND_COLOR_1, fg ='white', bd = 0)
signup_passwordEntry.place(x = 1025, y = 488)
signup_passwordEntry.insert(0, 'Password')
signup_passwordEntry.bind('<FocusIn>', signup_password_enter)

signup_openeye = PhotoImage(file='images/open_eye.png')
signup_eyeButton = Button(SIGN_UP_PAGE, image = signup_openeye, bd = 0, bg = BACKGROUND_COLOR_1, activebackground = BACKGROUND_COLOR_1, cursor ='hand2', command = signup_hide)
signup_eyeButton.place(x = 1490, y = 485)

#----------CONFIRM PASSWORD----------
signup_confirmpasswordEntry = Entry(SIGN_UP_PAGE, width = 23, font = (FONT, FONT_SIZE, 'bold'), bg = BACKGROUND_COLOR_1, fg ='white', bd = 0)
signup_confirmpasswordEntry.place(x = 1025, y = 595)
signup_confirmpasswordEntry.insert(0, 'Confirm Password')
signup_confirmpasswordEntry.bind('<FocusIn>', signup_confirmpassword_enter)

#----------REGISTER----------
signup_registerButton = Button(SIGN_UP_PAGE, text ='Register', font = (FONT, FONT_SIZE, 'bold'), bg = BACKGROUND_COLOR_1, fg ='white', activeforeground ='white', activebackground = BACKGROUND_COLOR_1, cursor ='hand2', bd = 0, command = connect_database)
signup_registerButton.place(x = 1200, y = 693)

#----------SIGN IN----------
signup_signinLabel = Label(SIGN_UP_PAGE, text ="Already have an account?", font = (FONT, 15, 'bold'), bg = BACKGROUND_COLOR_3, fg ='white', bd = 0)
signup_signinLabel.place(x=1120,y=815)

signup_signinButton = Button(SIGN_UP_PAGE, text ='Login', font = (FONT, 15, 'bold underline'), fg ='white', bg = BACKGROUND_COLOR_3, activeforeground ='white', activebackground = BACKGROUND_COLOR_3, cursor ='hand2', bd = 0, command = lambda : show_frame(SIGN_IN_PAGE)) #Liên kết người dùng đến trang sign_in
signup_signinButton.place(x = 1370, y = 808)

accountSystem.resizable(0,0)
accountSystem.mainloop()