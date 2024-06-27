from tkinter import colorchooser

def choose_color(color_entry):

  # Открываем диалог выбора цвета и устанавливаем выбранный цвет в поле ввода
  color_code = colorchooser.askcolor(title ="Choose color")
  color_entry.configure(state="normal")
  color_entry.delete(0, 'end')
  color_entry.insert(0, color_code[1])
  color_entry.configure(state="readonly")