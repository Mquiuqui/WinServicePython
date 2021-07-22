from win32printing import Printer, PrinterFontContext

font = {
    "height": 12,
    "orientation": 'left',

}
font2 = {
    "height": 13,
    "orientation": 2,

}


T = "Tansportadora".ljust(30)
D = "Data".ljust(34)
N = "Nome motorista e visto".ljust(5)
Di = "Diluição:"
O = "080_FOPE-REV00"


t = T.center(36,' ')
d = D.center(41,' ')
n = N.center(30,' ')
di = Di.center(10,' ')

nome = "Transportadora Quiuqui".rjust(3)
data = "20/02/2021".center(17,' ')
placa = "CUD-0056".center(0,' ') 




    
with Printer(printer_name="HP Photosmart C4700 series") as printer:
        printer.text(t+"Remessa:%s"%("20000/21"), font_config=font)
        printer.text("    "+nome, font_config=font)
        printer.text(d+" Efluente:%s"%("Fossa Séptica\n")+data, font_config=font)
        printer.text(n+" Placa:"+placa+"\n"+"___________________________________________________", font_config=font)
        printer.text("    "+di+"40     "+O,)


        printer.end_page
