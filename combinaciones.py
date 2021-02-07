import tkinter as tk
from math import * #lIBRERIA PARA LAS COMBIANCIONES Y FACTORIALES
from PIL import Image, ImageTk

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

        combinacion_entrada_N = tk.Entry(self, textvariable=self._N) #SE INGRESA DATOS CON ENTRY
        combinacion_entrada_N.pack()

        #ENTRADA DE R NUMEROS
        combinacion_entrada_etiqueta_R = tk.Label(self, text="Ingresa R elemento")
        combinacion_entrada_etiqueta_R.pack()
        combinacion_entrada_R = tk.Entry(self, textvariable=self._R)
        combinacion_entrada_R.pack()

        #EN ESTE BOTON SE LLAMA A LA FUNCION DE COMBINACIONES, TIPO JAVASCRIPT
        self.Calcular = tk.Button(self, text='Calcular',
                                  command=lambda : self._nCr_(
                                      int(self._N.get()), int(self._R.get())
                                  )) #FUNCION DE COMBINACIONES, PIDE PARAMETROS
        self.Calcular.pack()

    
        self.quit = tk.Button(self, text="QUIT", fg="red",
            command=self.master.destroy)
        self.quit.pack(side="bottom")

    # FUNCION DE COMBINACIONES
    def _nCr_(self, _n_, _r_ ):
        try:
            self._resultado = comb(_n_, _r_)
            if self._resultado == 1:
                self._resultado = factorial(_n_)
                return self._resultado

            else:
                pass


        except ImportError:
            print('ALGO MALO HA OCURRIDO')

        resultado_label = tk.Label(self, text=self._resultado) #MOSTRAMOS EL RESULTADO
        resultado_label.pack()



if __name__ == "__main__":
    root = tk.Tk() #OBJETO DE TKINTER EL CUAL SE LO PASAMOS A NUESTRO OBJETO
    root.geometry("1000x800") #TAMANO DE VENTANA
    root.title("LOS MIKES")
    
    main = Calculator(root) #LLAMAMOS A NUESTRO OBJETO Y LE PASAMOS EL PARAMETRO TKINTER
    main.pack(fill="both", expand=True)
    main.__main__()
    root.mainloop()

