from operator import pos
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from aqidl import post

def upload_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        img = Image.open(file_path)
        img = img.resize((500, 500))  
        photo = ImageTk.PhotoImage(img)
        
        uploaded_image.configure(image=photo)
        uploaded_image.image = photo
        predicted_value_label.config(text="Predicted Value:\n" + post(file_path))  # Replace "X" with your predicted value

root = tk.Tk()
root.title("File Prediction")

root.configure(bg='black')

uploaded_image_frame = tk.Frame(root, width=500, height=500, bg='black')
uploaded_image_frame.grid(row=0, column=0, padx=10, pady=10, sticky=tk.N+tk.S+tk.E+tk.W)

uploaded_image = tk.Label(uploaded_image_frame, borderwidth=2, relief="solid", bg='black')
uploaded_image.pack()

button_frame = tk.Frame(root, bg='black')
button_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky=tk.E+tk.W)

upload_button = tk.Button(button_frame, text="Upload & Predict", command=upload_file, width=40, height=4, bg='white', fg='black')
upload_button.pack(side=tk.LEFT, padx=10)

predicted_value_frame = tk.Frame(root, width=200, height=500, borderwidth=2, relief="solid", bg='black')
predicted_value_frame.grid(row=0, column=2, rowspan=2, padx=10, pady=10, sticky=tk.N+tk.S+tk.E+tk.W)

predicted_value_label = tk.Label(predicted_value_frame, text="Predicted Value:\nNone", width=100, height=500, wraplength=180, bg='black', fg='white')
predicted_value_label.pack(expand=True)

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=0)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

root.mainloop()