#!/usr/bin/env python
from argparse import ArgumentError
from argparse import ArgumentParser
from pathlib import Path
from tqdm import tqdm

from base import get_absolute_path


def parse_args():
    parser = ArgumentParser("Post process HebPipe output to a single file")
    parser.add_argument("-f", "--folder", metavar="FOLDER", help="Input folder", required=True)
    parser.add_argument("-o", "--output", help='Output file', required=True)
    args = parser.parse_args()
    return args


def get_paths(input_folder: str, output: str):
    folder = get_absolute_path(input_folder)
    assert folder.is_dir(), "folder must be a valid folder"
    output = get_absolute_path(output)
    assert not output.exists(), "output must not be an existing file"
    return folder, output


def process_files(input_folder: Path, output: Path):
    if not input_folder.exists():
        input_folder.mkdir(parents=True)
    elif list(input_folder.glob('**/*')):
        print(f'there are already files in {input_folder}, skipping postprocessing tokenized corpus')
        return

    files = list(input_folder.glob('**/*'))
    if not files:
        print(f'no files were found in tokenized output folder {input_folder}.')
        return
    with output.open('wb+') as f2:
        for fname in tqdm(files, desc='processing files', total=len(files), unit='file'):
            with fname.open('rb') as f:
                lines = [clean_line(line.decode()) for line in f.readlines()]
            f2.write(' '.join(lines).strip().encode('utf-8'))
    print(f"saved final corpus to {output}")

def main():
    args = parse_args()
    folder, output = get_paths(args.folder, args.output)
    process_files(folder, output)


def clean_line(line):
    line = line.strip().replace("|", " ")
    if line in ("<s>", "</s>"):
        return '\n'
    else:
        return line


if __name__ == '__main__':
    try:
        main()
    except ArgumentError as e:
        print(e)
        exit(1)
