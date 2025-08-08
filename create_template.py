# create_template.py
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def create_blank_pdf(filename):
    c = canvas.Canvas(filename, pagesize=A4)
    c.setFont("Helvetica", 12)
    c.drawString(200, 800, "Sample PDF Template")
    c.drawString(100, 760, "Name:")
    c.drawString(100, 740, "Date of Birth:")
    c.drawString(100, 720, "Address:")
    c.drawString(100, 700, "Phone:")
    c.save()

if __name__ == "__main__":
    create_blank_pdf("template.pdf")
    print("template.pdf created")
