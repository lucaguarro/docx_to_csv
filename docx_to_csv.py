import docx
import csv

doc = docx.Document('docx_files\Cracking the Machine Learning Interview.docx')

csv_rows = []
for p in doc.paragraphs:
    if any(run.bold for run in p.runs):
        if p.text.strip() != '':
            tag = p.text.strip()
    elif p.style.name == 'List Paragraph' and p.runs:
        question = p.runs[0].text.strip()
        answer = ''.join(r.text for r in p.runs[1:]).strip()
        csv_rows.append([question, answer, tag])

with open('./csv_files/CtMLI.csv', 'w', newline="", encoding='utf-8') as myfile:
    wr = csv.writer(myfile)
    wr.writerows(csv_rows)