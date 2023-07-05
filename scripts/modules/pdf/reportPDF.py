import pdfkit

def generatePDFReport(input, output):
    pdfkit.from_file(input, output)
