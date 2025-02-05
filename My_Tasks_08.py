# это программа преподавателя передаланная с записью задач и чтением задач из файла.
# Для продолжения работы без потери списка задач.

import tkinter as tk
from tkinter import messagebox


def add_task():
    task = task_entry.get()  # здесь мы получаем слова из поля для ввода
    if task:
        task_listBox.insert(tk.END, task)  # здесь с помощью константы END вставляем полученное слово в конец списка
        task_entry.delete(0, tk.END)  # здесь очищаем поле для ввода, от нулевого индекса и до конца


def delete_task():
    selected_task = task_listBox.curselection()  # с помощью функции **curselection** элемент, на который мы нажмём, будет передавать свой ID, индекс, в переменную  selected_task
    if selected_task:
        task_listBox.delete(selected_task)  # удаляем выбранный элемент из списка


def mark_task():
    selected_task = task_listBox.curselection()
    if selected_task:
        print(f' выдленная строка {selected_task}')
        task_listBox.itemconfig(selected_task,
                                bg="slate blue")  # с помощью функции **itemconfig** выполненная задача изменит цвет заливки


# Обработчик закрытия окна. Перед закрытием записываем в файл задачи
def on_closing():
    if messagebox.askokcancel("Выход", "Выйти из приложения?"):
        with open("tasks.txt", "w", encoding="utf-8") as file:  # отрываем для записи
            for i in range(task_listBox.size()):
                line = task_listBox.get(i)
                # print(line)
                if len(line) > 0:
                    line += '\n'
                    file.write(line)

        with open("sel_tasks.txt", "w", encoding="utf-8") as file:  # отрываем для записи выбранных задач
            # print('Выделенные')
            for i in range(task_listBox.size()):
                bg_color = task_listBox.itemcget(i, 'bg')
                print(bg_color)
                if bg_color == 'slate blue':
                    line = task_listBox.get(i)
                    line += '\n'
                    file.write(line)

        root.destroy()


root = tk.Tk()
# Устанавливаем обработчик события закрытия окна
root.protocol("WM_DELETE_WINDOW", on_closing)

root.title("Список задач")

root.configure(background="HotPink")

text1 = tk.Label(root, text="Введите вашу задачу:", bg="HotPink")
text1.pack(pady=5)

task_entry = tk.Entry(root, width=30, bg="DeepPink1")
task_entry.pack(pady=10)

add_task_button = tk.Button(root, text="Добавить задачу", command=add_task)
add_task_button.pack(pady=5)

delete_button = tk.Button(root, text="Удалить задачу", command=delete_task)
delete_button.pack(pady=5)

mark_button = tk.Button(root, text="Отметить выполненную задачу", command=mark_task)
mark_button.pack(pady=5)

text2 = tk.Label(root, text="Список задач:", bg="HotPink")
text2.pack(pady=5)

task_listBox = tk.Listbox(root, height=10, width=50, bg="LightPink1")
task_listBox.pack(pady=10)

# Открываем файл для чтения списка задач
with open("tasks.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.replace("\n", "")
        if len(line) > 0:
            task_listBox.insert(tk.END, line)
        print(line, ' ', len(line), ' ', line.isprintable())
print(task_listBox.size())

# Открываем файл для чтения отмеченного списка задач
with open("sel_tasks.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.replace("\n", "")
        if len(line) > 0:
            for i in range(task_listBox.size()):
                if line == task_listBox.get(i):
                    print(line)
                    task_listBox.itemconfig(i, bg="slate blue")

root.mainloop()
