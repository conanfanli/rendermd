
[//]: # (start:toc)
Table of Contents
=================
- [renderme](#renderme)
- [Usage](#usage)

[//]: # (end)

# renderme

Render markdown templates.

# Usage
[//]: # (start:shell`python -m rendermd.command_line --help`)
```
usage: rendermd [-h] [-p PATTERNS] [--no-recursive]

Render markdown templates. This command recursively search the current
directly and find all markdown files by matching given patterns (default to
"**/README.md").

optional arguments:
  -h, --help            show this help message and exit
  -p PATTERNS, --pattern PATTERNS
                        Comma separated list of markdown files to populate
  --no-recursive        Do not search for files recursively
```

[//]: # (end)


# Examples

## Inject Table of Contents

Before running `rendermd`.
```markdown
[//]: # (start_toc)
[//]: # (end)

# h1

## h2
```

After running `rendermd`.
```markdown
[//]: # (start_toc)
Table of Contents
=================
- [h1](#h1)
    - [h2](#h2)

[//]: # (end)

# h1

## h2
```

## Inject output of shell commands

Before running `rendermd`.
```markdown
[//]: # (start:shell`echo success`)
[//]: # (end)
```

After running `rendermd`.
```markdown
[//]: # (start:shell`echo success`)
success

[//]: # (end)
```
