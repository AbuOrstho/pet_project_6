# Импорт необходимых модулей
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
import time
import zipfile

# Создание начального окна
root = Tk()
root.title('ZipFile')
root.geometry('400x400+500+200')
root.configure(bg='#497E76')
root.resizable(False, False)


# Функция для создания окна сжатия файла
def compress():
    global compress_file, compress_way, main, file_name
    main = Toplevel(root)
    main.configure(bg='#497E76')
    main.geometry('350x350')
    main.title('Сжать')
    main.resizable(False, False)

    Label(main, text='Выберите файл(ы):', width=17, height=1, bg='#497E76', fg='#26252D',
          font=('Acumin Variable Concept', 9, 'bold')).place(x=0, y=50)
    compress_file = Entry(main, width=30)
    compress_file.place(x=122, y=50)
    Button(main, text='▼', width=2, height=1, command=select_file).place(x=315, y=50)

    Label(main, text='Выберите путь:', width=17, height=1, bg='#497E76', fg='#26252D',
          font=('Acumin Variable Concept', 9, 'bold')).place(x=0, y=100)
    compress_way = Entry(main, width=30)
    compress_way.place(x=122, y=100)
    Button(main, text='▼', width=2, height=1, command=select_way).place(x=315, y=100)

    Label(main, text='Название архива:', width=17, height=1, bg='#497E76', fg='#26252D',
          font=('Acumin Variable Concept', 9, 'bold')).place(x=0, y=150)
    file_name = Entry(main, width=30)
    file_name.place(x=122, y=150)

    image_icon1 = PhotoImage(file='дополнения/icons8-zip-40.png')
    main.iconphoto(False, image_icon1)

    Button(main, text='Сжать', width=10, height=2, font=('Times New Roman', 15, 'bold'), command=way).place(x=110,
                                                                                                            y=200)

    main.mainloop()


# Функция для получения файлов
def select_file(*args):
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                          title='Select',
                                          filetypes=(('All Files', '*.*'),))
    if filename:
        compress_file.insert(END, str(filename) + ',')


# Функция для получения пути сохранения
def select_way():
    global way
    way = filedialog.askdirectory(initialdir=os.getcwd(), title='Select Directory')

    if way:
        compress_way.delete(0, END)
        compress_way.insert(END, str(way))


# Функция для сжатия и сохранения их как архив
def way():
    cf = compress_file.get()[:-1]  # Убираем последнюю запятую из строки с путями файлов
    cw = compress_way.get()
    fn = file_name.get()

    zip_files = cf.split(',')

    if len(zip_files) == 1:
        compressed_file = zipfile.ZipFile(f'{cw}\\{fn}.zip', 'w')
        compressed_file.write(zip_files[0], os.path.basename(zip_files[0]), compress_type=zipfile.ZIP_DEFLATED)
        compressed_file.close()
    elif len(zip_files) > 1:
        compressed_file = zipfile.ZipFile(f'{cw}\\{fn}.zip', 'w')
        for file_path in zip_files:
            compressed_file.write(file_path, os.path.basename(file_path), compress_type=zipfile.ZIP_DEFLATED)
        compressed_file.close()

    progress_bar = ttk.Progressbar(main, orient='horizontal', length=200, mode='determinate')
    progress_bar.place(x=75, y=300)
    progress_bar.start()
    for i in range(0, 101, 8):
        time.sleep(0.1)  # Имитируем загрузку задачи
        progress_bar['value'] = i  # Устанавливаем текущее значение ProgressBar
        root.update_idletasks()  # Обновляем окно, чтобы обновления ProgressBar отобразились
    progress_bar.stop()  # Останавливаем ProgressBar после завершения задачи
    progress_bar.destroy()
    Label(main, text='Завершено', bg='#497E76', fg='black', font=('Acumin Variable Concept', 20, 'bold')).place(x=100,
                                                                                                                y=300)


