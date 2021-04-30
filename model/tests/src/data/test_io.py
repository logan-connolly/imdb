import pytest

from src.data.io import read_compressed_file, read_from_tsv
from src.data.io import write_decompressed_file, write_to_tsv


def test_read_compressed_file_not_found(tmp_path):
    """Raise when file is not found on disk"""
    with pytest.raises(FileNotFoundError):
        read_compressed_file(tmp_path / "made_up_file.tsv.gz")


def test_read_tsv_file_not_found(tmp_path):
    """Raise when file is not found on disk"""
    with pytest.raises(FileNotFoundError):
        read_from_tsv(tmp_path / "made_up_file.tsv.gz")


def test_write_decompressed_file(tmp_path):
    """Write data files to disk and check if they exist"""
    pass


def test_write_tsv_file(tmp_path):
    """Write data files to disk and check if they exist"""
    pass
