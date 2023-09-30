from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
from datetime import datetime
from pygame import mixer
from tkinter import messagebox

# load music for alarming
def play_music():
    mixer.init()
    mixer.music.load(r"C:\Users\MAC\Downloads\Music\despair-metal-trailer-109943.mp3")
    # Replace with the path to your music file
    mixer.music.play()

def stop_music():
    mixer.music.stop()

def set_alarm():
    hour = int(hour_label_input.get())
    minute = int(min_label_input.get())
    second = int(sec_label_input.get())
    period = period_label_input.get()

    # Adjust the hour for 12-hour format
    if period == 'PM' and hour != 12:
        hour += 12
    elif period == 'AM' and hour == 12:
        hour = 0

    alarm_time = datetime.now().replace(hour=hour, minute=minute, second=second)
    alarm_time_str = alarm_time.strftime("%I:%M:%S %p")

    time_difference = alarm_time - datetime.now()
    minutes, seconds = divmod(time_difference.seconds, 60)

    # Display a message with the countdown
    message = f"Alarm set for {minutes} minutes and {seconds} seconds from now."
    messagebox.showinfo("Alarm", message)

    alarm_button.config(state=DISABLED)

    while True:
        if alarm_time_str == datetime.now().strftime("%I:%M:%S %p"):
            print('need to wakeup')
            play_music()
            break

root = Tk()
root.geometry('400x200')
root.config(bg='black')

# create Frame line
frame_line = Frame(root,width=300,height=5,bg='blue')
frame_line.pack(fill=X)

# configure img
img = Image.open('F:\campusx.soln\images.jpg').resize((150,150))
img = ImageTk.PhotoImage(img)

img_label = Label(root,image=img)
img_label.place(x=10,y=15)

alarm_label = Label(root,text='Alarm Clock',width=10,height=2,bg='black',fg='white')
alarm_label.place(x=185,y=10)
alarm_label.config(font=('verdana',18,'bold'))

hour_label = Label(root,text='hour',width=5,height=1,bg='black',fg='white')
hour_label.place(x=170,y=60)
hour_label.config(font=('verdana',10,'bold'))

min_label = Label(root,text='min',width=5,height=1,bg='black',fg='white')
min_label.place(x=220,y=60)
min_label.config(font=('verdana',10,'bold'))

sec_label = Label(root,text='sec',width=5,height=1,bg='black',fg='white')
sec_label.place(x=270,y=60)
sec_label.config(font=('verdana',10,'bold'))

period_label = Label(root,text='period',width=5,height=1,bg='black',fg='white')
period_label.place(x=330,y=60)
period_label.config(font=('verdana',10,'bold'))

hour_label_input = ttk.Combobox(root,width=3,font=('arial',10))
hour_label_input['values'] = ('00','01','02','03','04','05','06','07','08','09','10','11','12')
hour_label_input.place(x=175,y=90)

min_label_input = ttk.Combobox(root,width=3,font=('arial',10))
min_label_input['values'] = [('0'+str(i)) if i < 10 else str(i) for i in range(0, 61)]
min_label_input.place(x=225,y=90)

sec_label_input = ttk.Combobox(root,width=3,font=('arial',10))
sec_label_input['values'] = [('0'+str(i)) if i < 10 else str(i) for i in range(0, 61)]
sec_label_input.place(x=275,y=90)

period_label_input = ttk.Combobox(root,width=4,font=('arial',10))
period_label_input['values'] = ['AM',"PM"]
period_label_input.place(x=330,y=90)

alarm_button = Button(root,text='Set Alarm',font=('arial',10,'bold'),bg='white',fg='black',width=10,command=set_alarm)
alarm_button.place(x=230,y=125)

alarm2_button = Button(root,text='STOP',font=('arial',10,'bold'),bg='white',fg='black',width=10,command=stop_music)
alarm2_button.place(x=230,y=160)

root.mainloop()