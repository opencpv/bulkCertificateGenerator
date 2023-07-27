from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import StringIO
import shutil
from reportlab.rl_config import defaultPageSize
from reportlab.pdfbase import pdfmetrics


def generateCerts(name, template_path, position=(24, 24), font_size=28, font="Great Vibes Regular", color=(1, 0, 0)):
    existing_pdf = PdfFileReader(open(template_path, "rb"))
    page_width = defaultPageSize[0]
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    can.setFont(font, font_size)
    text_width = pdfmetrics.stringWidth(name, font, font_size)
    text_x_pos = (page_width-text_width)/2.0
    can.drawString(text_x_pos, 450, name)
    can.save()
    # move to the beginning of the StringIO buffer
    packet.seek(0)
    new_pdf = PdfFileReader(packet)
    # read your existing PDF
    output = PdfFileWriter(open(template_path, "rb"))
    # add the "watermark" (which is the new pdf) on the existing page
    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)
    # finally, write "output" to a real file
    filename = "C:/Users/ARMOURY/Desktop/work/rise/certs/"+name+".pdf"
    outputStream = open(filename, "wb")
    output.write(outputStream)
    outputStream.close()
