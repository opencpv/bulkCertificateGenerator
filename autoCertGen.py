from lib.generateCerts import generateCerts
from lib.getStudentNames import getStudentNames
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from tqdm import tqdm
from time import sleep
pdfmetrics.registerFont(
    TTFont('Great Vibes Regular', 'C:/Users/ARMOURY/AppData/Local/Microsoft/Windows/Fonts/GreatVibes-Regular.ttf'))

csv_path = "C:/Users/ARMOURY/Desktop/work/rise/rise 2023 certificates.csv"
column_name = "Names"
template_path = "C:/Users/ARMOURY/Desktop/work/rise/Final RiSE 2023 Certificate of Participation.pdf"
student_names = getStudentNames(csv_path, column_name)
for student in tqdm(student_names, desc="PDF Generation Progess"):
    generateCerts(student, template_path)
# for student in student_names:
#     generateCerts(student, template_path)
#     print("*")
