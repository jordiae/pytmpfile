from pytmpfile import get_tmp_path, tempdir
import os

if __name__ == '__main__':
    with get_tmp_path(content='print("hello")\n', suffix='.py') as tmp_path:
        print(f'{tmp_path} exists inside context manager: {os.path.exists(tmp_path)}')
        print('And it has this content:')
        with open(tmp_path, 'r') as f:
            print(f.read())
    print(f'{tmp_path} exists outside context manager: {os.path.exists(tmp_path)}')
    print(f'All files will be created in {tempdir()}')
