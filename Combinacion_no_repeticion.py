import tkinter as tk
from math import * #lIBRERIA PARA LAS COMBIANCIONES Y FACTORIALES

# FUNCION DE COMBINACIONES sin repetición
def _nCr_(self, _n_, _r_):
    try:
        self._resultado = comb(_n_, _r_)
        if self._resultado == 1:
            self._resultado = factorial(_n_)
            return self._resultado

        else:
            pass


    except ImportError:
        print('ALGO MALO HA OCURRIDO')

    resultado_label = tk.Label(self, text=self._resultado)  # MOSTRAMOS EL RESULTADO
    resultado_label.pack()
    resultado_label.config(font=("Times New Roman", 24))


# def _nCr_Repeticion(self, self, _n_, _r_):
#     pass



