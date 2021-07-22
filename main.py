import time 
from datetime import datetime
from pathlib import Path
from SMWinservice import SMWinservice
from win32printing import Printer
import keyboard 

def writeToFile():

    
    font = {
        "height": 8,
    }
    with Printer(linegap=1) as printer:
        printer.text("teste", font_config=font)


class PythonCornerExample(SMWinservice):
    _svc_name_ = "teste_quiuqui4"
    _svc_display_name_ = "teste4"
    _svc_description_ = "descrição qualquer"

    def start(self):
        self.isrunning = True

    def stop(self):
        self.isrunning = False

    def main(self):
        writeToFile()

if __name__ == '__main__':
    PythonCornerExample.parse_command_line()     