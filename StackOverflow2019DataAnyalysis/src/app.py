# Script to Analyze Stack Overflow Developer Survey CSV

import csv
from collections import defaultdict, Counter


# path to csv data file (may need to change)
__csv_file = 'data/survey_results_public.csv'

__reader = {}
def read_file():
    with open(__csv_file) as f:
        __reader = csv.DictReader(f)


def headers():
    '''Print all the headers in the csv'''
    if not __reader:
        read_file()

    for line in __reader.keys:
        print(line)


def main():
    betterLife = Counter()

    with open(__csv_file) as f:
        reader = csv.DictReader(f)

        langs = Counter();
        total = 0
        for key in reader:
            langs.update(key['LanguageWorkedWith'].split(';'))
            total += 1

       # [print(key) for key in langs.elements()]

        # # [betterLife.update(line['BetterLife']) for line in reader]
        # for line in reader:
        #     betterLife[line['BetterLife']] += 1

    print(betterLife)

if __name__ == '__main__':
    read_file()
    headers()
    # keyvalues()
