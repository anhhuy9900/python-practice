import os
from pathlib import Path

def main():
    join_path = os.path.join('usr', 'main', 'huy')
    print('join_path: ', join_path)
    print('Path: ', Path('usr').joinpath('main').joinpath('huy'))
    print('The current working directory: ', os.getcwd())
    print('Relative paths: ', os.path.relpath('/project/python'))
    print('Checking if a file/directory exists: ', os.path.exists('../oop'))

if __name__ == '__main__':
    main()
