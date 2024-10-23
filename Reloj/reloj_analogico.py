from tkinter import Tk, Canvas, PhotoImage
import time
import math

window = Tk()
window.title("Reloj Analogico")
window.geometry("700x690")
canvas = Canvas(window, width=700,height=690,background="#566B7C")
canvas.pack()
background_reloj = PhotoImage(file="reloj.png")
canvas.create_image(5,0,anchor="nw", image=background_reloj)



def update_clock():
    canvas.delete("hands")  # Limpia las manecillas anteriores

    # Obtiene la hora actual
    now = time.localtime()
    hour = now.tm_hour % 12
    minute = now.tm_min
    second = now.tm_sec

    # Calcula los ángulos de las manecillas
    hour_angle = math.radians((hour + minute / 60) * 30) - math.pi / 2
    minute_angle = math.radians(minute * 6) - math.pi / 2
    second_angle = math.radians(second * 6) - math.pi / 2

    # Coordenadas del centro del reloj
    center_x, center_y = 350, 345

    # Dibuja la manecilla de la hora
    canvas.create_line(center_x, center_y,
                       center_x + 150 * math.cos(hour_angle),  # Increased length
                       center_y + 150 * math.sin(hour_angle), fill="#F09017", width=20, tags="hands")

    # Dibuja la manecilla del minuto
    canvas.create_line(center_x, center_y,
                       center_x + 230 * math.cos(minute_angle),  # Increased length
                       center_y + 230 * math.sin(minute_angle), fill="#DD3A0F", width=20, tags="hands")

    # Dibuja la manecilla del segundo
    canvas.create_line(center_x, center_y,
                       center_x + 250 * math.cos(second_angle),  # Increased length
                       center_y + 250 * math.sin(second_angle), fill="#8096BF", width=15, tags="hands")

    window.after(1000, update_clock)  # Actualiza el reloj cada segundo


update_clock()
window.mainloop()