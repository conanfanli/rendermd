import difflib
import re
import subprocess
from typing import Tuple

from .printer import Diff

SHELL_START = re.compile(r"\[//\]: # \(rendermd.shell.start`(.+)`\)")
SHELL_END = "[//]: # (rendermd.end)"


def get_command_output(command: str) -> str:
    """Return command output wrapped in block."""
    result = subprocess.run(command, shell=True, capture_output=True)
    if result.returncode == 0:
        return result.stdout.decode("utf-8").strip()
    elif result.stderr:
        raise Exception(result.stderr.decode("utf-8").strip())
    raise Exception(f"{result}")


def generate_markdown(file_path: str) -> Tuple[str, Diff]:
    """Given a markdown file, generate table of contents.

    Returns:
        (content, diff)
    """
    with open(file_path) as infile:
        original_lines = []
        resulted_lines = []

        inside_toc_block = False
        contains_toc = False

        for line in infile.readlines():
            line = line.rstrip("\n")
            original_lines.append(line)

            if line.startswith("[//]") and (match := SHELL_START.match(line)):
                command = match.group(1)
                inside_toc_block = True
                contains_toc = True
                resulted_lines += (
                    [line] + get_command_output(command).splitlines() + [SHELL_END]
                )
            elif line.startswith(SHELL_END):
                inside_toc_block = False
                continue

            if not inside_toc_block:
                resulted_lines.append(line)

    return (
        "\n".join(resulted_lines),
        contains_toc
        and Diff(list(difflib.context_diff(original_lines, resulted_lines)))
        or Diff([]),
    )
