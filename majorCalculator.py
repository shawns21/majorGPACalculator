import PyPDF2
import time

def extractTextFromPdf(pdfFile: str) -> [str]:

    with open(pdfFile, 'rb') as pdfFileObj:
        reader = PyPDF2.PdfReader(pdf, strict=False)
        pdfText = ""

        for page in reader.pages:

            content = page.extract_text()
            pdfText += (content)

        return pdfText
    
if __name__ == '__main__':

    try:

        JohnJaySubjects = {'CS', 'MA', 'PH'}
        JohnJayClasses = {'CSCI411', 'MAT152', 'MAT253', 'CSCI362', 'CSCI377', 'CSCI271', 'MAT301', 'CSCI376', 'MAT380', 'MAT242', 'MAT243', 'MAT141', 'MAT351', 'MAT204', 'MAT310', 'CSCI401', 'CSCI421', 'PHI216', 'CSCI373', 'MAT385', 'CSCI400', 'CSCI360', 'MAT105', 'CSCI374', 'MAT244', 'MAT241', 'CSCI275', 'CSCI358', 'CSCI385', 'CSCI272', 'MAT151', 'CSCI404', 'CSCI380', 'MAT371', 'CSCI379', 'CSCI412', 'CSCI375', 'CSCI274'}  

        MedgarEverSubjects = {'CS', 'MT', 'PH'}
        MedgarEversClasses = {'CS140', 'PHYL213', 'MTH204', 'CS281', 'MTH237', 'MTH202', 'CS325', 'CS360', 'PHYW213', 'PHYW212', 'CS244', 'PHY212', 'PHYL212', 'MTH203', 'CS241', 'MTH151', 'CS345', 'CS260', 'CS312', 'CS315', 'CS246', 'CS350', 'CS265', 'PHY213', 'CS395'}

        StatenIslandSubjects = {'MTH', 'CSC', 'AST', 'BIO', 'CHM', 'GEO', 'ESC', 'PHY'}
        StatenIslandClasses = {'MTH123', 'CSC426', 'CSC412', 'CSC475', 'CSC446', 'CSC346', 'CSC229', 'CHM121', 'CSC435', 'CSC250', 'GEO116', 'GEO102', 'CSC480', 'CSC484', 'CSC432', 'AST160', 'MTH232', 'CSC434', 'BIO170', 'CSC228', 'MTH229', 'MTH230', 'CSC226', 'CSC332', 'CHM127', 'CSC425', 'CSC482', 'CSC315', 'GEO103', 'CSC420', 'CSC430', 'AST120', 'CHM141', 'CSC223', 'CSC427', 'CSC305', 'MTH306', 'BIO171', 'MTH130', 'CHM142', 'GEO115', 'PHY160', 'PHY161', 'CSC490', 'CSC235', 'CSC126', 'CSC326', 'ESC111', 'CSC221', 'BIO181', 'PHY120', 'CSC429', 'CSC225', 'CSC424', 'CSC421', 'CSC438', 'MTH231', 'CSC211', 'BIO180', 'CSC245', 'MTH228', 'CSC470', 'CSC220', 'CSC347', 'CSC382', 'ESC110', 'CSC227', 'CSC330', 'CSC436', 'MTH125', 'PHY121'}

        BrooklynCollegeSubjects = {'CI', 'MA'}
        BrooklynCollegeClasses = {'CISC1115', 'CISC1170', 'CISC2210', 'CISC3115', 'CISC3130', 'CISC3140', 'CISC3320', 'CISC3305', 'CISC3310', 'CISC3142', 'CISC3220', 'CISC3230', 'CISC4900', 'CISC5001', 'CISC2820W', 'CISC3318W', 'MATH1006', 'MATH1011', 'MATH1012', 'MATH1201', 'MATH1206', 'MATH1211', 'MATH2501', 'MATH3501'}

        possibleEnds = {'A', 'B', 'C', 'D', 'F', '-', '+'}


        def JohnJaySearch():

            grades = []

            for line in lines_list:
        
                if (line[:2] in JohnJaySubjects):

                    if (line[:9].replace(" ", "") in JohnJayClasses):
                        grades.append(line[-6:].replace(" ", ""))
            
            return grades
                            
        def MedgarEversSearch():

            grades = []

            for line in lines_list:
        
                if (line[:2] in MedgarEverSubjects):

                    if (line[:8].replace(" ", "") in MedgarEversClasses) or (line[:9].replace(" ", "") in MedgarEversClasses):
                    
                        hold = line[-7:].replace(" ", "")
        
                        if hold[-1] in possibleEnds:
                            
                            if not hold[0].isdigit():

                                hold = hold[1:]
                            
                            grades.append(hold)
            
            return grades

        def StatenIslandSearch():

            grades = []

            for line in lines_list:
        
                if (line[:3] in StatenIslandSubjects):

                    if (line[:8].replace(" ", "") in StatenIslandClasses) or (line[:9].replace(" ", "") in StatenIslandClasses):
                    
                        hold = line[-7:].replace(" ", "")
        
                        if hold[-1] in possibleEnds:
                            
                            if not hold[0].isdigit():

                                hold = hold[1:]
                            
                            grades.append(hold)

            return grades
            
        def BrooklynCollegeSearch():

            grades = []

            for line in lines_list:
        
                if (line[:2] in BrooklynCollegeSubjects):

                    if (line[:10].replace(" ", "") in BrooklynCollegeClasses or line[:11].replace(" ", "") in BrooklynCollegeClasses):
                    
                        hold = line[-7:].replace(" ", "")
    
                        if hold[-1] in possibleEnds:
                        
                            if not hold[0].isdigit():

                                hold = hold[1:]
                        
                            grades.append(hold)
            
            return grades 

        pdf = 'transcript.pdf'
        extractedText = extractTextFromPdf(pdf)

        lines_list = extractedText.splitlines()
    
        #Whatever choice they choose for the school they are in, we will use that schools search function

        creditsAndGrades = JohnJaySearch()

        grade_mapping = {'A+': 4.0, 'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0, 'B-': 2.7, 'C+': 2.3, 'C': 2.0, 'C-': 1.7, 'D+': 1.3, 'D': 1.0, 'D-': 0.7, 'F': 0.0}

        total_credits = 0
        weighted_gpa_sum = 0

        for entry in creditsAndGrades:
            if entry[0].isdigit() and entry[0] != '0':
                credits = int(entry[:4][0])
                grade = entry[4:]  
                total_credits += credits
                weighted_gpa_sum += grade_mapping[grade] * credits
        
        if total_credits == 0:

            print("No classes counted")
        
        else:

            weighted_gpa = weighted_gpa_sum / total_credits

            majorGPA = round(weighted_gpa, 4)

            print(majorGPA)
        
        time.sleep(20)
    
    except Exception as e:

        print(f'An error occured: {e}')

    time.sleep(20)
