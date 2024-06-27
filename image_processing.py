from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageEnhance, ImageDraw
import cv2

class ImageEditor:
  def __init__(self, root):
    self.root = root
    self.image_loaded = False
    self.img = None
    self.label = None

  # Функции для работы с изображениями
  def load_image(self):
    file_path = filedialog.askopenfilename()
    if file_path:
      try:
        self.img = Image.open(file_path)
        self.img.thumbnail((350, 350))
        self.display_image(self.img)
        self.image_loaded = True
      except Exception as e:
        messagebox.showerror("Ошибка загрузки", "Не удалось загрузить изображение: " + str(e))
        self.image_loaded = False

  def capture_image(self):
    # Подключаемся к веб-камере
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
      print("Не удалось подключиться к камере.")
      return

    # Делаем снимок
    ret, frame = cap.read()
    if ret:
      # Сохраняем изображение
      cv2.imwrite('snapshot.jpg', frame)
      self.img = Image.open('snapshot.jpg')
      self.img.thumbnail((350, 350))
      self.display_image(self.img)
      print("Снимок сделан и сохранен как snapshot.jpg")
      self.image_loaded = True
    else:
      print("Не удалось сделать снимок.")
      self.image_loaded = False

    # Освобождаем камеру
    cap.release()
    cv2.destroyAllWindows()

  def display_image(self, img):
    tk_image = ImageTk.PhotoImage(img)
    self.label.image = tk_image
    self.label.config(image=tk_image)

  def apply_color_filter(self, color):
    if self.img and self.image_loaded:
      red, green, blue = self.img.split()
      empty_pixels = red.point(lambda _: 0)

      if color == 'RED':
        filtered_img = Image.merge("RGB", (red, empty_pixels, empty_pixels))
      elif color == 'GREEN':
        filtered_img = Image.merge("RGB", (empty_pixels, green, empty_pixels))
      elif color == 'BLUE':
        filtered_img = Image.merge("RGB", (empty_pixels, empty_pixels, blue))
      elif color == 'ORIGINAL':
        filtered_img = self.img
      else:
        print("Выбран неизвестный цвет.")
        return

      self.display_image(filtered_img)
    else:
      print("Изображение не загружено.")

  def increase_brightness(self, brightness_entry):
    if not self.image_loaded:
      messagebox.showerror("Ошибка", "Изображение не загружено.")
      return

    try:
      brightness_value = brightness_entry.get()
      if brightness_value:
        brightness_value = float(brightness_value)
        if brightness_value > 0:
          enhancer = ImageEnhance.Brightness(self.img)
          brightened_image = enhancer.enhance(brightness_value)
          self.display_image(brightened_image)
        else:
          messagebox.showerror("Ошибка", "Значение яркости должно быть больше 0")
      else:
        messagebox.showerror("Ошибка", "Поле яркости не должно быть пустым")
    except ValueError:
      messagebox.showerror("Ошибка", "Введено некорректное значение яркости")
    except Exception as e:
      messagebox.showerror("Ошибка", "Произошла ошибка при изменении яркости: " + str(e))

  # Функция для повышения резкости изображения
  def increase_sharpness(self, sharpness_entry):
    if not self.image_loaded:
      messagebox.showerror("Ошибка", "Изображение не загружено.")
      return

    try:
      sharpness_value = sharpness_entry.get()
      if sharpness_value:
        sharpness_value = float(sharpness_value)
        if sharpness_value > 0:
          enhancer = ImageEnhance.Sharpness(self.img)
          sharpened_image = enhancer.enhance(sharpness_value)
          self.display_image(sharpened_image)
        else:
          messagebox.showerror("Ошибка", "Значение резкости должно быть больше 0")
      else:
        messagebox.showerror("Ошибка", "Поле резкости не должно быть пустым")
    except ValueError:
      messagebox.showerror("Ошибка", "Введено некорректное значение резкости")
    except Exception as e:
      messagebox.showerror("Ошибка", "Произошла ошибка при изменении резкости: " + str(e))

  # Функция для рисования прямоугольника на изображении
  def draw_rectangle(self, entry_x1, entry_y1, entry_x2, entry_y2, color_entry):
    if not self.image_loaded:
      messagebox.showerror("Ошибка", "Изображение не загружено.")
      return

    try:
      x1 = int(entry_x1.get())
      y1 = int(entry_y1.get())
      x2 = int(entry_x2.get())
      y2 = int(entry_y2.get())

      if x1 >= x2 or y1 >= y2:
        raise ValueError("Координаты прямоугольника введены некорректно.")

      color = color_entry.get()
      if not color:
        raise ValueError("Не выбран цвет.")

      draw = ImageDraw.Draw(self.img)
      draw.rectangle((x1, y1, x2, y2), outline=color, width=2)
      self.display_image(self.img)

    except ValueError as ve:
      messagebox.showerror("Ошибка ввода", str(ve))
    except Exception as e:
      messagebox.showerror("Ошибка", "Произошла ошибка: " + str(e))