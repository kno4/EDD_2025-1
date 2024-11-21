import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from ProyectoEDD.Libro import Libro
from ProyectoEDD.ABB import ABB

class LibreriaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Librería Kno")
        self.root.geometry("850x700")
        self.root.configure(bg="#e9f5fb")

        #Título
        ttk.Label(self.root, text="Gestión de Librería", font=("Helvetica", 24, "bold"), background="#e9f5fb", foreground="#0077b6").pack(pady=20)

        #Creación de etiquetas y formularios
        form_frame = ttk.LabelFrame(self.root, text="Información del Libro", padding=(20, 10), style="Custom.TLabelframe")
        form_frame.pack(fill="x", padx=20, pady=10)

        ttk.Label(form_frame, text="ID del Libro:", style="Custom.TLabel").grid(row=0, column=0, sticky="w", pady=5, padx=5)
        ttk.Label(form_frame, text="Título:", style="Custom.TLabel").grid(row=1, column=0, sticky="w", pady=5, padx=5)
        ttk.Label(form_frame, text="Autor:", style="Custom.TLabel").grid(row=2, column=0, sticky="w", pady=5, padx=5)
        ttk.Label(form_frame, text="Stock:", style="Custom.TLabel").grid(row=3, column=0, sticky="w", pady=5, padx=5)
        ttk.Label(form_frame, text="Precio:", style="Custom.TLabel").grid(row=4, column=0, sticky="w", pady=5, padx=5)

        self.id_entrada = ttk.Entry(form_frame, width=30)
        self.titulo_entrada = ttk.Entry(form_frame, width=30)
        self.autor_entrada = ttk.Entry(form_frame, width=30)
        self.stock_entrada = ttk.Entry(form_frame, width=30)
        self.precio_entrada = ttk.Entry(form_frame, width=30)

        self.id_entrada.grid(row=0, column=1, pady=5, padx=5)
        self.titulo_entrada.grid(row=1, column=1, pady=5, padx=5)
        self.autor_entrada.grid(row=2, column=1, pady=5, padx=5)
        self.stock_entrada.grid(row=3, column=1, pady=5, padx=5)
        self.precio_entrada.grid(row=4, column=1, pady=5, padx=5)

        button_frame = ttk.Frame(self.root, padding=(20, 10))
        button_frame.pack(fill="x", pady=10)

        #Mejora de botones
        self.add_button = tk.Button(button_frame, text="Insertar Libro", command=self.insertar_libro, bg="#38b000", fg="white", font=("Arial", 12, "bold"))
        self.search_button = tk.Button(button_frame, text="Consultar Libro", command=self.consultar_libro, bg="#0077b6", fg="white", font=("Arial", 12, "bold"))
        self.delete_button = tk.Button(button_frame, text="Eliminar Libro", command=self.eliminar_libro, bg="#e63946", fg="white", font=("Arial", 12, "bold"))
        self.show_button = tk.Button(button_frame, text="Mostrar Todos los Libros", command=self.mostrar_libros, bg="#ff9f1c", fg="white", font=("Arial", 12, "bold"))
        self.sell_button = tk.Button(button_frame, text="Vender Libro", command=self.vender_libro, bg="#ff6b6b", fg="white", font=("Arial", 12, "bold"))
        self.add_stock_button = tk.Button(button_frame, text="Agregar Stock", command=self.agregar_stock, bg="#4d9de0", fg="white", font=("Arial", 12, "bold"))

        self.add_button.grid(row=0, column=0, padx=10, pady=5)
        self.search_button.grid(row=0, column=1, padx=10, pady=5)
        self.delete_button.grid(row=0, column=2, padx=10, pady=5)
        self.show_button.grid(row=0, column=3, padx=10, pady=5)
        self.sell_button.grid(row=0, column=4, padx=10, pady=5)
        self.add_stock_button.grid(row=0, column=5, padx=10, pady=5)

        #Listado de libros agregados
        output_frame = ttk.LabelFrame(self.root, text="Salida", padding=(20, 10), style="Custom.TLabelframe")
        output_frame.pack(fill="both", expand=True, padx=20, pady=10)
        self.output = tk.Text(output_frame, wrap=tk.WORD, width=80, height=20, font=("Courier", 12), state=tk.DISABLED, bg="#f7f9fc", fg="#333333")
        self.output.pack(fill="both", expand=True)
        self.abb = ABB()

        self.estilizar_interfaz()

    def estilizar_interfaz(self):
        style = ttk.Style(self.root)
        style.configure("Custom.TLabelframe", background="#e9f5fb", foreground="#0077b6", font=("Helvetica", 12, "bold"))
        style.configure("Custom.TLabel", background="#e9f5fb", foreground="#333333", font=("Helvetica", 10))

    def insertar_libro(self):
        try:
            id_libro = int(self.id_entrada.get())
            titulo = self.titulo_entrada.get()
            autor = self.autor_entrada.get()
            stock = int(self.stock_entrada.get())
            precio = float(self.precio_entrada.get())

            libro = Libro(id_libro, titulo, autor, stock, precio)

            if self.abb.buscar(libro):
                messagebox.showerror("Error", "El código del libro ya existe. No se puede duplicar")
                return

            self.abb.insertar(libro)
            self.limpiar_campos()
            messagebox.showinfo("Éxito", "Libro insertado correctamente.")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa valores válidos.")

    def vender_libro(self):
        try:
            id_libro = int(self.id_entrada.get())
            libro_encontrado = self.abb.buscar(Libro(id_libro, "", "", 0, 0))

            if not libro_encontrado:
                messagebox.showinfo("Resultado", f"Libro con ID {id_libro} no encontrado.")
                return

            cantidad_vender = simpledialog.askinteger("Vender Libro", "¿Cuántos libros deseas vender?", minvalue=1)
            if cantidad_vender is None:
                return

            nodo = self.abb.raiz
            while nodo is not None:
                if id_libro == nodo.valor.id:
                    if nodo.valor.stock < cantidad_vender:
                        messagebox.showerror("Error", "No hay suficiente stock para completar la venta.")
                        return
                    nodo.valor.stock -= cantidad_vender
                    messagebox.showinfo("Éxito", f"Venta realizada. Stock restante: {nodo.valor.stock}")
                    return
                elif id_libro < nodo.valor.id:
                    nodo = nodo.izquierdo
                else:
                    nodo = nodo.derecho

        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa un ID válido.")

    def agregar_stock(self):
        try:
            id_libro = int(self.id_entrada.get())
            libro_encontrado = self.abb.buscar(Libro(id_libro, "", "", 0, 0))

            if not libro_encontrado:
                messagebox.showinfo("Resultado", f"Libro con ID {id_libro} no encontrado.")
                return

            cantidad_agregar = simpledialog.askinteger("Agregar Stock", "¿Cuántos libros deseas agregar?", minvalue=1)
            if cantidad_agregar is None:
                return

            nodo = self.abb.raiz
            while nodo is not None:
                if id_libro == nodo.valor.id:
                    nodo.valor.stock += cantidad_agregar
                    messagebox.showinfo("Éxito", f"Stock actualizado. Stock actual: {nodo.valor.stock}")
                    return
                elif id_libro < nodo.valor.id:
                    nodo = nodo.izquierdo
                else:
                    nodo = nodo.derecho

        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa un ID válido.")

    def consultar_libro(self):
        try:
            id_libro = int(self.id_entrada.get())
            libro_encontrado = self.abb.buscar(Libro(id_libro, "", "", 0, 0))

            if libro_encontrado:
                self.mostrar_mensaje(f"Libro con ID {id_libro} encontrado en el árbol.")
            else:
                messagebox.showinfo("Resultado", f"Libro con ID {id_libro} no encontrado.")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa un ID válido.")

    def eliminar_libro(self):
        try:
            id_libro = int(self.id_entrada.get())
            libro_encontrado = self.abb.buscar(Libro(id_libro, "", "", 0, 0))

            if not libro_encontrado:
                messagebox.showinfo("Resultado", f"Libro con ID {id_libro} no encontrado. No se puede eliminar.")
                return

            self.abb.eliminar(Libro(id_libro, "", "", 0, 0))
            messagebox.showinfo("Éxito", "Libro eliminado correctamente.")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa un ID válido.")

    def mostrar_libros(self):
        libros = self.abb.en_orden()
        if libros:
            encabezado = f"{'ID':<10}{'Título':<30}{'Autor':<20}{'Stock':<10}{'Precio':<10}\n"
            separador = "-" * 80 + "\n"
            mensaje = encabezado + separador
            for libro in libros:
                mensaje += f"{libro.id:<10}{libro.titulo:<30}{libro.autor:<20}{libro.stock:<10}{libro.precio:<10.2f}\n"
            self.mostrar_mensaje(mensaje)
        else:
            self.mostrar_mensaje("No hay libros en la biblioteca.")

    def mostrar_mensaje(self, mensaje):
        self.output.config(state=tk.NORMAL)
        self.output.delete(1.0, tk.END)
        self.output.insert(tk.END, mensaje)
        self.output.config(state=tk.DISABLED)

    def limpiar_campos(self):
        self.id_entrada.delete(0, tk.END)
        self.titulo_entrada.delete(0, tk.END)
        self.autor_entrada.delete(0, tk.END)
        self.stock_entrada.delete(0, tk.END)
        self.precio_entrada.delete(0, tk.END)

def main():
    root = tk.Tk()
    LibreriaGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
