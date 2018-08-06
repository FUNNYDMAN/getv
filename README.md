# Getv

[![Documentation Status](https://readthedocs.org/projects/getv/badge/?version=latest)](https://getv.readthedocs.io/en/latest/?badge=latest)


#### please notice, package not ready for production!

This package provides simple way to get last version string from github. It may be useful if you wanna display this info somewhere in your project. 

## Getting started

Now package is available  only on [https://test.pypi.org](https://test.pypi.org)

1. Download it via pip:
```bash
pip install --index-url https://test.pypi.org/project/ getv
```

2. Check installation
```bash
pip list
```
## How to use it

```python
from getv.main import get_last_version
get_last_version()
```