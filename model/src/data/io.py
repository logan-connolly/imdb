import gzip
from pathlib import Path

import pandas as pd

from src.data.paths import DataDirs


def read_compressed_file(file_path: Path) -> bytes:
    """Read in .tsv.gz file from disk"""
    try:
        with gzip.open(file_path, "rb") as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"{file_path!r} not found on disk")


def write_decompressed_file(tsv_content: bytes, output_path: Path) -> None:
    """Write extracted tsv file to disk"""
    with open(output_path, "wb") as f:
        f.write(tsv_content)


def read_from_tsv(file_path: Path):
    """Read in tsv file from external data"""
    try:
        read_kwargs = {"dtype": "object", "sep": "\t", "na_values": [r"\N"]}
        return pd.read_csv(file_path, **read_kwargs)
    except FileNotFoundError as err:
        raise FileNotFoundError(f"Could not find file {file_path.name!r}") from err


def write_to_tsv(df: pd.DataFrame, file_path: Path):
    """Write dataframe to csv format"""
    df.to_csv(file_path, sep="\t", index=False)


def read_processed_data():
    """Read in data that was preprocessed, specifying data types"""
    file_path = DataDirs.processed / "processed.tsv"
    try:
        return pd.read_csv(file_path, sep="\t")
    except FileNotFoundError as err:
        raise FileNotFoundError(f"Could not find file {file_path.name!r}") from err
