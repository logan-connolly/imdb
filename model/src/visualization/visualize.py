from functools import partial

import pandas as pd
from seaborn import displot

from src.data.io import read_processed_data
from src.data.paths import FIGPATH


def create_fig(df: pd.DataFrame, plt_fn, name: str, **kwargs) -> None:
    """Create plot figure and write out to reports/figures"""
    fig = plt_fn(df, **kwargs)
    fig_path = FIGPATH / f"{plt_fn.__name__}_{name}.svg"
    fig.savefig(fig_path, format="svg")


def generate_hists(df: pd.DataFrame) -> None:
    """Generate histogram plots for numeric columns"""
    create_hist = partial(create_fig, df=df, plt_fn=displot, kind="hist")
    create_hist(name="runtime", x="runtimeMinutes")
    create_hist(name="ratings", x="averageRating")
    create_hist(name="year", x="startYear")


if __name__ == "__main__":
    df = read_processed_data()
    generate_hists(df)
