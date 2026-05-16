from io import BytesIO
import openpyxl

def descargar_plantilla():
    wb = openpyxl.Workbook() #obtiene el workbook y nos ayudara a obtener el worksheet

    ws = wb.active #este activa un worksheet

    ws.append(["Heal", "Kills", "Asistencias"]) # esta crea las filas con HEAL,KILLS Y ASISTENCIAS
    
    buffer = BytesIO() # esto lo que hace es poner el archivo en la ram antes que todo

    wb.save(buffer) # este guarda el worksheet en la memoria

    buffer.seek(0) #regresa al inicio del archivo para poder leerlo

    return buffer #esto tiene el archivo para poder descargarlo
