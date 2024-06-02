import pdfplumber
import sys

#extract data from the file using pdfplumber
#understanding the spacing within the text data
#extract the data that i need from expression 

root = sys.path[0]+"\g.pdf"


# Open the PDF file
with pdfplumber.open(root) as pdf:
    # Access the first page of the PDF
    first_page = pdf.pages[0]
    
    # Extract text from the first page
    text = first_page.extract_text()
    print(text)