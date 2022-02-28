from tkinter import Tk, Button, Label, Entry
import os

DIRECTORY = os.getcwd() #f"F:\Макро\jpg"
count = os.listdir(DIRECTORY)
text = f"В папке {DIRECTORY}: {str(len(count))} файлов"
geometry = "750x230"
description = "Введите в строке имя для файлов. В конце имени будет присоединён порядковый номер.\n" \
              "По умолчанию номера файлов задаются порядковым номером. Нажмите 'применить' без имени файлов"
exten_off = "Введите расширение(без точки), которое не переименуется.\n" \
        "По умолчанию файлы 'exe' не переименовываются"
exten_on = "Введите расширение(без точки), файлы с которым нужно переименовать"

del_spaces = "Чтобы удалить пробелы из названий во всех файлах папки, нажмите кнопку --> \n" \
             "Если файл уже существует, к его названию добавится 'new' и порядковый номер"

def del_spases():
    count = 0
    for root, dirs, files in os.walk(DIRECTORY):
        for name in files:
            path_name = os.path.join(root, name)
            extension = path_name[path_name.rfind(".") + 0:]
            target = name[0: name.rfind(extension)]
            if " " in target:
                target = target.replace(' ', '')
                old_name = os.path.join(root, name)
                new_name = os.path.join(root, target + extension)
                if not os.path.exists(new_name):
                    #print(target + extension)
                    os.rename(old_name, new_name)
                    #print(old_name, new_name)
                else:
                    new_name = os.path.join(root, target + "new" + str(count) + extension)
                    os.rename(old_name, new_name)
                    count += 1



def name():
    text = txt_name.get()
    patt = text.split()
    patt = ''.join(patt)
    patt = patt + " "
    lbl.configure(rename_files(DIRECTORY, patt, ext_off(), ext_on()))

def ext_off():
    text = txt_extension_off.get()
    text = text.split()
    text = ''.join(text)
    text = "." + text
    return text

def ext_on():
    text = txt_extension_on.get()
    text = text.split()
    text = ''.join(text)
    text = "." + text
    return text

def rename_file(root, name, new_name):
    old_name = os.path.join(root, name)
    new_name = os.path.join(root, new_name)
    if not os.path.exists(new_name):
        os.rename(old_name, new_name)
        # print(old_name, new_name, extension)
    # print(old_name, new_name, extension)

def rename_files(DIRECTORY, patt, ext_off, ext_on):
    count = 0
    for root, dirs, files in os.walk(DIRECTORY):
        for name in files:
            path_name = os.path.join(root, name)
            extension = path_name[path_name.rfind(".") + 0:]
            count += 1
            new_name = patt.replace(" ", str(count))
            new_name = new_name + extension

            if extension == ".exe":
                continue
            if ext_off != ".":
                if extension == ext_off:
                    continue
            if ext_on != ".":
                if extension == ext_on:
                    rename_file(root, name, new_name)
                else:
                    continue
            else:
                rename_file(root, name, new_name)


window = Tk()
window.title("Переименование файлов ver_0.21")
window.geometry(geometry)
lbl = Label(window, text=text, font=("Arial", 10))
lbl.grid(column=0, row=0)
btn_name = Button(window, text="применить", font=("Arial", 10), command=name)
btn_name.grid(column=1, row=2)
txt_name = Entry(window, width=30, font=("Arial", 10))
txt_name.grid(column=0, row=2)
lbl_description = Label(window, text=description, font=("Arial", 10))
lbl_description.grid(column=0, row=1)
lbl_extension_off = Label(window, text=exten_off, font=("Arial", 10))
lbl_extension_off.grid(column=0, row=3)
txt_extension_off = Entry(window, width=5, font=("Arial", 10))
txt_extension_off.grid(column=0, row=4)
lbl_extension_on = Label(window, text=exten_on, font=("Arial", 10))
lbl_extension_on.grid(column=0, row=5)
txt_extension_on = Entry(window, width=5, font=("Arial", 10))
txt_extension_on.grid(column=0, row=6)
lbl_del_spaces = Label(window, text=del_spaces, font=("Arial", 10))
lbl_del_spaces.grid(column=0, row=7)
btn_del_spases = Button(window, text="удалить пробелы", font=("Arial", 10), command=del_spases)
btn_del_spases.grid(column=1, row=7)

window.mainloop()

