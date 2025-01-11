import tkinter as tk
import tkinter.ttk as ttk

def insert_time_entry3():
    e3.delete(0, tk.END)
    s_mg = e1.get()
    print(s_mg); print(type(s_mg))
    s = float(s_mg)
    print(s); print(type(s))
    #s_mg = list(s_mg)
    #print(s_mg); print(type(s_mg))
    #s = float(s_mg.pop(0))
    #print(s); print(type(s))

    v = float(e2.get())
    t_mg = (s/v)*60
    t_mg1 = round(t_mg, 2)
    e3.insert(0, t_mg1)
    print(t_mg1); print(type(t_mg1))

    #tablica.insert(parent='', index='end', iid=tablica.id, text='Участок: ' + str(tablica.iid), values=(e1.get, e2.get, t_mg))

    return t_mg

def tabl_insert():
    tablica.insert(parent='', index='end', iid=tablica.iid, text="Участок: " + str(tablica.id),
                   values=(e0.get(), e1.get(), e2.get(), e3.get()))

    tablica.iid += 1
    tablica.id += 1

def tabl_select_del():
    dannye = tablica.selection()
    tablica.delete(dannye)
    print(dannye)
    for i in dannye:
        print(tablica.delete(i))
        #print(type(dannye))




    #for i in dannye:
     #   print('Общее время: ', tablica.item(i, 'values'))
      #  print(type(dannye))











def t_obchee():
    dannye = tablica.selection()
    # print(dannye)
    l_s = list()
    for i in dannye:
        ##print('Строка данные: ', tablica.item(i, 'values')[3])
        x = tablica.item(i, 'values')[3]
        print(x); print(type(x))

        x_sum = float(x); print(x_sum); print(type(x_sum))

        l_s.append(x); print(l_s); print(type(l_s))
        w_s = list(map(float, l_s)); print(w_s); print(type(w_s))
        s_sum = sum(w_s); print('Общее время= ', s_sum); print(type(s_sum)) #общее время марша!! float
        s_sum1 = round(s_sum, 1)                               #округлил до первого знака

        e4.delete(0, tk.END)
        e4.insert(0, s_sum1)



        s_s_sum1 = str(s_sum1); print(s_s_sum1); print(type(s_s_sum1)) #float -> str
        s1_s_sum1 = s_s_sum1.replace('.', ''); print(s1_s_sum1); print(type(s1_s_sum1)) # убрал '.', str

        l_s_sum1 = list(s1_s_sum1); print(l_s_sum1); print(type(l_s_sum1)) #str->list  130 -> ['1','3','0']

#Радотаем с дробной частью (находим секунды)
        m_l_s_sum1 = int(l_s_sum1[-1]) * 6;                  #взяди последний элемент, list -> int и находим секунды
        print('Секунды=', m_l_s_sum1); print(type(m_l_s_sum1))

# Радотаем с целой частью (находим часы и минуты)
        l_s_sum1.pop(-1); print(l_s_sum1); print(type(l_s_sum1)) #убрали последний элимент
        s2_s_sum1 = ''.join(l_s_sum1); print(s2_s_sum1); print(type(s2_s_sum1)) #из ['1' '3' '5'] list делаем [135] str
        h_s_sum1 = int(s2_s_sum1);  print('Всего минут:', h_s_sum1); print(type(h_s_sum1))             #str -> int




        l5.config(text=f'Время: {h_s_sum1} мин. {m_l_s_sum1} сек.')





#def s_obchee():
    dannye = tablica.selection()
    # print(dannye)
    l_t = list()
    for i in dannye:
        ##print('Строка данные: ', tablica.item(i, 'values')[3])
        x = tablica.item(i, 'values')[1]
        print(x); print(type(x))

        x_sum = float(x); print(x_sum); print(type(x_sum))

        l_t.append(x); print(l_t); print(type(l_t))
        w_t = list(map(float, l_t)); print(w_t)
        t_sum = sum(w_t); print(t_sum); print(type(t_sum))
        t_sum1 = round(t_sum, 1)                           # общее растояние марша!!!!1

        e5.delete(0, tk.END)
        e5.insert(0, t_sum1)

    s_t_sum1 = str(t_sum1)                  #; print(s); print(type(s))
    s1_t_sum1 = s_t_sum1.replace('.', '')   #; print(s1); print(type(s1))

    l_t_sum1 = list(s1_t_sum1)#; print(l); print(type(l))

    m_l_t_sum1 = int(l_t_sum1[-1]) * 100; print(m_l_t_sum1)#; print(type(m))

    l_t_sum1.pop(-1)#; print(l); print(type(l))

    s2_t_sum1 = ''.join(l_t_sum1)#; print(s2); print(type(s2))

    h_t_sum1 = int(s2_t_sum1); print(h_t_sum1)#; print(type(h))

    l4.config(text=f'Растояние: {h_t_sum1} км. {m_l_t_sum1} м.')





