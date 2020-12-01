from .core import Diff as Diff
from enum import Enum
from typing import Any

class Printer(Enum):
    HEADER: str = ...
    BLUE: str = ...
    CYAN: str = ...
    GREEN: str = ...
    WARNING: str = ...
    RED: str = ...
    FAIL: str = ...
    RESET: str = ...
    BOLD: str = ...
    UNDERLINE: str = ...
    def print(self, msg: str) -> None: ...
    @classmethod
    def print_colored_diff(cls: Any, diff: Diff) -> None: ...