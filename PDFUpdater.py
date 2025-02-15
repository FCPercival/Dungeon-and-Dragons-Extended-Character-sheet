"""Utility to update a PDF form template with data from a filled PDF form."""

import pdfrw
from pdfrw import PdfReader, PdfWriter, PdfDict, PdfString

ANNOT_KEY = '/Annots'  # key for annotations on a page
ANNOT_FIELD_KEY = '/T' # field name key
ANNOT_VAL_KEY = '/V'   # field value key

def get_field_name(annotation):
    name_obj = annotation.get(ANNOT_FIELD_KEY)
    if isinstance(name_obj, PdfString):
        return name_obj.to_unicode()
    elif isinstance(name_obj, str):
        return name_obj.strip("()")
    return None

def extract_form_data(pdf_path):
    pdf = PdfReader(pdf_path)
    data = {}
    for page in pdf.pages:
        annotations = page.get(ANNOT_KEY)
        if annotations:
            for annotation in annotations:
                field_name = get_field_name(annotation)
                if field_name:
                    value = annotation.get(ANNOT_VAL_KEY)
                    if isinstance(value, PdfString):
                        value = value.to_unicode()
                    elif value is None:
                        value = ''
                    else:
                        value = str(value)
                    data[field_name] = value
    return data

def fill_pdf(template_pdf_path, output_pdf_path, data_dict):
    pdf = PdfReader(template_pdf_path)
    for page in pdf.pages:
        annotations = page.get(ANNOT_KEY)
        if annotations:
            for annotation in annotations:
                field_name = get_field_name(annotation)
                if field_name and field_name in data_dict:
                    new_value = str(data_dict[field_name])
                    annotation.update(
                        PdfDict(V=PdfString.encode(new_value))
                    )
                    if '/AP' in annotation:
                        del annotation['/AP']
    PdfWriter().write(output_pdf_path, pdf)

old_pdf = input("Enter the path to the original filled PDF file: ").strip()
new_pdf_template = input("Enter the path to the new PDF template file: ").strip()
output_pdf = new_pdf_template

form_data = extract_form_data(old_pdf)
print("Extracted form data:", form_data)

fill_pdf(new_pdf_template, output_pdf, form_data)

print("New PDF generated with imported form data at:", output_pdf)