root = tk.Tk()

root.geometry('700x700+50+10')
root.title('Route_MG')

l0 = tk.Label(root, text='Название участка')
l0.place(x=10, y=5)
e0 = tk.Entry(root)
e0.place(x=137, y=5)

l1 = tk.Label(root, text='Расстояние (км)')
l1.place(x=10, y=35)
e1 = tk.Entry(root)
e1.place(x=137, y=35)

l2 = tk.Label(root, text='Скорость (км/ч)')
l2.place(x=10, y=65)
e2 = tk.Entry(root)
e2.config(state='normal')
e2.place(x=137, y=65)

l3 = tk.Label(root, text='Время участка (минут)')
l3.place(x=310, y=5)
e3 = tk.Entry(root)
e3.config(state='normal')
e3.place(x=310, y=35)

#spisok = ('Республики', 'Мира', 'Матросова')
#cb = ttk.Combobox(root, values=spisok)
#cb.place(x=150, y=350)


b1 = tk.Button(root, text='Расчет', width=10, height=1)
b1.place(x=345, y=60)
b1.configure(command = insert_time_entry3)

b2 = tk.Button(root, text='Вставить', width=10, height=1)
b2.place(x=545, y=60)
b2.configure(command=tabl_insert)

b3 = tk.Button(root, text='Считать', width=10, height=1)
b3.place(x=20, y=350)
b3.configure(command=tabl_select_del)

b4 = tk.Button(root, text='Расчет: Общее растояние и время', width=42, height=1)
b4.place(x=300, y=395)
b4.configure(command=t_obchee)
e4 = tk.Entry(root)              #общее время
e4.config(state='normal')
e4.place(x=530, y=330, width=120)

#b5 = tk.Button(root, text='Общее растояние', width=15, height=1)
#b5.place(x=300, y=355)
#b5.configure(command=s_obchee)
e5 = tk.Entry(root)              #общее растояние
e5.config(state='normal')
e5.place(x=300, y=330, width=128)


l4 = tk.Label(root)
l4['text'] = f'Растояние: {0} км. {0} м.'
l4.place(x=300, y=365)

#l4 = tk.StringVar()
#l4 = tk.Label(root, textvariable=l4_text)
#l4.place(x=300, y=365)

l5 = tk.Label(root, text=f'Время: {0} ч. {0} мин.')
l5.place(x=500, y=365)




s = e1.get()
print(type(s))
s = list(s)
print(type(s))
print(s)
s11 = list(map(int, s))
print(type(s11))
print(s11)


#colonki = ("#1", "#2", "#3")
tablica = ttk.Treeview(root)# , show= "headings", columns=colonki)
tablica['columns'] = ('Наименование', 'Расстояние', 'Скорость', 'Время')
tablica.place(x=50, y=100)

tablica.column('#0', width=120, minwidth=25)
tablica.column('Наименование', width=120)
tablica.column('Расстояние', width=120)
tablica.column('Скорость', width=120)
tablica.column('Время', width=120)

#Заголовки
tablica.heading('#0', text='Label')
tablica.heading('Наименование', text='Наименование')
tablica.heading('Расстояние', text='Растояние',)
tablica.heading('Скорость', text='Скорость')
tablica.heading('Время', text='Время')

tablica.id = 0
tablica.iid = 0

#Добавляем данные в таблицу
#tablica.insert(parent='', index='end', iid=tablica.id,\
#               text="Участок: " + str(tablica.iid),\
#               values=(e1.get, e2.get, insert_time_entry3))


#tablica.pack()

root.mainloop()