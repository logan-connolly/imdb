from typing import Callable, Dict

import pandas as pd

from src.data.io import read_from_tsv, write_to_tsv
from src.data.paths import DataDirs, Sources, source_to_external_path


def clean_akas(df: pd.DataFrame) -> pd.DataFrame:
    """Clean akas data frame after reading"""
    out_cols = ["titleId", "title", "region"]
    region_mask = df.region == "DE"
    return df.loc[region_mask, out_cols]


def clean_basics(df: pd.DataFrame) -> pd.DataFrame:
    """Clean ratings data frame after reading"""
    out_cols = ["tconst", "primaryTitle", "startYear", "runtimeMinutes", "genres"]
    df = df[out_cols].dropna()
    df = df[df.runtimeMinutes.str.isnumeric()].astype(
        {"startYear": "uint16", "runtimeMinutes": "uint16"}
    )
    year_mask = df.startYear >= 1930
    runtime_min_mask = df.runtimeMinutes > 60
    runtime_max_mask = df.runtimeMinutes < 360
    return df.loc[(year_mask) & (runtime_min_mask) & (runtime_max_mask)]


def clean_ratings(df: pd.DataFrame) -> pd.DataFrame:
    """Clean ratings data frame after reading"""
    return df


def get_cleaners() -> Dict[str, Callable[[pd.DataFrame], pd.DataFrame]]:
    """Return a mapping of sources to cleaning functions"""
    return {
        Sources.akas: clean_akas,
        Sources.basics: clean_basics,
        Sources.ratings: clean_ratings,
    }


def preprocess_data() -> None:
    """Clean external files and write out cleaned files to interim"""
    cleaners = get_cleaners()
    for name, external_file_path in source_to_external_path().items():
        external_df = read_from_tsv(external_file_path)
        cleaned_df = cleaners[name](external_df).dropna()
        output_path = DataDirs.interim / f"{name}.tsv"
        write_to_tsv(cleaned_df, output_path)
