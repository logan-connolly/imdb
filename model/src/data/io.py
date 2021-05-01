import gzip
from pathlib import Path

import pandas as pd


def read_compressed_file(file_path: Path) -> bytes:
    """Read in .tsv.gz file from disk"""
    try:
        print(f"Reading compressed file {file_path.name!r} from data/raw")
        with gzip.open(file_path, "rb") as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"{file_path!r} not found on disk")


def write_decompressed_file(tsv_content: bytes, output_path: Path) -> None:
    """Write extracted tsv file to disk"""
    with open(output_path, "wb") as f:
        print(f"Writing decompressed file {output_path.name!r} to data/external")
        f.write(tsv_content)


def read_from_tsv(file_path: Path):
    """Read in tsv file from external data"""
    try:
        print(f"Reading tsv file {file_path.name!r} from data/external")
        read_kwargs = {"dtype": "object", "sep": "\t", "na_values": [r"\N"]}
        return pd.read_csv(file_path, **read_kwargs)
    except FileNotFoundError as err:
        raise FileNotFoundError(
            f"Could not find file {file_path.name!r} in data/external"
        ) from err


def write_to_tsv(df: pd.DataFrame, file_path: Path):
    """Write dataframe to csv format"""
    print(f"Writing dataframe to {file_path.name!r} to data/interim")
    df.to_csv(file_path, sep="\t", index=False)
