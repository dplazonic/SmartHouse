from tkinter import *
from tkinter import messagebox
from todo_db_manager.todo_db_manager import *
from time import strftime
import datetime

db = TasksDatabase('tasks.db')

def todomain():

    def populate_list():
        tasks_list.delete(0, END)
        for row in db.fetch():
            tasks_list.insert(END, row)


    def validate_date(date_text):
    
        try:
            datetime.datetime.strptime(date_text, '%d.%m.%Y.')
            return True
        except ValueError:
            return False
    


    def validate_time(time_text):
        
        try:
            datetime.datetime.strptime(time_text, '%H:%M')
            return True
        except ValueError:
            return False
        


    def add_item():
        

        if osoba_text.get() == '' or datum_text.get() == '' or vrijeme_text.get() == '' or zadatak_text.get() == '':
            messagebox.showerror('Polja za unos su prazna', 'Unesite podatke za unos')
        
        elif validate_date(datum_text.get()) == False:
            messagebox.showerror("Polja za unos je neispravno", "Neispravan format datuma - potrebno upsati dd.mm.yyyy.")

        elif validate_time(vrijeme_text.get()) == False:
            messagebox.showerror("Polja za unos neispravno", "Neispravan format vremena - potrebno upsati hh:mm")

        else:
            db.insert(osoba_text.get(), datum_text.get(),
                    vrijeme_text.get(), zadatak_text.get())
            tasks_list.delete(0, END)
            tasks_list.insert(END, (osoba_text.get(), vrijeme_text.get(),
                                    datum_text.get(), zadatak_text.get()))
            clear_text()
            populate_list()


    def select_item(event):
        try:
            global selected_task
            index = tasks_list.curselection()[0]
            selected_task = tasks_list.get(index)   

            osoba_entry.delete(0, END)
            osoba_entry.insert(END, selected_task[1])
            datum_entry.delete(0, END)
            datum_entry.insert(END, selected_task[2])
            vrijeme_entry.delete(0, END)
            vrijeme_entry.insert(END, selected_task[3])
            zadatak_entry.delete(0, END)
            zadatak_entry.insert(END, selected_task[4])
        except IndexError:
            pass



    def remove_item():
        db.remove(selected_task[0])
        clear_text()
        populate_list()


    def update_item():
        if validate_date(datum_text.get()) == False:
            messagebox.showerror("Polja za unos neispravno", "ne valja date")

        elif validate_time(vrijeme_text.get()) == False:
            messagebox.showerror("Polja za unos neispravno", "ne valja time")
        else:
            db.update(selected_task[0], osoba_text.get(), datum_text.get(),
                    vrijeme_text.get(), zadatak_text.get())
            populate_list()


    def clear_text():
        osoba_entry.delete(0, END)
        datum_entry.delete(0, END)
        vrijeme_entry.delete(0, END)
        zadatak_entry.delete(0, END)

    def temp_text_vrijeme_in(e):
        vrijeme_entry.delete(0,"end")
    # def temp_text_vrijeme_out(e):
    #     vrijeme_entry.insert(0, "format je hh:mm")

    def temp_text_datum_in(e):
        datum_entry.delete(0,"end")
    # def temp_text_datum_out(e):
    #     datum_entry.insert(0, "format je dd.mm.yyyy.")  
    

    todo_window = Toplevel(padx=30)


    todo_window.columnconfigure((0,1,2,3), weight=1)
    todo_window.resizable(False,False)

    osoba_text = StringVar()
    osoba_label = Label(todo_window, text='Osoba', font=('bold', 14), pady=20)
    osoba_label.grid(row=5, column=0)
    osoba_entry = Entry(todo_window, textvariable=osoba_text)
    osoba_entry.grid(row=5, column=1)

    datum_text = StringVar()
    datum_label = Label(todo_window, text='Datum', font=('bold', 14), pady=20)
    datum_label.grid(row=5, column=2)
    datum_entry = Entry(todo_window, textvariable=datum_text)
    datum_entry.insert(0, "format je dd.mm.yyyy.")  
    datum_entry.grid(row=5, column=3)
    datum_entry.bind("<FocusIn>", temp_text_datum_in)
    # datum_entry.bind("<FocusOut>", temp_text_datum_out)

    vrijeme_text = StringVar()
    vrijeme_label = Label(todo_window, text='Vrijeme', font=('bold', 14), pady=20)
    vrijeme_label.grid(row=6, column=0)
    vrijeme_entry = Entry(todo_window, textvariable=vrijeme_text)
    vrijeme_entry.insert(0, "format je hh:mm")  
    vrijeme_entry.grid(row=6, column=1)
    vrijeme_entry.bind("<FocusIn>", temp_text_vrijeme_in)
    # vrijeme_entry.bind("<FocusOut>", temp_text_vrijeme_out)


    zadatak_text = StringVar()
    zadatak_label = Label(todo_window, text='Zadatak', font=('bold', 14), pady=20)
    zadatak_label.columnconfigure((0), weight=1)

    zadatak_label.grid(row=7, column=0)
    zadatak_entry = Entry(todo_window, textvariable=zadatak_text, width=50)
    zadatak_label.columnconfigure((1), weight=1)

    zadatak_entry.grid(row=7, column=1, columnspan=2)


    tasks_list = Listbox(todo_window, height=8, width=80, border=0)
    tasks_list.columnconfigure((0,1,2), weight=1, minsize = 40)
    tasks_list.grid(row=10, column=0, columnspan=3, rowspan=3, pady=20, padx=50)


    scrollbar = Scrollbar(todo_window)
    scrollbar.grid(row=10, column=2,rowspan=3, sticky='ns')

    tasks_list.configure(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=tasks_list.yview)

    tasks_list.bind('<<ListboxSelect>>', select_item)




    add_btn = Button(todo_window, text='Dodaj zadatak', width=12, command=add_item)
    add_btn.grid(row=9, column=0, padx=20, pady=20)

    remove_btn = Button(todo_window, text='Ukloni zadatak', width=12, command=remove_item)
    remove_btn.grid(row=9, column=1)

    update_btn = Button(todo_window, text='Ažuriraj', width=12, command=update_item)
    update_btn.grid(row=9, column=2)

    clear_btn = Button(todo_window, text='Očisti unos', width=12, command=clear_text)
    clear_btn.grid(row=9, column=3)

    todo_window.title('TODO')
    todo_window.geometry('920x600')

    populate_list()

    todo_window.mainloop()


