import tempfile
import unittest

from rendermd.toc import generate_markdown_toc

TOC_BLOCK = ("[//]: # (START_TOC)", "[//]: # (END_TOC)")


class TocTest(unittest.TestCase):
    def test_shell_generator(self) -> None:
        fp = tempfile.TemporaryFile()

        original_content = """
[//]: # (START_TOC)
[//]: # (END_TOC)

# h1

## h2

"""
        fp.write(original_content.encode("utf-8"))
        new_content, diff = generate_markdown_toc(
            original_content.splitlines(), fp.name
        )
        assert (
            new_content.splitlines()
            == """
[//]: # (START_TOC)
Table of Contents
=================
[//]: # (END_TOC)
            """.splitlines()
        )

        fp.close()
