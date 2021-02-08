import tkinter as tk
from PIL import Image, ImageTk
from Comb_Calculator.Combinacion_no_repeticion import _nCr_, _nCr_Repeticion


class Calculator(tk.Frame):

    #SE DECLARAN LAS VARIABLES A USAR
    def __init__(self, __Padre__, *pargs):
        super(Calculator, self).__init__(__Padre__, *pargs)
        self._N = tk.IntVar()
        self._R = tk.IntVar()
        self._resultado = tk.IntVar()
        image2 = Image.open('fondo.png')
        # image2.show()
        image1 = ImageTk.PhotoImage(image2)
        background_label = tk.Label(self, image=image1)
        background_label.image1 = image1
        background_label.place(x=0, y=0, height=800, width=1000)

    #FUNCION EN LA QUE SE EJECUTA EL CODIGO
    def __main__(self):
        #ENTRADA DE N NUMEROS

        combinacion_entrada_etiqueta_N = tk.Label(self, text="Ingresa N elemento")
        combinacion_entrada_etiqueta_N.pack() # EL METODO PACK HACE QUE APAREZCA NUESTRO WIDGET
        combinacion_entrada_etiqueta_N.config(font=("Times New Roman", 24))

        combinacion_entrada_N = tk.Entry(self, textvariable=self._N) #SE INGRESA DATOS CON ENTRY
        combinacion_entrada_N.pack()
        combinacion_entrada_N.config(font=("Times New Roman", 24))


        #ENTRADA DE R NUMEROS
        combinacion_entrada_etiqueta_R = tk.Label(self, text="Ingresa R elemento")
        combinacion_entrada_etiqueta_R.pack()
        combinacion_entrada_etiqueta_R.config(font=("Times New Roman", 24))
        combinacion_entrada_R = tk.Entry(self, textvariable=self._R)
        combinacion_entrada_R.pack()
        combinacion_entrada_R.config(font=("Times New Roman", 24))

        #EN ESTE BOTON SE LLAMA A LA FUNCION DE COMBINACIONES, TIPO JAVASCRIPT
        self.Calcular = tk.Button(self, text='Sin Repeticion',
                                  command=lambda: _nCr_(
                                      self, int(self._N.get()), int(self._R.get())
                                  )) #FUNCION DE COMBINACIONES, PIDE PARAMETROS
        self.Calcular.pack()
        self.Calcular.config(font=("Times New Roman", 24))


        self.Combinacion_repeticion = tk.Button(self, text='Con Repeticion',
                                command=lambda: _nCr_Repeticion(
                                self, int(self._N.get()), int(self._R.get())
                                ))
        self.Combinacion_repeticion.pack()
        self.Combinacion_repeticion.config(font=("Times New Roman", 24))

        self.quit = tk.Button(self, text="Salir", fg="red",
            command=self.master.destroy)
        self.quit.pack(side="bottom")
        self.quit.config(font=("Times New Roman", 24))




if __name__ == "__main__":
    root = tk.Tk() #OBJETO DE TKINTER EL CUAL SE LO PASAMOS A NUESTRO OBJETO
    root.geometry("1000x800") #TAMANO DE VENTANA
    root.title("LOS MIKES")
    
    main = Calculator(root) #LLAMAMOS A NUESTRO OBJETO Y LE PASAMOS EL PARAMETRO TKINTER
    main.pack(fill="both", expand=True)
    main.__main__()
    root.mainloop()

