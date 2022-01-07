# -*-coding:utf-8-*-
import os
from langconv import tradition2simple


def tradition2simple_directory(dir_path):
    for file in os.listdir(dir_path):
        filepath = os.path.join(dir_path, file)
        if os.path.isdir(filepath):
            tradition2simple_directory(r'D:\Documents\Github2022\Learn-Git-in-30-days\zh-tw')
        elif file.endswith('.md'):
            lines = []
            for line in open(filepath, 'r', encoding='utf8'):
                lines.append(tradition2simple(line))

            with open(filepath, 'w', encoding='utf8') as fout:
                fout.write(''.join(lines))


if __name__ == '__main__':
    tradition2simple_directory(r'D:\Documents\Github2022\Learn-Git-in-30-days')
