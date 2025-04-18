# OP08 Tasks

---

# Домашнее задание в файле My_Tasks_08.py

---


Пишем прогу со списком дел. Добавление, удаление, пометка в списке.

 будем использовать не только функции, которые разбирали в прошлом уроке, но и другие:

 tk.TK() — создание основного окна приложения;
 pack() — метод для управления расположением виджета в окне;
 grid() — метод для расположения виджетов в сетке окна;
 place() — метод для позиционирования виджетов с точными координатами;
 Для создания различных виджетов и их конфигурации:

 tk.Label() — создание текстовой метки;
 tk.Button() — создание кнопки;
 tk.Entry() — создание поля ввода текста;
 tk.Text() — создание многострочного текстового поля;
 tk.Checkbutton() — создание флажка (чекбокса);
 tk.Radiobutton() — создание радиокнопки;
 tk.Listbox() — создание списка для выбора элементов;
 tk.Canvas() — создание холста для рисования графики.
 Для работы с событиями и обработки пользовательского ввода:

 bind() — метод для привязки событий к виджетам;
 get() — метод для получения значения из поля ввода;
 insert() — метод для вставки текста в виджет;
 delete() — метод для удаления части текста из виджета;
 curselection() — метод для получения выбранных элементов из списка или другого виджета;
 itemconfig() — метод для конфигурации отдельных элементов в списке или холсте.

Основные методы `Listbox`

1. **`insert(index, item)`**:
   - Добавляет элемент `item` в `Listbox` на позицию `index`.
   - Пример: `listbox.insert(0, "Первый элемент")` добавляет элемент в начало списка.

2. **`delete(index)`**:
   - Удаляет элемент с позиции `index`.
   - Пример: `listbox.delete(0)` удаляет первый элемент.

3. **`get(index)`**:
   - Возвращает элемент по индексу `index`.
   - Пример: `item = listbox.get(0)` получает первый элемент.

4. **`size()`**:
   - Возвращает количество элементов в `Listbox`.
   - Пример: `count = listbox.size()`.

5. **`curselection()`**:
   - Возвращает кортеж, содержащий индексы выбранных элементов.
   - Пример: `selected_indices = listbox.curselection()`.

6. **`selection_set(index)`**:
   - Устанавливает выделение для элемента с индексом `index`.
   - Пример: `listbox.selection_set(0)` выделяет первый элемент.

7. **`selection_clear(index)`**:
   - Снимает выделение с элемента с индексом `index`.
   - Пример: `listbox.selection_clear(0)` снимает выделение с первого элемента.

8. **`see(index)`**:
   - Прокручивает `Listbox`, чтобы сделать элемент с индексом `index` видимым.
   - Пример: `listbox.see(5)` прокручивает список, чтобы увидеть элемент с индексом 5.

9. **`xview()` и `yview()`**:
   - Эти методы используются для управления прокруткой `Listbox`. `xview` для горизонтальной прокрутки (если это необходимо), `yview` для вертикальной.
   - Пример: `listbox.yview(END)` прокручивает до конца списка.
