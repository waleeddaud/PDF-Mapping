# fill_pdf.py
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import json
import pikepdf

def create_overlay(data, overlay_path):
    """Create overlay PDF with text at specific coordinates."""
    c = canvas.Canvas(overlay_path, pagesize=A4)
    c.setFont("Helvetica", 12)

    # Coordinates for each field (x, y)
    coordinates = {
        "Name": (200, 760),
        "DateOfBirth": (200, 740),
        "Address": (200, 720),
        "Phone": (200, 700)
    }

    for field, value in data.items():
        if field in coordinates:
            x, y = coordinates[field]
            c.drawString(x, y, value)

    c.save()

def merge_pdfs(template_path, overlay_path, output_path):
    """Merge overlay text with template PDF (flatten result)."""
    template_pdf = pikepdf.open(template_path)
    overlay_pdf = pikepdf.open(overlay_path)

    for base_page, overlay_page in zip(template_pdf.pages, overlay_pdf.pages):
        base_page.add_overlay(overlay_page)

    template_pdf.save(output_path)

if __name__ == "__main__":
    # Load data
    with open("sample_data.json", "r") as f:
        data = json.load(f)

    overlay_path = "overlay.pdf"
    output_path = "filled_form.pdf"

    # Step 1: Create overlay with filled data
    create_overlay(data, overlay_path)

    # Step 2: Merge overlay with the template
    merge_pdfs("template.pdf", overlay_path, output_path)

    print("filled_form.pdf created successfully")
