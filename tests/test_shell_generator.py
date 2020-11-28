import unittest

from rendermd.shell import ShellGenerator


class ShellTest(unittest.TestCase):
    def test_shell_generator(self) -> None:
        g = ShellGenerator()
        original_content = f"""
[//]: # (start:shell`echo success`)
{g.block_end}
"""
        new_content, diff = g.generate_content(original_content.splitlines())
        assert (
            new_content.splitlines()
            == f"""
[//]: # (start:shell`echo success`)
success

{g.block_end}""".splitlines()
        )
