from src.data.download import download_data
from src.data.extract import extract_data
from src.data.preprocess import combine_data, preprocess_data


def get_data():
    """Orchestration function for downloading, extracting, and processing data"""
    download_data()
    extract_data()
    preprocess_data()
    combine_data()


if __name__ == "__main__":
    get_data()
