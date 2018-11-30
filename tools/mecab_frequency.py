import sys
import  os
from glob import glob
from collections import Counter

import MeCab

def main():
    # input_dir = sys.argv[1]
    input_dir = '../wiki/articles/'
    tagger = MeCab.Tagger('')
    tagger.parse('')

    frequency = Counter()
    count_proccessed = 0

    for path in glob(os.path.join(input_dir, '*', 'wiki_**')):
        print('Proccessing {0}...'.format(path), file=sys.stderr)

        with open(path) as file:
            for content in iter_docs(file):

                tokens = get_tokens(tagger, content)

                frequency.update(tokens)

                count_proccessed += 1
                if count_proccessed % 10000 == 0:
                    print('{0} documents were proccerssesed.'.format(count_proccessed),
                        file=sys.stderr)

    for token, count in frequency.most_common(30):
        print(token, count, 'end...')

def iter_docs(file):
    for line in file:
        if line.startswith('<doc '):
            buffer = []
        elif line.startswith('</doc>'):
            countent = ''.join(buffer)
            yield countent
        else:
            buffer.append(line)

def get_tokens(tagger, content):
    tokens = []
    node = tagger.parseToNode(content)
    while node:
        category, sub_category = node.feature.split(',')[:2]

        if category == '名詞' and sub_category in ('固有名詞', '一般'):
            tokens.append(node.surface)
        node = node.next

    return tokens


if __name__ == '__main__':
    main()