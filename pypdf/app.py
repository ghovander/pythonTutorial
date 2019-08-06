import PyPDF2
from pathlib import Path
import os

absolute_path = str(Path(__file__).resolve().parent.absolute())
sample_pdf = os.path.join(absolute_path, "sample.pdf")
rotated_pdf = os.path.join(absolute_path, "rotated.pdf")
combined_pdf = os.path.join(absolute_path, "combined.pdf")


with open(sample_pdf, "rb") as file:
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)
    page = reader.getPage(0)
    page.rotateClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open(rotated_pdf, "wb") as output:
        writer.write(output)


merger = PyPDF2.PdfFileMerger()
file_names = [sample_pdf, rotated_pdf]
for file_name in file_names:
    merger.append(file_name)
merger.write(combined_pdf)
