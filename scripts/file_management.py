import os
from collections import defaultdict
import requests

sortDict = {
    'er': 'Examiner Reports',
    'ms': 'Mark Schemes',
    'qp': 'Question Papers',
    'gt': 'Grade Thresholds',
    'in': 'Inserts'
}


def createFolder(path, name):
    '''
    Safely creates a folder at the location.

    Parameters:
    path (string):  the location the folder resides in
    name (string):  the name of the folder to be created

    Returns:
    string: The path to the new folder
    '''
    newPath = os.path.join(path, name)
    if not os.path.exists(newPath):
        os.makedirs(newPath)
    return newPath

# def sortExams(exams):
#     files = defaultdict(list)
#     keys = sortDict.keys()
#     for exam in exams:
#         code = exam.name.split('_')
#         print(code)
#         if code in keys:
#             files[sortDict[code]].append(exam)
#         else:
#             files['Others'].append(exam)
#     return files


def populateFolders(path, exams):
    '''
    Iterates through all exams and downloads the files to their respective folders.

    Pass the result from getExams()

    Parameters:
    path (string): the path of the exam season
    exams (list of linkClass): the exams with the downloadlink

    Returns:
    Nothing.
    '''
    # print(examDict)
    for exam in exams:
        print(f'Downloading {exam.name}')
        file = requests.get(exam.url, allow_redirects=True)
        with open(os.path.join(path, exam.name), 'wb') as examFile:
            examFile.write(file.content)
        # break
