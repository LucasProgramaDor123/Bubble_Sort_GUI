import random
import tkinter as tk

def generate_list(size):
    return [random.randint(-100, 100) for _ in range(size)]

def sort_list(list_data):
    comparisons = 0
    for i in range(len(list_data) - 1):
        for j in range(len(list_data) - 1):
            comparisons += 1
            if list_data[j] > list_data[j + 1]:
                list_data[j], list_data[j + 1] = list_data[j + 1], list_data[j]
    return list_data, comparisons

def update_ui():
   try:
       size = int(size_entry.get())
       unsorted_list = generate_list(size)
       sorted_list, comparisons = sort_list(unsorted_list[:])

       unsorted_list_text.set("\n".join(map(str, unsorted_list)))
       sorted_list_text.set("\n".join(map(str, sorted_list)))
       comparisons_label.config(text=f"Comparisons: {comparisons}")

       unsorted_list_area.config(state="normal")
       unsorted_list_area.delete(1.0, tk.END)
       unsorted_list_area.insert(tk.END, unsorted_list_text.get())
       unsorted_list_area.config(state="disabled")

       sorted_list_area.config(state="normal")
       sorted_list_area.delete(1.0, tk.END)
       sorted_list_area.insert(tk.END, sorted_list_text.get())
       sorted_list_area.config(state="disabled")


   except ValueError:
       # Handle invalid input (non-integer)
       pass


# Cria janela principal
root = tk.Tk()
root.title("Bubble Sort GUI")

# pede o tamanho
size_label = tk.Label(root, text="Numero de elementos:")
size_label.pack()

size_entry = tk.Entry(root)
size_entry.pack()

# Botão!!
generate_button = tk.Button(root, text="Generate", command=update_ui)
generate_button.pack()

# Lista original
unsorted_list_label = tk.Label(root, text="Fora de ordem:")
unsorted_list_label.pack()
unsorted_list_text = tk.StringVar()
unsorted_list_area = tk.Text(root, width=50, height=20, state="disabled", wrap="word")
unsorted_list_area.config(font=("Courier New", 10))
unsorted_list_area.config(state="normal")
unsorted_list_area.insert(tk.END, unsorted_list_text.get())
unsorted_list_area.config(state="disabled")
unsorted_list_area.pack()

# Lista ordenada
sorted_list_label = tk.Label(root, text="Em ordem:")
sorted_list_label.pack()
sorted_list_text = tk.StringVar()
sorted_list_area = tk.Text(root, width=50, height=20, state="disabled", wrap="word")
sorted_list_area.config(font=("Courier New", 10))
sorted_list_area.config(state="normal")
sorted_list_area.insert(tk.END, sorted_list_text.get())
sorted_list_area.config(state="disabled")
sorted_list_area.pack()

#comparação
comparisons_label = tk.Label(root)
comparisons_label.pack()

# Iniciar o LOOP
root.mainloop()
