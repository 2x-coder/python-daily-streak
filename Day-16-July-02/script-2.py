from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

doc = SimpleDocTemplate("report-script-2.pdf")

styles = getSampleStyleSheet()

story = []

story.append(Paragraph("<b>Research Report</b>", styles['Title']))
story.append(Paragraph("This report is generated automatically.", styles['BodyText']))

doc.build(story)