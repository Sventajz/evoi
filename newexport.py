import csv
from pdfminer.high_level import extract_text
import numpy as np
def extract_text_from_pdf(pdf_path, page_number):
    with open(pdf_path, 'rb') as file:
        text = extract_text(file, page_numbers=[page_number])
    return text

def extract_and_save_to_csv(pdf_path, page_numbers, csv_filename, lines_to_extract, lines_to_save=6):
    # Initialize a list to store dictionaries of extracted values for each page
    all_extracted_values = []

    for page_number in page_numbers:
        text = extract_text_from_pdf(pdf_path, page_number)

        # Split the text into lines
        lines = [line.strip() for line in text.split('\n')]

        # Initialize a dictionary to store the extracted values
        extracted_values = {}

        # Iterate through lines and extract content after ":"
        for line in lines:
            for key in lines_to_extract:
                if line.startswith(key):
                    value = line[len(key):].split(':', 1)[1].strip()  # Extract content after ":"
                    extracted_values[key] = value

        # Append the extracted values to the list for each page
        all_extracted_values.append(extracted_values)

    # Print the extracted values
    print("Extracted Lines:")
    for extracted_values in all_extracted_values:
        print(extracted_values)

    # Save the extracted values to a CSV file
    with open(csv_filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=lines_to_extract.keys())

        # Write the header to the CSV file
        writer.writeheader()

        # Write the saved lines to the CSV file for each page
        writer.writerows(all_extracted_values)

# Replace 'your_pdf_file.pdf' with the actual path to your PDF file
pdf_path = 'ASR CABINET VERVOORT HQ Ducale7 V01. 20221129 AXE.pdf'
# Specify the page numbers you want to extract (modify as needed)
page_numbers_to_extract = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55]
#,15,17,20,22,25,27,28,30,33,35,37,40,43,45,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,79,81,84
csv_filename = '6.csv'

# Specify the lines you want to extract (modify as needed)
lines_to_extract = {
    'AP name / number': '',
    'AP model': '',
    'AP Reference': '',
    'AP serial number': '',
    'IP address': '',
    'Customer': '',
    'Site name': '',
    'Site address': '',
    'Problems encountered' : '',
    'Corrective actions' : ''
}

lines_to_save = 6  # Set the number of lines to save

extract_and_save_to_csv(pdf_path, page_numbers_to_extract, csv_filename, lines_to_extract, lines_to_save)

