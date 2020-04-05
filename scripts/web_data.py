import requests
from bs4 import BeautifulSoup, SoupStrainer
from classes import linkClass
from links import RemoteLinks


def getExamClasses(url, pattern):
    '''
    Gets all the seperate classes(English, Spanish, Math).

    Parameters:
    url (string): Handled automatically. The string to the webpage (check enum)
    pattern (string): used to determine whether it is the proper link.

    Returns:
    List of linkClass objects
    '''
    print('Fetching Exam links...')
    page = requests.get(url).text
    soup = BeautifulSoup(page, "lxml")
    exams = []
    for p in soup.find_all('p'):
        link = ""
        name = ""

        if len(p.find_all('a')) > 0:
            for a in p.find_all('a'):
                print(f"Fetching {a.text}")
                link = a['href']
                name = a.text

            for span in p.find_all('span'):
                name = name + span.text

            exams.append(linkClass(name, link))

    print('Finished downloading Exam links')
    return exams


def getExamSeasons(url):
    '''
    Gets all the seasons (Nov 2019, June 2018, etc.) for a class.

    Pass the result from getExamLinks()

    Parameters:
    url (string): The url of the class page

    Returns:
    A list of linkClass objects.
    '''
    print('Fetching exam seasons')
    page = requests.get(url).text
    soup = BeautifulSoup(page, "html.parser")
    examSeasons = []
    for a in soup.find_all('a', {"class": 'clearfix'}):
        link = requests.head(a['href'], allow_redirects=True).url
        name = a.find_all('label')[0].text
        examSeasons.append(linkClass(name, link))
        print(f'Fetching {link}')

    return examSeasons


def getExams(url):
    '''
    Gets all the individual exams(Question papers, Mark schemes, etc.)

    Pass the result from getExamSeasons()

    Parameters:
    url (string): The url of the exam season

    Returns:
    A list of linkClass objects
    '''
    print('Fetching individual exams...')
    page = requests.get(url).text
    soup = BeautifulSoup(page, "html.parser")
    exams = []
    for a in soup.find_all('a'):
        if a.has_attr('download'):
            examUrl = RemoteLinks.PAST_PAPERS.value + a['href']
            examName = a['href'].split('/')[-1]
            # print(examName)
            print(f'Fetching URL for {examUrl}')
            exams.append(linkClass(examName, examUrl))
    return exams
