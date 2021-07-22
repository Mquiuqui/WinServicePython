from win32printing import Printer, PrinterFontContext
a = "testeRemessa"
b = "testeEfluente"
c = "testePlaca"
d = ""
font = {
    "height": 12,
    "orientation": 'left',

}
font2 = {
    "height": 13,
    "orientation": 2,

}


d = print("teste".ljust(25), end='')
print("teste") 
    
with Printer(printer_name="Microsoft Print to PDF") as printer:

    printer.text(a.ljust(25),font_config=font)


    printer.text(" ", font_config=font2)
    printer.text("   Transportadora"+"Remessa:%s\n"% (a)+"   Rodrigo" , font_config=font)
    printer.text("   Data"+"Efluente:%s\n"%(b)+"   R 00/00/2021 21:21:08", font_config=font)
    printer.text("   Nome motorista e visto.", font_config=font)
    printer.text("_____________________________________________________________", font_config=font)
    printer.text("   Diluição", font_config=font)
    printer.end_page
