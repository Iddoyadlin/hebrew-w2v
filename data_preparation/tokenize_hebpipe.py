import subprocess
from pathlib import Path

from base import get_config, get_absolute_path


def run_hebpipe_command(split_corpus_folder: Path, tokenized_output_folder: Path):
    command = f'python -m hebpipe {split_corpus_folder}/* -o pipes --dirout {tokenized_output_folder} -w -t'
    print(f"\nplease run hebpipe separately by running \n`{command}`. "
          "\nmake sure correct python environment is configured and java JRA and JDK are installed."
          " see more details at {https://github.com/amir-zeldes/HebPipe}\n")


if __name__ == "__main__":
    config = get_config()
    tokenized_output_folder = get_absolute_path(config["TOKENIZED_OUTPUT_FOLDER"])
    split_corpus_folder = get_absolute_path(config["SPLIT_CORPUS_OUTPUT_FOLDER"])
    run_hebpipe_command(split_corpus_folder, tokenized_output_folder)
