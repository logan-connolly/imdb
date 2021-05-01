from typing import Callable

import pandas as pd
from src.data.io import read_from_tsv, write_to_tsv
from src.data.paths import DataDirs, Sources, source_to_external_path


def get_cleaner(source: str) -> Callable[[pd.DataFrame], pd.DataFrame]:
    """Return a cleaner function based on the df source name"""

    def clean_basics(df: pd.DataFrame) -> pd.DataFrame:
        out_cols = ["tconst", "primaryTitle", "startYear", "runtimeMinutes", "genres"]
        df = df[(df.runtimeMinutes.str.isnumeric()) & (df.startYear.str.isnumeric())]
        df = df.astype({"startYear": "uint16", "runtimeMinutes": "uint16"})
        filter = (df.startYear >= 1930) & (df.runtimeMinutes.between(60, 240))
        return df.loc[filter, out_cols]

    def default(df: pd.DataFrame) -> pd.DataFrame:
        return df

    cleaners = {Sources.basics: clean_basics}
    return cleaners.get(source, default)


def preprocess_data() -> None:
    """Clean external files and write out cleaned files to interim"""
    for name, external_file_path in source_to_external_path().items():
        external_df = read_from_tsv(external_file_path)
        cleaned_df = get_cleaner(name)(external_df).dropna()
        output_path = DataDirs.interim / f"{name}.tsv"
        write_to_tsv(cleaned_df, output_path)
