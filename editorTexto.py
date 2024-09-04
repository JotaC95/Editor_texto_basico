import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


class TextEditor:
    def __init__(self, root):
        # Crear la ventana
        self.root = root
        self.root.title("Editor de Texto")
        self.root.geometry("800x600")

        # Configuración del menú
        self.menu_bar = tk.Menu(root)  # Crea una barra de menu
        root.config(menu=self.menu_bar)  # A;ade la barra a la ventana

        # Crea un menu desplegable
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        # A;ade en menu desplegable a la bara de menu con la etiqueta archivo
        self.menu_bar.add_cascade(label="Archivo", menu=self.file_menu)
        # A;ade elementos a la barra con comandos
        self.file_menu.add_command(label="Nuevo", command=self.new_file)
        self.file_menu.add_command(label="Abrir", command=self.open_file)
        self.file_menu.add_command(label="Guardar", command=self.save_file)
        self.file_menu.add_separator()  # A;ade un separador solo para efecto visual
        self.file_menu.add_command(label="Salir", command=root.quit)

        # Segundo menu desplegable con acciones como copiar pegar con el nombre Editar
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Editar", menu=self.edit_menu)
        self.edit_menu.add_command(label="Cortar", command=self.cut)
        self.edit_menu.add_command(label="Copiar", command=self.copy)
        self.edit_menu.add_command(label="Pegar", command=self.paste)

        # Área de texto
        self.text_area = tk.Text(root, undo=True)
        self.text_area.pack(fill=tk.BOTH, expand=1)

        # Configuración de la barra de desplazamiento
        self.scrollbar = tk.Scrollbar(self.text_area)
        self.text_area.config(
            yscrollcommand=self.scrollbar.set
        )  # Para que el area de texto se ajuste al scroll
        self.scrollbar.config(
            command=self.text_area.yview
        )  # Controla el desplazamiento del scroll para que se mueva con la vista del area de texto
        self.scrollbar.pack(
            side=tk.RIGHT, fill=tk.Y
        )  # Ubica la barra y al ubica del lado izquierdo y la expande en toda la ventana

    # Funcion para nuevo archivo
    def new_file(self):
        self.text_area.delete(1.0, tk.END)  # Borra el area de texto
        self.root.title("Nuevo Archivo - Editor de Texto")

    # Funcion para abrir un archivo
    def open_file(self):
        file_path = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("All Files", "*.*"), ("Text Files", "*.txt")],
        )
        if file_path:
            try:
                with open(file_path, "r") as file:
                    self.text_area.delete(1.0, tk.END)
                    self.text_area.insert(tk.END, file.read())
                self.root.title(f"{file_path} - Editor de Texto")
            except Exception as e:
                messagebox.showerror("Error", e)

    # Funcion para guardar archivos
    def save_file(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("All Files", "*.*"), ("Text Files", "*.txt")],
        )
        if file_path:
            try:
                with open(file_path, "w") as file:
                    file.write(self.text_area.get(1.0, tk.END))
                self.root.title(f"{file_path} - Editor de Texto")
            except Exception as e:
                messagebox.showerror("Error", e)

    # Funcio para cortar un archivo
    def cut(self):
        self.text_area.event_generate("<<Cut>>")

    # Funcio para copiar un archivo
    def copy(self):
        self.text_area.event_generate("<<Copy>>")

    # Funcio para pegar un archivo
    def paste(self):
        self.text_area.event_generate("<<Paste>>")


if __name__ == "__main__":
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()
