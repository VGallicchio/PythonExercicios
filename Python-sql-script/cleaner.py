import csv
import unidecode
import unicodedata

# convert the source file to utf-16 and clean
# change utf-8 to the encoding of the source file as necessary
with open("PythonDOJO-SQL/movies.csv", 'rt', encoding='utf-8',
          errors='replace', newline='') as rf, \
     open("PythonDOJO-SQL/clean_file.csv", 'wt', encoding='cp1251',
          errors='ignore', newline='') as wf:

        # add other csv parameters as necessary
        # (https://docs.python.org/3/library/csv.html#dialects-and-formatting-parameters)
        reader = csv.reader(rf, delimiter=',')
        for row in reader:
            wf.write(','.join(f.strip() for f in row))
            wf.write('\n')

