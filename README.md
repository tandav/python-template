# python-template
Template repo for python packages

## features
- [ ] configuration using `pyproject.toml`
- [x] build using setuptools
- [x] bumpver config
- [x] smoke test
- [x] pre-commit config
- [x] ci with tests, pre-commit checks and uploading to pypi
- [x] dependabot config

## install
```bash
# install from pypi
pip install mypackage

# development
pip install -e .[dev]

# or install the latest version from github
pip install git+https://github.com/tandav/mypackage
```
