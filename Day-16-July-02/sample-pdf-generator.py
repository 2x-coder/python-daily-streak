from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

filename = "sample-script-1.pdf"

c = canvas.Canvas(filename, pagesize=A4)

width, height = A4

c.setFont("Helvetica-Bold", 20)
c.drawString(50, height-50, "My First PDF")

c.setFont("Helvetica", 12)

text = """
This PDF was generated using Python.

Features:
- Custom text
- Different fonts
- Multiple pages
- Images
- Tables
"""

textobject = c.beginText(50, height-100)

for line in text.split("\n"):
    textobject.textLine(line)

c.drawText(textobject)

c.save()

print("PDF created!")   