from functools import partial
from typing import Callable

import pandas as pd
import seaborn as sns

from src.data.io import read_processed_data
from src.data.paths import FIGPATH

SeabornPlot = Callable[..., sns.FacetGrid]


def plot_fig(df: pd.DataFrame, plt_fn: SeabornPlot, name: str, **kwargs) -> None:
    """Create plot figure and write out to reports/figures"""
    fig = plt_fn(data=df, **kwargs)
    fig_path = FIGPATH / f"{plt_fn.__name__}_{name}.svg"
    fig.savefig(fig_path, format="svg")


def generate_hists(df: pd.DataFrame) -> None:
    """Generate histogram plots for numeric columns"""
    create_hist = partial(plot_fig, df=df, plt_fn=sns.displot, kind="hist")
    create_hist(name="runtime", x="runtimeMinutes")
    create_hist(name="ratings", x="averageRating")
    create_hist(name="year", x="startYear")


def generate_scatter_plots(df: pd.DataFrame) -> None:
    """Generate scatter plots for numeric columns"""
    create_scatter = partial(plot_fig, df=df, plt_fn=sns.relplot, kind="scatter")
    create_scatter(name="runtime", x="runtimeMinutes", y="averageRating")
    create_scatter(name="year", x="startYear", y="averageRating")
    create_scatter(name="votes", x="numVotes", y="averageRating")


if __name__ == "__main__":
    df = read_processed_data()
    sampled = df.sample(1000)
    generate_hists(df)
    generate_scatter_plots(sampled)
