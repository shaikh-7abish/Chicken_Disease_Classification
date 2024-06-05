from dataclasses import dataclass
from pathlib import Path

# creating a dataclass means data type for checking the return type of a function
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_files: Path
    unzip_file: Path
