import PyPDF2
import re
import webbrowser

with open('sda.pdf', 'rb') as pdfFile:
    reader = PyPDF2.PdfFileReader(pdfFile)
    page2 = reader.getPage(5)
    text = page2.extractText()
    # print(text)
    rex = re.compile("(?<=fungsi lagi :)(.*)", re.DOTALL)
    body = re.search(rex, text).group(0)
    holdings = re.findall(r'([a-z A-Z \s]+)(?=\n)', body)
    for company in holdings:
        webbrowser.open_new_tab(f'http://google.com/search?q={company}')