from PIL import Image, ImageTk
from rembg import remove
from tkinter import filedialog
import tkinter as tk

# input_path = "v3.jpg"
# output_path = "output.png"
# input = Image.open(input_path)
# output = remove(input)
# output.save(output_path)

root = tk.Tk()
root.title("Aming Torta BG Remover")

frame = tk.Frame(root, width=300, height=300, bg="lightgreen")
frame.pack()

def edit_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg; *.jpeg; *.png; *.gif")])
    output_file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
    if file_path and output_file_path:
        image = Image.open(file_path)
        output = remove(image)
        output.save(output_file_path)

        resized_image = output.resize((300, 300))

        display = ImageTk.PhotoImage(resized_image)
        label.config(image=display)
        label.image = display
        frame.destroy()

label = tk.Label(root)
label.pack()

button = tk.Button(root, text="Open Image", command=edit_image)
button.pack()

root.mainloop()