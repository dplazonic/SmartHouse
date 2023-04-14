import tkinter as tk
from tkinter import *
from db_comm import save_data, get_data
from web_api import *
from Klase import *
from time import strftime
from todo_db_manager.todo_db_manager import *
from todo import *

db = TasksDatabase('tasks.db')


#weather_data = retrieve_data_weather()

def stanje_hvac():
    stanje_hvac_data = get_data("hvac")[0]
    if stanje_hvac_data ==0:
        stanje2 = "Ugašeno"
    else:
        stanje2 = f"Upaljeno, Temperatura je {stanje_hvac_data} °C"
  
    hvac_stanje.config(text=stanje2)
    hvac_stanje.after(2000, stanje_hvac)

def stanje_svijetla():
    stanje_svijetla_data = get_data("svijetla")[0]
    if stanje_svijetla_data ==0:
        stanje2 = "Ugašeno"
    elif stanje_svijetla_data == 100:
        stanje2 = "Upaljeno"
    else:
        stanje2 = "Prigušeno"
    svijetlo_stanje.config(text=f"Svijetlo je: {stanje2}")
    svijetlo_stanje.after(2000, stanje_svijetla)

def stanje_rolete():
    stanje_rolete_data = get_data("roleta")[0]
    if stanje_rolete_data ==0:
        stanje1 = "Zatvorena"
    elif stanje_rolete_data == 100:
        stanje1 = "Otvorena"
    else:
        stanje1 = "Djelomično otvorena"
    rolete_stanje.config(text=f"Roleta je: {stanje1}")
    rolete_stanje.after(2000, stanje_rolete)
    
def clock():
    time_string = strftime('%H:%M:%S\n%d %B\n%A')  
    l1_clock.config(text=time_string)
    l1_clock.after(1000,clock) 

# def weather():
#     weather_data = retrieve_data_weather()
#     main_label_centar.config(text=weather_data)
#     main_label_centar.after(600000, weather)
#     print(weather_data)
    
def otvori(name):
    save_data(name, 30)

def zatvori(name):
    save_data(name, 0)

def automatic():

    if radiobutton_var.get() == 2:
        rolete.config(state="disabled")
        svijetla.config(state="disabled")
        hvac.config(state="disabled")

        # if int(weather_data.temperature[:2]) < 16:
        #     save_data("hvac", 20)

        # if weather_data.is_day == 0:
        #     save_data("roleta", 0)
        #     save_data("svijetla", 100)



    else:
        rolete.config(state="normal")
        svijetla.config(state="normal")
        hvac.config(state="normal")

def postavke(funkcija, true, false):
    postavke = tk.Tk()
    postavke.title(f"Postavke {funkcija}")
    Otvori = tk.Button(postavke, text=true, command= lambda: otvori(funkcija))
    Zatvori = tk.Button(postavke, text=false, command= lambda: zatvori(funkcija))

    Otvori.pack(padx=5, pady=5)
    Zatvori.pack(padx=5, pady=5)

    slider = tk.Scale(postavke, from_=0, to=100, orient=tk.HORIZONTAL, length=200, label=funkcija)
    value = get_data(funkcija)
    slider.set(value)
    slider.pack(pady=20)
    slider.bind("<ButtonRelease-1>", lambda event: save_data(funkcija, slider.get()))

def postavke_hvac(funkcija, true, false):
    postavke_hvac = tk.Tk()
    postavke_hvac.title(f"Postavke {funkcija}")
    Otvori = tk.Button(postavke_hvac, text=true, command= lambda: otvori(funkcija))
    Zatvori = tk.Button(postavke_hvac, text=false, command= lambda: zatvori(funkcija))

    Otvori.pack(padx=5, pady=5)
    Zatvori.pack(padx=5, pady=5)

    slider = tk.Scale(postavke_hvac, from_=17, to=30, orient=tk.HORIZONTAL, length=200, label=funkcija)
    value = get_data(funkcija)
    slider.set(value)
    slider.pack(pady=20)
    slider.bind("<ButtonRelease-1>", lambda event: save_data(funkcija, slider.get()))
    

root = tk.Tk()
root.geometry("600x400")
root.title("Smart Home")

main_label_frame_lijevi = tk.LabelFrame(root, text="Postavke", labelanchor="n")
main_label_frame_lijevi.place(relx=0.95, rely=0, anchor="ne")

radiobutton_var = tk.IntVar()

manual_cb = tk.Radiobutton(main_label_frame_lijevi,text = "Manual", variable=radiobutton_var, value=1, command=automatic)
manual_cb.grid(row=4, column=1, pady=5)

automatic_cb = tk.Radiobutton(main_label_frame_lijevi,text = "Automatic",variable=radiobutton_var, value=2, command=automatic)
automatic_cb.grid(row=5, column=1, pady=5)
automatic_cb.select()



rolete_stanje = tk.Label(main_label_frame_lijevi, text=f"Roleta je: ")
rolete_stanje.grid(column=1, row=6)

svijetlo_stanje = tk.Label(main_label_frame_lijevi, text=f"Svijetlo je: ")
svijetlo_stanje.grid(column=1, row=7)

hvac_stanje = tk.Label(main_label_frame_lijevi, text=f"")
hvac_stanje.grid(column=1, row=8)

rolete = tk.Button(main_label_frame_lijevi, text="Rolete", width=10, command= lambda: postavke("Roleta","Otvori","Zatvori"))
rolete.grid(row=1, column=1, pady=5)

svijetla = tk.Button(main_label_frame_lijevi, text="Svijetla", width=10,command= lambda: postavke("Svijetla","Upali","Ugasi"))
svijetla.grid(row=2, column=1, pady=5)

hvac = tk.Button(main_label_frame_lijevi, text="HVAC", width=10, command= lambda: postavke_hvac("HVAC","Upali","Ugasi"))
hvac.grid(row=3, column=1, pady=5)

l1_clock = tk.Label(root)
l1_clock.place(relx=0.2, rely=0, anchor="n")




main_label_centar = tk.Label(root, text = "")
main_label_centar.place(relx=0.5, rely=0.0, anchor="ne")



# # -------TODO-------

main_label_frame_desni = tk.LabelFrame(root, text="TO-DO", labelanchor="n")
main_label_frame_desni.place(relx=0.05, rely=0.2, anchor="nw", width=320)

# to_do_lable = tk.Label(main_label_frame_desni, text="")
# to_do_lable.grid(row=0, column=0)

lista_zadataka = Listbox(main_label_frame_desni, height=10, width=49, border=1)
lista_zadataka.grid (row=1, column=0)

scrollbar = Scrollbar(main_label_frame_desni)
scrollbar.grid(row=1, column=3, sticky='ns')
lista_zadataka.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=lista_zadataka.yview)






def populate_list():
    lista_zadataka.delete(0, END)
    for row in db.fetch():
        lista_zadataka.insert(END, row)
    lista_zadataka.after(2000, populate_list)




    

todo_button = tk.Button(main_label_frame_desni, text="Postavke zadataka", width=15, command=todomain)
todo_button.grid(row=5, column=0, pady=5)
 


 
automatic()
stanje_hvac()
stanje_rolete()
stanje_svijetla()
#weather()
clock()
populate_list()

root.mainloop()
