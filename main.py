import os
import fitz  # pip install PyPDF2 Pillow PyMuPDF
from PIL import Image
import random

base_directory = os.getcwd()
input_folder = os.path.join(base_directory, 'input')
output_folder = os.path.join(base_directory, 'output')
signature_file = os.path.join(base_directory, 'signature.jpg')

os.makedirs(output_folder, exist_ok=True)

def add_signature_to_pdf(pdf_path, signature_path, output_path):
    doc = fitz.open(pdf_path)
    
    signature = Image.open(signature_path)
    signature_width, signature_height = signature.size
    signature_pix = fitz.Pixmap(signature_path)
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        page_width = page.rect.width
        page_height = page.rect.height

        
        random_x_offset = random.choice([150, 200, 250, 100, 180, 120])
        random_y_offset = random.choice([20, 30, 40, 25, 35, 45])

        x = (page_width - signature_width) / 2 + random_x_offset
        y = page_height - signature_height - random_y_offset


        # x = (page_width - signature_width) / 2 + 200
        # y = page_height - signature_height - 30 
        
        page.insert_image(fitz.Rect(x, y, x + signature_width, y + signature_height), pixmap=signature_pix, overlay=True)
    
    doc.save(output_path)
    doc.close()


for filename in os.listdir(input_folder):
    if filename.lower().endswith('.pdf'):
        input_pdf_path = os.path.join(input_folder, filename)
        output_pdf_path = os.path.join(output_folder, filename)
        add_signature_to_pdf(input_pdf_path, signature_file, output_pdf_path)

print(f"All the PDFs have been processed and saved to {output_folder}")
