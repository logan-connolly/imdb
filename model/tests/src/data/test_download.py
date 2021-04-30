import pytest

from src.data.download import download_file_from_url


@pytest.mark.parametrize("url", ["google.com", "htt://google.com"])
def test_invalid_url(url, tmp_path):
    """Check that invalid URLs raise ValueErrors"""
    with pytest.raises(ValueError):
        download_file_from_url(url, tmp_path / "dummy_file")
