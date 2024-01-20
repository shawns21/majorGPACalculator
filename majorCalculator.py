import PyPDF2

def extractTextFromPdf(pdfFile: str) -> [str]:

    with open(pdfFile, 'rb') as pdfFileObj:
        reader = PyPDF2.PdfReader(pdf, strict=False)
        pdfText = ""

        for page in reader.pages:

            content = page.extract_text()
            pdfText += (content)

        return pdfText
    
if __name__ == '__main__':

    JohnJaySubjects = {'CS', 'MA', 'PH'}
    JohnJayClasses = {'CSCI411', 'MAT152', 'MAT253', 'CSCI362', 'CSCI377', 'CSCI271', 'MAT301', 'CSCI376', 'MAT380', 'MAT242', 'MAT243', 'MAT141', 'MAT351', 'MAT204', 'MAT310', 'CSCI401', 'CSCI421', 'PHI216', 'CSCI373', 'MAT385', 'CSCI400', 'CSCI360', 'MAT105', 'CSCI374', 'MAT244', 'MAT241', 'CSCI275', 'CSCI358', 'CSCI385', 'CSCI272', 'MAT151', 'CSCI404', 'CSCI380', 'MAT371', 'CSCI379', 'CSCI412', 'CSCI375', 'CSCI274'}  

    MedgarEverSubjects = {'CS', 'MT', 'PH'}
    MedgarEversClasses = {'PHYL213', 'MTH204', 'CS281', 'MTH237', 'MTH202', 'CS325', 'CS360', 'PHYW213', 'PHYW212', 'CS244', 'PHY212', 'PHYL212', 'MTH203', 'CS241', 'MTH151', 'CS345', 'CS260', 'CS312', 'CS315', 'CS246', 'CS350', 'CS265', 'PHY213', 'CS395'}

    def JohnJaySearch():

        for line in lines_list:
    
            if (line[:2] in JohnJaySubjects):

                if (line[:9].replace(" ", "") in JohnJayClasses):
                    print(line)
                        
    def MedgarEversSearch():

        for line in lines_list:
    
            if (line[:2] in MedgarEverSubjects):

                if (line[:8].replace(" ", "") in MedgarEversClasses or line[:9].replace(" ", "") in MedgarEversClasses):
                    print(line)

    pdf = 'transcript.pdf'
    extractedText = extractTextFromPdf(pdf)

    lines_list = extractedText.splitlines()

    JohnJaySearch()