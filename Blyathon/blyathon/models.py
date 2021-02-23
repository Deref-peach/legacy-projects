from dataclasses import dataclass
from typing import List


@dataclass
class CodeModel:
    comment: List[str]
    string: List[str]
    docstrings: List[str]
    code: List[str]
