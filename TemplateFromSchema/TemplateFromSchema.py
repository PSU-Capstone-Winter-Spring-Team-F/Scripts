import csv
import itertools
import json
import re
import sys

def main():
    print("Welcome to Template From Schema")

    inname = sys.argv[1]
    jname = ''

    with open(inname, newline='') as infile:
        reader = csv.reader(infile, delimiter='\t')
        jname = next(reader)
        jname = re.sub(r'[^A-Za-z]', '', f'''{jname}''')
        jtemp = {}
        for row in itertools.islice(reader, 0, None):
            if row[0] != 'nullable: true':
                jtemp[row[0]] = None

        print(jtemp)

        with open(f'''{jname}.json''', 'w') as outfile:
            jtemp.pop('}')
            json.dump(jtemp, outfile, indent=2)

    return 0


if __name__ == '__main__':
    main()
