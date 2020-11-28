import unittest

from rendermd.shell import generate_markdown


class ShellTest(unittest.TestCase):
    def test_shell_generator(self) -> None:
        original_content = """
[//]: # (rendermd.shell.start`echo success`)
[//]: # (rendermd.end)
"""
        new_content, diff = generate_markdown(original_content.splitlines())
        assert (
            new_content.splitlines()
            == """
[//]: # (rendermd.shell.start`echo success`)
success
[//]: # (rendermd.end)""".splitlines()
        )
