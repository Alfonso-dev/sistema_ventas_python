from tkinter import *

def ingresar():
    pass

ventana = Tk()
ventana.title("Login")
ventana.resizable(False,False)

frame_one = Frame(ventana)
frame_one.config(width="100", height="500", bg="Blue")
frame_one.pack()
frame_two = Frame(ventana)
frame_two.config(width="400", height="500", bg="white")
frame_two.pack()

#*************** LABELS LOGIN ***********
label_usuario = Label(frame_one, text="USUARIO:")
label_usuario.place(x=170, y=140)

label_password = Label(frame_one, text="Password:")
label_password.place(x=170, y=220)

label_recovery = Label(frame_one, text="¿Olvidaste tu cuenta?")
label_recovery.config(fg="blue")
label_recovery.place(x=165, y=320)

#*************** ENTRYS LOGIN ***********
input_usuario = Entry(frame_one, justify="center")
input_usuario.place(x=170, y=180)

input_password = Entry(frame_one, justify="center", show="*")
input_password.place(x=170, y=260)

#*************** BOTONES LOGIN ************
btn_ingresar = Button(frame_one, text="INGRESAR")
btn_ingresar.place(x=190, y=400)

ventana.mainloop()