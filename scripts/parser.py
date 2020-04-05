import argparse
import mainMethods

parser = argparse.ArgumentParser(description='Download Up-To-date Past Papers.')
parser.add_argument(
    '-A', '--AICE', help='Downloads the AICE As and A level exam with the syllabus code provided. Type ALL to download all exams(may take a while!).')

parser.add_argument(
    '-O', '--ORDINARY', help='Downloads the O-level exam with the syllabus code provided. Type ALL to download all exams(may take a while!).',)

parser.add_argument(
    '-I', '--IGCSE', help='Downloads the IGCSE exam with the syllabus code provided. Type ALL to download all exams(may take a while!).')

parser.add_argument(
    '-LA', '--LISTAICE', help='Lists all the As and A level AICE classes with the syllabus numbers.', action='store_true')

parser.add_argument(
    '-LO', '--LISTORDINARY', help='Lists all the O level classes with the syllabus numbers.', action='store_true')

parser.add_argument(
    '-LI', '--LISTIGCSE', help='Lists all the IGCSE classes with the syllabus numbers.', action='store_true')

# parser.add_argument(
#     '-A', '--AICE', help='Probably the most useful sort. Sorts files based on filegroups. For example, .txt and .docx would be moved to the Documents folder.')
args = vars(parser.parse_args())

if args['AICE']:
    mainMethods.downloadAICE(args['AICE'])

if args['ORDINARY']:
    mainMethods.downloadO(args['ORDINARY'])

if args['IGCSE']:
    mainMethods.downloadIGCSE(args['IGCSE'])

if args['LISTAICE']:
    mainMethods.listAICE()

if args['LISTORDINARY']:
    mainMethods.listO()

if args['LISTIGCSE']:
    mainMethods.listIGCSE()