# Функция для создания окна распаковки файла
def unpack():
    global unpack_file, unpack_way, window
    window = Toplevel(root)
    window.configure(bg='#497E76')
    window.geometry('350x350')
    window.title('Рспаковать')
    window.resizable(False, False)

    Label(window, text='Выберите файл:', width=17, height=1, bg='#497E76', fg='#26252D',
          font=('Acumin Variable Concept', 9, 'bold')).place(x=0, y=50)
    unpack_file = Entry(window, width=30)
    unpack_file.place(x=122, y=50)
    Button(window, text='▼', width=2, height=1, command=select_file1).place(x=315, y=50)

    Label(window, text='Выберите путь:', width=17, height=1, bg='#497E76', fg='#26252D',
          font=('Acumin Variable Concept', 9, 'bold')).place(x=0, y=100)
    unpack_way = Entry(window, width=30)
    unpack_way.place(x=122, y=100)
    Button(window, text='▼', width=2, height=1, command=select_way1).place(x=315, y=100)

    Button(window, text='Распаковать', width=10, height=2, font=('Times New Roman', 15, 'bold'),
           command=unpack_files).place(x=110,
                                       y=200)
    window.mainloop()


# Функция для получения файла который нужно распаковать
def select_file1(*args):
    global filename1
    filename1 = filedialog.askopenfilename(initialdir=os.getcwd(),
                                           title='Select',
                                           filetypes=(('ZIP Files', '*.zip'),))
    if filename1:
        unpack_file.delete(0, END)
        unpack_file.insert(END, str(filename1))


# Функция для пути распаковки
def select_way1(*args):
    global unpack_way1
    unpack_way1 = filedialog.askdirectory(initialdir=os.getcwd(), title='Select Directory')

    if unpack_way1:  # Проверяем, чтобы была выбрана директория, чтобы избежать ошибки при нажатии "Отмена"
        unpack_way.delete(0, END)
        unpack_way.insert(END, str(unpack_way1))


# Функция для распаковки архива и сохранения их в указанную папку
def unpack_files():
    uf = unpack_file.get()
    uw = unpack_way.get()

    fantasy_zip = zipfile.ZipFile(f'{uf}')
    fantasy_zip.extractall(f'{uw}')
    fantasy_zip.close()
    progress_bar = ttk.Progressbar(window, orient='horizontal', length=200, mode='determinate')
    progress_bar.place(x=75, y=300)

    progress_bar.start()
    for i in range(0, 101, 8):
        time.sleep(0.1)  # Имитируем загрузку задачи
        progress_bar['value'] = i  # Устанавливаем текущее значение ProgressBar
        root.update_idletasks()  # Обновляем окно, чтобы обновления ProgressBar отобразились
    progress_bar.stop()  # Останавливаем ProgressBar после завершения задачи
    progress_bar.destroy()
    Label(window, text='Завершено', bg='#497E76', fg='black', font=('Acumin Variable Concept', 20, 'bold')).place(x=100,
                                                                                                                  y=300)


# Создание виджетов для начального окна
image_icon = PhotoImage(file='дополнения/icon.png')
root.iconphoto(False, image_icon)

Label(root, text='ZipFile', font=('Acumin Variable Concept', 20, 'bold'), bg='#497E76', fg='#26252D').place(x=150, y=30)

zipper_icon = PhotoImage(file='дополнения/icons8-zip-80.png', )
zipper = Button(root, image=zipper_icon, bg='#497E76', bd=0, command=compress)
zipper.place(x=50, y=100)

Label(root, text='Сжать', font=('Acumin Variable Concept', 15, 'bold'), bg='#497E76', fg='#26252D').place(x=58, y=180)

ar_icon = PhotoImage(file='дополнения/icons8-архив-80.png')
ar = Button(root, image=ar_icon, bg='#497E76', bd=0, command=unpack)
ar.place(x=270, y=100)

Label(root, text='Распаковать', font=('Acumin Variable Concept', 15, 'bold'), bg='#497E76', fg='#26252D').place(x=245,
                                                                                                                y=180)

root.mainloop()
