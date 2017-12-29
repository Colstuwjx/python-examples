# coding=utf-8

import re


def main():
    regex = r'(\[.*?\]\s*){4}\s*\[(.*?)\]'
    source = '''[2017-12-29 15:53:50,214] [INFO] [6:DummyThread-21] [ccqueue.worker:_execute:50] [task-ebd1baab-1418-49c9-8d01-51484948a6f3]\nTask ebd1baab-1418-49c9-8d01-51484948a6f3 succeeded.'''

    m = re.search(regex, source)
    print m.group(2)


if __name__ == "__main__":
    main()
