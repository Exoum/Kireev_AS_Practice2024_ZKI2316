import tkinter as tk
from tkinter import messagebox, ttk, Label, Entry, Button
from utils import choose_color

def setup_ui(root, editor):
  # Создаем главное окно приложения
  root.title("Обработчик изображений")
  root.geometry('600x350')
  root.minsize(600, 350)

  # Создаем фрейм для холста и размещаем его справа
  left_canvas_frame = tk.Frame(root)
  left_canvas_frame.pack(side=tk.LEFT, fill=tk.Y)

  # Создаем фрейм для холста и размещаем его справа
  right_left_canvas_frame = tk.Frame(root)
  right_left_canvas_frame.pack(side=tk.RIGHT, fill=tk.BOTH)

  # Создаем фрейм для инструментов рисования и размещаем его внутри левого фрейма
  tools_frame = tk.Frame(left_canvas_frame)
  tools_frame.pack(fill=tk.X, padx=10, pady=5)

  # Размещаем элементы управления в tools_frame с помощью grid
  Label(tools_frame, text='X1').grid(row=0, column=0, sticky='w')
  entry_x1 = Entry(tools_frame, width=20)
  entry_x1.grid(row=0, column=1, padx=5, pady=5)

  Label(tools_frame, text='Y1').grid(row=1, column=0, sticky='w')
  entry_y1 = Entry(tools_frame, width=20)
  entry_y1.grid(row=1, column=1, padx=5, pady=5)

  Label(tools_frame, text='X2').grid(row=2, column=0, sticky='w')
  entry_x2 = Entry(tools_frame, width=20)
  entry_x2.grid(row=2, column=1, padx=5, pady=5)

  Label(tools_frame, text='Y2').grid(row=3, column=0, sticky='w')
  entry_y2 = Entry(tools_frame, width=20)
  entry_y2.grid(row=3, column=1, padx=5, pady=5)

  color_entry = Entry(tools_frame, width=20, state="readonly")
  color_entry.grid(row=4, column=1, padx=5, pady=5)
  Button(tools_frame, text='Выбрать цвет', command=lambda: choose_color(color_entry)).grid(row=4, column=0, sticky='w')

  Button(tools_frame, text='Нарисовать прямоугольник', command=lambda: editor.draw_rectangle(entry_x1,entry_y1,entry_x2,entry_y2,color_entry)).grid(row=5, column=0, columnspan=2, pady=5)

  # Создаем сепаратор и размещаем его под фреймом инструментов рисования
  separator = ttk.Separator(left_canvas_frame, orient='horizontal')
  separator.pack(fill=tk.X, padx=10, pady=5)

  # Создаем фрейм для группировки элементов управления яркости и резкости и размещаем его под сепаратором
  enhancement_frame = tk.Frame(left_canvas_frame)
  enhancement_frame.pack(fill=tk.X, padx=10, pady=5)

  # Метка и поле ввода для яркости
  Label(enhancement_frame, text="Яркость:").grid(row=0, column=0, sticky="ew")
  brightness_entry = Entry(enhancement_frame, width=25)
  brightness_entry.grid(row=0, column=1, sticky="ew")

  # Кнопка для повышения яркости
  Button(enhancement_frame, text="Повысить яркость", command=lambda: editor.increase_brightness(brightness_entry)).grid(row=1, column=0, columnspan=2, sticky="ew", pady=5)

  # Метка и поле ввода для резкости
  Label(enhancement_frame, text="Резкость:").grid(row=2, column=0, sticky="ew")
  sharpness_entry = Entry(enhancement_frame, width=25)
  sharpness_entry.grid(row=2, column=1, sticky="ew")

  # Кнопка для повышения резкости
  Button(enhancement_frame, text="Повысить резкость", command=lambda: editor.increase_sharpness(sharpness_entry)).grid(row=3, column=0, columnspan=2,sticky="ew", pady=5)

  # Создаем холст
  label = Label(root, bg='lightgray')
  label.pack(fill=tk.BOTH, expand=True)

  editor.label = label

  # Меню
  root.option_add("*tearOff", False)
  menu_bar = tk.Menu(root)
  file_menu = tk.Menu(menu_bar)
  filter_menu = tk.Menu(menu_bar)

  file_menu.add_command(label="Загрузить изображение", command=editor.load_image)
  file_menu.add_command(label="Сделать снимок с веб-камеры", command=editor.capture_image)
  menu_bar.add_cascade(label="Файл", menu=file_menu)

  filter_menu.add_command(label="Красный", command=lambda: editor.apply_color_filter('RED'))
  filter_menu.add_command(label="Зеленый", command=lambda: editor.apply_color_filter('GREEN'))
  filter_menu.add_command(label="Синий", command=lambda: editor.apply_color_filter('BLUE'))
  filter_menu.add_command(label="Оригинальное изображение", command=lambda: editor.apply_color_filter('ORIGINAL'))
  menu_bar.add_cascade(label="Фильтры", menu=filter_menu)

  root.config(menu=menu_bar)
    