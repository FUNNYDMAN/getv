# Getv

> Display version info in your project

[![Documentation Status](https://readthedocs.org/projects/getv/badge/?version=latest)](https://getv.readthedocs.io/en/latest/?badge=latest)


#### please notice, package is not ready for production!

This package provides simple way to get last version string of project from github. It may be useful if you wanna display this info somewhere in your app. 

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

### Example usage with Flask
```python 
import os

from flask import Flask

from getv.main import GetVersion

app = Flask(__name__)

getv = GetVersion()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)

PATH_TO_V_FILE = os.path.join(PROJECT_DIR, 'version.txt')


@app.route('/')
def index():
    last_v = getv.get_last_version()
    getv.write_or_create_version_file(PATH_TO_V_FILE)
    return 'Project version %s' % last_v


if __name__ == "__main__":
    app.run()
```

[documentation](https://getv.readthedocs.io/en/latest/)
