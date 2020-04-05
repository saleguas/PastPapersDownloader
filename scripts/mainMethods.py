from links import RemoteLinks
import file_management
import web_data
import threading
import sys


def downloadExamSection(currentPath, examClass):
    '''
    Used for multithreaded downloading.

    Parameters:
    currentPath (string): The path to the class folder(accounting, comp sci)
    examSection (linkClass): The linkClass object to a section.

    Returns:
    Nothing.
    '''
    test = []
    sectionPath = file_management.createFolder(currentPath, examClass.name)
    seasonExams = web_data.getExamSeasons(examClass.url)
    for seasonExam in seasonExams:
        seasonPath = file_management.createFolder(sectionPath, seasonExam.name)
        exams = web_data.getExams(seasonExam.url)
        test.append(exams)
        file_management.populateFolders(seasonPath, exams)
    sys.exit()


def downloadCAIE(folderName, pattern, url, syllabusCode):
    '''
    Downloads a CAIE exam (no PRE-U).

    Enter the syllabus code for the exam to download. Type ALL to download all the exams.

    Parameters:
    folderName (string): the name of the folder to store the files
    pattern (string): pattern used to identify whether a link is valid

    Returns:
    Nothing.
    '''

    currentPath = file_management.createFolder('output', folderName)
    examClasses = web_data.getExamClasses(url, pattern)
    if syllabusCode.lower() == 'all':
        for examClass in examClasses:
            processThread = threading.Thread(
                target=downloadExamSection, args=(currentPath, examClass))
            processThread.start()
    else:
        examClass = list(filter(lambda x: syllabusCode in x.name, examClasses))
        if len(examClass) > 0:
            examClass = examClass[0]
            print(examClass)
            downloadExamSection(currentPath, examClass)


def printDivider():
    bar = '-' * 50
    print()
    print(bar)
    print('*' * 50)
    print(bar)
    print()


def downloadAICE(syllabusCode):
    downloadCAIE('AS and A Levels', RemoteLinks.AICE_PATTERN.value,
                 RemoteLinks.AICE.value, syllabusCode)


def downloadIGCSE(syllabusCode):
    downloadCAIE('IGCSEs', RemoteLinks.IGCSE_PATTERN.value,
                 RemoteLinks.IGCSE.value, syllabusCode)


def downloadO(syllabusCode):
    downloadCAIE('O Levels', RemoteLinks.O_PATTERN.value,
                 RemoteLinks.O.value, syllabusCode)


def listClasses(value, pattern):
    exams = web_data.getExamClasses(
        value, pattern)
    printDivider()
    for exam in exams:
        print(exam.name)
    printDivider()

def listAICE():
    listClasses(RemoteLinks.AICE.value, RemoteLinks.AICE_PATTERN.value)

def listIGCSE():
    listClasses(RemoteLinks.IGCSE.value, RemoteLinks.IGCSE_PATTERN.value)

def listO():
    listClasses(RemoteLinks.O.value, RemoteLinks.O_PATTERN.value)
