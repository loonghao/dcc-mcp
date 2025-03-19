# Your Project Name

<div align="center">

[![PyPI version](https://badge.fury.io/py/your-project-name.svg)](https://badge.fury.io/py/your-project-name)
[![Build Status](https://github.com/username/your-project-name/workflows/Build%20and%20Release/badge.svg)](https://github.com/username/your-project-name/actions)
[![Documentation Status](https://readthedocs.org/projects/your-project-name/badge/?version=latest)](https://your-project-name.readthedocs.io/en/latest/?badge=latest)
[![Python Version](https://img.shields.io/pypi/pyversions/your-project-name.svg)](https://pypi.org/project/your-project-name/)
[![License](https://img.shields.io/github/license/username/your-project-name.svg)](https://github.com/username/your-project-name/blob/main/LICENSE)
[![Downloads](https://static.pepy.tech/badge/your-project-name)](https://pepy.tech/project/your-project-name)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Ruff](https://img.shields.io/badge/ruff-enabled-brightgreen)](https://github.com/astral-sh/ruff)

</div>

Your project description

## Features

- Feature 1
- Feature 2
- Feature 3

## Installation

```bash
pip install your-project-name
```

Or with Poetry:

```bash
poetry add your-project-name
```

## Usage

```python
import your_project_name

# Add usage examples here
```

## Development

### Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/your-project-name.git
cd your-project-name

# Install dependencies with Poetry
poetry install
```

### Testing

```bash
# Run tests with nox
nox -s pytest

# Run linting
nox -s lint

# Fix linting issues
nox -s lint_fix
```

### Documentation

```bash
# Build documentation
nox -s docs

# Serve documentation with live reloading
nox -s docs-serve
```

## License

MIT

## GitHub Actions Configuration

This template uses GitHub Actions for CI/CD. The following workflows are included:

- **Build and Release**: Tests the package on multiple Python versions and operating systems, and publishes to PyPI when a new release is created.
- **Documentation**: Builds and deploys documentation to GitHub Pages.
- **Dependency Review**: Scans dependencies for security vulnerabilities.
- **Scorecards**: Analyzes the security health of the project.

The release workflow uses PyPI's trusted publishing, which means you don't need to set up any PyPI API tokens. Instead, you'll need to configure trusted publishing in your PyPI project settings once you've created your package. See [PyPI's documentation on trusted publishing](https://docs.pypi.org/trusted-publishers/) for more information.

### Release Process

To create a new release:

1. Update the version in `pyproject.toml`
2. Update the `CHANGELOG.md` with the new version and changes
3. Commit and push the changes
4. Create a new tag with the version number (e.g., `1.0.0`)
5. Push the tag to GitHub

```bash
# Example release process
git add pyproject.toml CHANGELOG.md
git commit -m "Release 1.0.0"
git tag 1.0.0
git push && git push --tags
```

The GitHub Actions workflow will automatically build and publish the package to PyPI.
