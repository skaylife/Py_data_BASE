from tkinter import *
from tkinter import messagebox
from db import Databese

# Py to Exe CMD "pyinstaller --windowed -F main.py"

db = Databese('store.db')


def populate_list():
    part_list.delete(0, END)
    for row in db.fetch():
        part_list.insert(END, row)

def add_item():
    if part_text.get() == '' or author_text.get() == '' or market_text.get() == '' or price_text.get() == '':
        messagebox.showerror('Ошибка поля', 'Заполните все поля пожалуйста')
        return
    db.insert(part_text.get(), author_text.get(),
              market_text.get(), price_text.get())
    part_list.delete(0, END)
    part_list.insert(END, (part_text.get(), author_text.get(),
                           price_text.get(), market_text.get()))
    clear_text()
    populate_list()


def select_item(event):
    try:
        global selected_item
        index = part_list.curselection()[0]
        selected_item = part_list.get(index)

        part_entry.delete(0, END)
        part_entry.insert(END, selected_item[1])

        author_entry.delete(0, END)
        author_entry.insert(END, selected_item[2])

        market_entry.delete(0, END)
        market_entry.insert(END, selected_item[3])

        price_entry.delete(0, END)
        price_entry.insert(END, selected_item[4])
    except IndexError:
        pass

def remove_item():
    db.remove(selected_item[0],)
    clear_text()
    populate_list()

def update_item():
    db.update(selected_item[0], part_text.get(), author_text.get(),
                            market_text.get(), price_text.get())
    populate_list()



def clear_text():
    part_entry.delete(0, END)
    author_entry.delete(0, END)
    market_entry.delete(0, END)
    price_entry.delete(0, END)

# Создание объекта окна
app = Tk()

# Текст
part_text = StringVar()
part_label = Label(app, text='Название', font=('bold, 10'), pady=20)
part_label.grid(row=0, column=0, sticky=W)
part_entry = Entry(app, textvariable=part_text)
part_entry.grid(row=0, column=1)

# Автор
author_text = StringVar()
author_label = Label(app, text='Автор', font=('bold, 10'))
author_label.grid(row=0, column=2, sticky=W)
author_entry = Entry(app, textvariable=author_text)
author_entry.grid(row=0, column=3)

# Магазин
market_text = StringVar()
market_label = Label(app, text='Магазин', font=('bold, 10'))
market_label.grid(row=1, column=0, sticky=W)
market_entry = Entry(app, textvariable=market_text)
market_entry.grid(row=1, column=1)

# Цена
price_text = StringVar()
price_label = Label(app, text='Цена', font=('bold, 10'))
price_label.grid(row=1, column=2, sticky=W)
price_entry = Entry(app, textvariable=price_text)
price_entry.grid(row=1, column=3)

# Лист с информацие, какие товары добавленны
part_list = Listbox(app, height=8, width=70, border=0)
part_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)

# Скроллбар
scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=3)

# Завфиксировать скроллбар в листбоксе
part_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=part_list.yview)

# Выделиение лист бокса
part_list.bind('<<ListboxSelect>>', select_item)



# Кнопки
add_btn = Button(app, text='Добавить товар', width=15, command=add_item)
add_btn.grid(row=2, column=0, pady=20)

remove_btn = Button(app, text='Удалить товар', width=15, command=remove_item)
remove_btn.grid(row=2, column=1)

update_btn = Button(app, text='Изменить товар', width=15, command=update_item)
update_btn.grid(row=2, column=2)

clear_btn = Button(app, text='Стереть товар', width=15, command=clear_text)
clear_btn.grid(row=2, column=3)



app.title('База данных')
app.geometry('700x350')


# Лист с базой данных
populate_list()


# To create an executable, install pyinstaller and run
# '''
# pyinstaller --onefile --add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk' --add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl' part_manager.py
# '''



# Запуск программы бесконечный цикл
app.mainloop()