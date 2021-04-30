from pathlib import Path

import pytest

from src.data import paths


@pytest.fixture
def mock_data_dir(monkeypatch):
    """Patch DATAPATH constant to point to test data directory"""
    mock_data_dir = Path(__file__).parent / "data"
    monkeypatch.setattr(paths, "DATAPATH", mock_data_dir)
    return mock_data_dir
