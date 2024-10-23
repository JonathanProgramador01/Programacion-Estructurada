import os
from datetime import datetime
from tkinter import Tk, Canvas, PhotoImage
import pytz
from tkcalendar import Calendar




timezones = [
    ('Alemania', 'Europe/Berlin'),
    ('Brazil', 'America/Sao_Paulo'),
    ('Canada', 'America/Toronto'),
    ("Mexico","America/Mexico_City"),
    ('Egypt', 'Africa/Cairo'),
    ('Japan', 'Asia/Tokyo'),
    ('London', 'Europe/London'),
    ('Switzerland', 'Europe/Zurich'),
    ('Ukraine', 'Europe/Kiev'),
    ('USA', 'America/New_York')
]

window = Tk()
window.title("World Clocks")
window.geometry("1920x1080")

canvas = Canvas(window,width=1300,height=700,bg="#191A19")
canvas.pack()
canvas.create_text(160,0,anchor="nw",fill="#4E9F3D",text="World Clocks", font=("Elephant",100,"bold"))

bandera_dir = "Banderas/"

imagenes = [] # Para guardar las referencias de mis imagenes
text_items = [] #Este es para guardar mis canvas para despues poder modificarlos
banderas  = [f for f in os.listdir(bandera_dir)]

z = 0
y = 180
for i in range(3):
    x = 20
    if not i:
        rango = 4
    else:
        rango = 3
    for j in range(rango):

        china_timezone = pytz.timezone(timezones[z][1])
        hora = datetime.now(china_timezone)

        image = PhotoImage(file=f"{bandera_dir}{banderas[z]}")
        imagenes.append(image)
        canvas.create_image(x,y,anchor="nw",image=image)
        canvas.create_text(x+150,y, anchor="nw", text=timezones[z][0].split(".")[0],fill="#D8E9A8", font=("Arial",17))
        time_text= canvas.create_text(x+150,y+50,anchor="nw",text=hora.strftime("%H:%M:%S"),font=("Arial",17),fill="#D8E9A8")
        date_text = canvas.create_text(x + 150, y + 80, anchor="nw", text=hora.strftime("%Y-%m-%d"), font=("Arial", 17),
                           fill="#D8E9A8")
        text_items.append((time_text,date_text))
        x += 310
        z += 1
    y += 190

def update_canvas_text():
    z = 0
    for i in range(3):
        if not i:
            rango = 4
        else:
            rango = 3
        for j in range(rango):

            timezone = pytz.timezone(timezones[z][1])
            hora = datetime.now(timezone)

            time_text, date_text = text_items[z]
            canvas.itemconfig(time_text, text=hora.strftime("%H:%M:%S"))
            canvas.itemconfig(date_text, text=hora.strftime("%Y-%m-%d"))
            z += 1

    window.after(1000, update_canvas_text)



year = int(datetime.now().strftime("%Y"))
month = int(datetime.now().strftime("%m"))
day = int(datetime.now().strftime("%d"))
cal = Calendar(
    window,
    selectmode='day',
    year=2024,
    month=10,
    day=14,
    background='#D8E9A8',
    foreground='#191A19',
    headersbackground='#4E9F3D',
    headersforeground='#FFFFFF',
    normalbackground='#D8E9A8',
    normalforeground='#191A19',
    weekendbackground='#1E5128',
    weekendforeground='#FFFFFF',
    font=("Arial", 12)
)
cal.place(x=950,y=465)


update_canvas_text()
window.mainloop()