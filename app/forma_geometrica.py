from abc import ABC, abstractmethod


class FormaGeometrica(ABC):
    PI = 3.14 # constantele se scriu cu litere de mari
    # variabile = zone din mem calc in care se salveaza valori, care se pot modifica in timp, constalele nu isi modifca valoarea


    @abstractmethod
    def get_arie(self):
        pass



