from dotenv import load_dotenv
import lzma
import os
from tqdm import tqdm

load_dotenv()


def read_files_dir(path: str, file_format=".txt"):
    """Read all files in a directory with a specific format

    Args:
        path (str): _description_
        file_format (str, optional): _description_. Defaults to ".txt".

    Returns:
        _type_: _description_
    """
    files = []
    for filename in os.listdir(path):
        if filename.endswith(file_format) and os.path.isfile(
            os.path.join(path, filename)
        ):
            files.append(filename)

    return files


if __name__ == "__main__":
    data_dir_path = os.getenv("DATA_DIR")
    files = read_files_dir(data_dir_path, file_format=".txt")
    vocab = set()

    # if we have 20 files, we will compresss them into n_files
    n_files = int(os.getenv("NUMBER_OF_FILES_SPLIT"))
    max_files_per_split = len(files) // n_files if n_files != 0 else len(files)

    # split the files into n_files
    for i in range(n_files):
        with open(f"{data_dir_path}/train_data_{i+1}.txt", "w") as f:
            for j, filename in enumerate(
                tqdm(files[:max_files_per_split], total=max_files_per_split)
            ):
                file_path = os.path.join(data_dir_path, filename)
                # lzma is for file formats that are compressed (e.g., xz)
                # with lzma.open(file_path, "rt", encoding="utf-8") as infile:
                with open(file_path, "r", encoding="utf-8") as infile:
                    for _, l in enumerate(tqdm(infile)):
                        text = l.strip() + "\n"
                        f.write(text)
                        vocab.update(set(text))

            files = files[max_files_per_split:]

    with open(f"{data_dir_path}/vocab.txt", "w") as vf:
        vf.write("\n".join(vocab))
