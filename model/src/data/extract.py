from pathlib import Path

from src.data.io import read_compressed_file, write_decompressed_file
from src.data.paths import DataDirs, source_to_raw_path


def extract_file(file_path: Path, output_path: Path) -> None:
    """Extract contents of compressed file to output path"""
    if output_path.exists():
        print(f"{output_path.name!r} already exists in data/external, skipping extract")
    else:
        file_content = read_compressed_file(file_path)
        write_decompressed_file(file_content, output_path)


def extract_data():
    """Extract compressed files for each raw data file"""
    for name, raw_file_path in source_to_raw_path().items():
        output_path = DataDirs.external / f"{name}.tsv"
        extract_file(raw_file_path, output_path)
