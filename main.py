import tkinter as tk
from ui import setup_ui
from image_processing import ImageEditor

def main():
    root = tk.Tk()
    editor = ImageEditor(root)
    setup_ui(root, editor) 
    
  # Запускаем главный цикл приложения
    root.mainloop()

if __name__ == "__main__":
    main()
