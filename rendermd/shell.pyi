from .core import Diff as Diff, MarkdownGenerator as MarkdownGenerator
from typing import Any, List, Tuple

def get_command_output(command: str) -> str: ...

class ShellGenerator(MarkdownGenerator):
    block_start: Any = ...
    def generate_content(self, original_lines: List[str], file_path: str=...) -> Tuple[str, Diff]: ...
