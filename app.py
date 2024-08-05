import PyPDF2
from pathlib import Path

# Create the merger object
merger = PyPDF2.PdfMerger()

# Define the path to the "pdf_files" directory
path = Path("pdf_files")

# Store the files in a list by alphabetical order
pdf_files = sorted(path.iterdir())

for pdf_file in pdf_files:
    if pdf_file.suffix == ".pdf":
        merger.append(pdf_file)

# Write the new file in the root directory
merger.write("merged.pdf")

