from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, List

DATAPATH = Path(__file__).parents[2] / "data"


@dataclass
class Sources:
    basics: str = "basics"
    ratings: str = "ratings"


@dataclass
class DataDirs:
    raw: Path = DATAPATH / "raw"
    external: Path = DATAPATH / "external"
    interim: Path = DATAPATH / "interim"
    processed: Path = DATAPATH / "processed"


def get_sources() -> List[str]:
    """Get a list of sources from Sources dataclass"""
    sources_dict = asdict(Sources())
    return list(sources_dict.values())


def source_to_url() -> Dict[str, str]:
    """Get a dictionary of sources mapped to urls"""
    base_url = "https://datasets.imdbws.com"
    return {name: f"{base_url}/title.{name}.tsv.gz" for name in get_sources()}


def source_to_raw_path() -> Dict[str, Path]:
    """Get a dictionary of sources mapped to raw file paths"""
    return {name: DataDirs.raw / f"{name}.tsv.gz" for name in get_sources()}


def source_to_external_path() -> Dict[str, Path]:
    """Get a dictionary of sources mapped to external file paths"""
    return {name: DataDirs.external / f"{name}.tsv" for name in get_sources()}


def source_to_interim_path() -> Dict[str, Path]:
    """Get a dictionary of sources mapped to external file paths"""
    return {name: DataDirs.interim / f"{name}.tsv" for name in get_sources()}
