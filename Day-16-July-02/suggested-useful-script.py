from reportlab.platypus import *
from reportlab.lib.styles import getSampleStyleSheet

class PDFGenerator:

    def __init__(self, filename):
        self.doc = SimpleDocTemplate(filename)
        self.styles = getSampleStyleSheet()
        self.story = []

    def heading(self, text):
        self.story.append(Paragraph(text, self.styles['Heading1']))

    def paragraph(self, text):
        self.story.append(Paragraph(text, self.styles['BodyText']))

    def table(self, data):
        self.story.append(Table(data))

    def image(self, path, width=250, height=180):
        self.story.append(Image(path, width, height))

    def save(self):
        self.doc.build(self.story)

pdf = PDFGenerator("report.pdf")

pdf.heading("Research Report")
pdf.paragraph("Generated completely using Python.")

pdf.table([
    ["Model","Accuracy"],
    ["Ogden", "95%"],
    ["Neo-Hookean", "89%"]
])

pdf.save()