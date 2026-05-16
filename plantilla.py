from io import BytesIO
import openpyxl

def descargar_plantilla():
    wb = openpyxl.Workbook()

    ws = wb.active

    ws.append(["Heal", "Kills", "Asistencias"])
    
    buffer = BytesIO()

    wb.save(buffer)

    buffer.seek(0)

    return buffer
