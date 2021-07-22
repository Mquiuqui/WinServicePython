import time 
from datetime import datetime
from pathlib import Path
from SMWinservice import SMWinservice
from win32printing import Printer

def writeToFile():

    font = {
        "height": 11,

    }
    with Printer() as printer:

        printer.text("   Transportadora\n"+"   rodrigo", font_config=font)
        printer.text(" ", font_config=font)
        printer.text("   Data\n"+"   R 00/00/2021 21:21:08", font_config=font)
        printer.text(" ", font_config=font)
        printer.text("   Nome motorista e visto.", font_config=font)
        printer.text("_____________________________________________________________", font_config=font)
        printer.text("   Diluição", font_config=font)
        printer.end_page




class PythonCornerExample(SMWinservice):
    _svc_name_ = "teste_quiuqui"
    _svc_display_name_ = "teste6"
    _svc_description_ = "descrição qualquer sobre impressão"

    def start(self):
        self.isrunning = True

    def stop(self):
        self.isrunning = False

    def main(self):
         writeToFile()
        

        

if __name__ == '__main__':
    PythonCornerExample.parse_command_line()     