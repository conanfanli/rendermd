import tempfile
import unittest

from rendermd.toc import TocGenerator

TOC_BLOCK = ("[//]: # (START_TOC)", "[//]: # (END_TOC)")


class TocTest(unittest.TestCase):
    def test_toc_generator(self) -> None:
        g = TocGenerator()
        with tempfile.NamedTemporaryFile() as fp:

            original_content = f"""
{g.block_start}
{g.block_end}

# h1

## h2

    """
            fp.write(original_content.encode("utf-8"))
            fp.seek(0)

            new_content, diff = g.generate_content(
                original_content.splitlines(), fp.name
            )
            assert (
                new_content.splitlines()
                == f"""
{g.block_start}
Table of Contents
=================
- [h1](#h1)
    - [h2](#h2)

{g.block_end}

# h1

## h2

    """.splitlines()
            )
