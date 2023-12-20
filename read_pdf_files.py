import os
import re
import PyPDF2
import pandas as pd
from datetime import datetime

# Define a function to extract data from a PDF file
def extract_data_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        print("*************")
        # text = pdf_reader.pages[0].extract_text()
        for page in pdf_reader.pages:
            # Extract text from each page
            text = page.extract_text()
        return text
# Directory path
dir_path = '.'  # Current directory. Change this if necessary.

# List all PDF files in the directory
# pdf_files = [f for f in os.listdir(dir_path) if f.endswith('.pdf')]
pdf_files = [f for f in os.listdir(dir_path) if f.lower().endswith('.pdf')]
print(pdf_files)
# Extract data and store in a list
data_list = []
for pdf_file in pdf_files:
    text = extract_data_from_pdf(pdf_file)
    print(text)