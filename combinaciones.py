import tkinter as tk
from math import *

class Calculator(tk.Frame):

    def __init__(self, __Padre__):
        super(Calculator, self).__init__(__Padre__)
        self._N = tk.IntVar()
        self._R = tk.IntVar()
        self._resultado = tk.IntVar()



        
    def create_widgets(self):
        combinacion_entrada_etiqueta_N = tk.Label(self, text="Ingresa N elemento")
        combinacion_entrada_etiqueta_N.pack()
        combinacion_entrada_N = tk.Entry(self, textvariable=self._N)
        combinacion_entrada_N.pack()

        combinacion_entrada_etiqueta_R = tk.Label(self, text="Ingresa R elemento")
        combinacion_entrada_etiqueta_R.pack()
        combinacion_entrada_R = tk.Entry(self, textvariable=self._R)
        combinacion_entrada_R.pack()

        self.Calcular = tk.Button(self, text='Calcular', command=self._nCr_())
        self.Calcular.pack()

    
        self.quit = tk.Button(self, text="QUIT", fg="red",
            command=self.master.destroy)
        self.quit.pack(side="bottom")


    def _nCr_(self):
        try:
            _n_ = self._N.get()
            _r_ = self._R.get()
            _re_ = int(self._resultado.get())


            if _re_ != 1:
                _re_ = comb(int(_n_),int(_r_))
                return _re_

            else:
                _re_ = factorial(_n_)
                return _re_

            

            resultado_label = tk.Label(self, textvariable=_re_)
            resultado_label.pack()

        except ImportError:
            print('ERROR')
        


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('300x300')
    
    main = Calculator(root)
    main.pack(fill="both", expand=True)
    main.create_widgets()
    root.mainloop()

