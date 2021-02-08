import tkinter as tk
from math import * #lIBRERIA PARA LAS COMBIANCIONES Y FACTORIALES

# FUNCION DE COMBINACIONES sin repetición
def _nCr_(self, _n_, _r_):
    try:
        self._resultado = comb(_n_, _r_)
    except ImportError:
        print('ALGO MALO HA OCURRIDO')

    resultado_label = tk.Label(self, text=self._resultado)  # MOSTRAMOS EL RESULTADO
    resultado_label.pack()
    resultado_label.config(font=("Times New Roman", 24))


def _nCr_Repeticion(self, _n_, _r_):
    try:
        if _n_ == _r_:
            _n_r_same = factorial(_r_)
            self._resultado = _n_r_same

        else:
            self._resultado = factorial(_n_ + _r_ - 1) / (factorial(_r_) * factorial(_n_ - 1))



    except ImportError:
        print('ALGO MALO HA OCURRIDO')

    resultado_label = tk.Label(self, text=self._resultado)  # MOSTRAMOS EL RESULTADO
    resultado_label.pack()
    resultado_label.config(font=("Times New Roman", 24))

