# Learning Python Repository

A Consolidation of all my tutorial and learning projects for python

## Important notes

## Devtools

`pip install devtools`

```python
from devtools import debug

debug({
  "some": "thing",
  "num": 42,
})
```

## Ignoring noisy files in diff

add `.gitattributes` and add this line

```sh
# subsitute any other nosiy file here
poetry.lock -diff
```

Git will interpret the file (or extension with `*.whatever`) as a binary file 
and only show a message saying the file has changed.
