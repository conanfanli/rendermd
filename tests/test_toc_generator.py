import tempfile
import unittest

from rendermd.toc import generate_markdown_toc

TOC_BLOCK = ("[//]: # (START_TOC)", "[//]: # (END_TOC)")


class TocTest(unittest.TestCase):
    def test_toc_generator(self) -> None:
        with tempfile.NamedTemporaryFile() as fp:

            original_content = """
[//]: # (START_TOC)
[//]: # (END_TOC)

# h1

## h2

    """
            fp.write(original_content.encode("utf-8"))
            fp.seek(0)

            new_content, diff = generate_markdown_toc(
                original_content.splitlines(), fp.name
            )
            assert (
                new_content.splitlines()
                == """
[//]: # (START_TOC)
Table of Contents
=================
- [h1](#h1)
    - [h2](#h2)

[//]: # (END_TOC)

# h1

## h2

    """.splitlines()
            )
