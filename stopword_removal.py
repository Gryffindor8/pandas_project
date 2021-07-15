import glob
import os

stop_words = []

with open("stopwords-de.txt", encoding='utf-8') as f:
    for word in f:
        word = word.split('\n')
        stop_words.append(word[0])
result = []
for filepath in glob.glob(os.path.join('', '*.tok')):
    file = open(filepath, 'r', encoding='utf-8')
    string = file.read()
    li = list(string.split(" "))
    li = [x.lower() for x in li]
    li = [word.replace(",", '').replace('.', '').replace('%', '').replace(';', '')
              .replace('!', '').replace('—', '').replace(':', '').replace("-", '') for word in li]
    li = [x for x in li if x]

    li = [word.replace("\n", '') for word in li]
    # li = [word.replace("\n", '' for word in li]
    r = [t for t in li if not t in stop_words]
    result.append(r)

non_stop_words_files = ['1974-Schmidt-SPD.nostop', '1976-Schmidt-SPD.nostop', '1980-Schmidt-SPD.nostop',
                        '1983-Kohl-CDU.nostop', '1987-Kohl-CDU.nostop', '1991-Kohl-CDU.nostop']

for i, j in zip(range(len(result)), non_stop_words_files):
    with open(j, 'w') as f:
        for item in result[i]:
            f.write("%s " % item)
