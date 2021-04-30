from src.data.extract import extract_file


def test_extract_file(mock_data_dir, tmp_path):
    """Test that sample ratings.tsv.gz file is extracted and written out"""
    file_path = mock_data_dir / "raw" / "ratings.tsv.gz"
    output_path = tmp_path / "ratings.tsv"

    extract_file(file_path, output_path)
    assert output_path.exists()
