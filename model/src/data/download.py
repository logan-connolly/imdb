from pathlib import Path
from urllib import request
from urllib.error import URLError

from src.data.paths import DataDirs, source_to_url


def download_file_from_url(url: str, output_path: Path) -> None:
    """Download file to desired output path if does not already exist"""
    if output_path.exists():
        print(f"{output_path.name!r} already exists in data/raw, skipping download")
    else:
        print(f"Downloading from {url} to data/raw ...")
        try:
            request.urlretrieve(url, output_path)
        except (URLError, ValueError) as err:
            raise ValueError(f"{url} was not formatted correctly") from err


def download_data() -> None:
    """Download data files from the internet and store as gzipped compressed files"""
    for name, url in source_to_url().items():
        output_path = DataDirs.raw / f"{name}.tsv.gz"
        download_file_from_url(url, output_path)
