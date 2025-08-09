# PDF Field Mapping Prototype

This is a minimal working prototype that demonstrates how to map structured JSON data to a PDF template using Python, place text at precise coordinates, and output a flattened PDF ready for submission.

---

## Files Overview

### 1. `create_template.py`  
**Purpose:**  
Creates a simple sample PDF template (`template.pdf`) with placeholder labels for fields such as **Name**, **Date of Birth**, **Address**, and **Phone**.

**Key Points:**
- Uses **ReportLab** to draw labels and structure.
- Positions are defined in `(x, y)` coordinates, measured from the **bottom-left corner** of the page.
- Simulates a real form that would be provided by the client.

**Example usage:**
```bash
python create_template.py
# -> generates template.pdf
```

---

### 2. `data.json`  
**Purpose:**  
Holds the structured input data that will be mapped to the PDF.

**Format:** Standard JSON key-value pairs.

**Example `data.json`:**
```json
{
  "Name": "John Doe",
  "DateOfBirth": "1990-05-14",
  "Address": "123 Main Street, Springfield, USA",
  "Phone": "(555) 123-4567"
}
```

_In production this JSON could come from a DB, API, or other source._

---

### 3. `fill_pdf.py`  
**Purpose:**  
Reads the JSON data, generates an overlay with the field values at specific coordinates, and merges it with the template to create a filled, flattened PDF.

**Structure / Key functions:**
- `create_overlay(data, overlay_path)` — uses ReportLab to draw text at coordinates onto an overlay PDF.
- `merge_pdfs(template_path, overlay_path, output_path)` — uses PikePDF to add the overlay to the template and save a flattened result.

**Coordinates mapping (example snippet inside `fill_pdf.py`):**
```python
coordinates = {
    "Name": (200, 760),
    "DateOfBirth": (200, 740),
    "Address": (200, 720),
    "Phone": (200, 700)
}
```
_This mapping can be moved to an external `mapping.json` for scalability._

**Example usage:**
```bash
python fill_pdf.py
# -> reads data.json, creates overlay.pdf, merges with template.pdf, outputs filled_form.pdf
```

---

## Workflow

1. **Create virtual environment, activate the script and install dependencies**
```bash
uv venv
# After creating activate the virtual environment '.\.venv\Scripts\activate'
uv pip install -r requirements.txt
```

2. **Create the template**
```bash
python create_template.py
# creates template.pdf
```

3. **Fill the template**
```bash
python fill_pdf.py
# reads data.json -> overlay.pdf -> filled_form.pdf
```

---

## Output Files

- `template.pdf` — Blank form with placeholder labels.
- `overlay.pdf` — Generated text overlay with data (intermediate file).
- `filled_form.pdf` — Final output with data filled in and flattened.

---

## How This Relates to the Job Description

- **Mapping fields to coordinates** — Demonstrates mapping canonical data fields to PDF positions.
- **JSON input** — Matches the requirement for JSON/YAML mapping specs.
- **Flattened output** — Ensures the filled PDF is ready for submission and not editable.
- **Modular structure** — Easy to extend for checkboxes, conditional logic, multi-line wrapping, and multi-page templates.

---

## Next Steps / Suggested Enhancements

- Move `coordinates` into a `mapping.json` to make mapping data-driven.
- Add:
  - Checkbox and radio button handling.
  - Multi-line text wrapping and font/line-height controls.
  - Basic QA checks (pixel/coordinate sanity, value validation).
  - Version tracking of templates and mapping files (GitHub + PR workflow).
- Add HIPAA-safe test-data and a README section describing PHI handling for client demos.

---

## Notes

If you want, I can update the prototype so `fill_pdf.py` loads coordinates from a `mapping.json` (so the repo matches the client's "mapping specs" requirement). Just say “yes” and I’ll add the `mapping.json` + updated `fill_pdf.py`.
