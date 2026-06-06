# DCC-MCP

> [!IMPORTANT]
> **This project has been migrated to the [dcc-mcp organization](https://github.com/dcc-mcp).**
> Please visit the new organization repositories for the latest development and updates:
> - [dcc-mcp/dcc-mcp-core](https://github.com/dcc-mcp/dcc-mcp-core) — Core library
> - [dcc-mcp/dcc-mcp-maya](https://github.com/dcc-mcp/dcc-mcp-maya) — Maya integration
> - [dcc-mcp/dcc-mcp-blender](https://github.com/dcc-mcp/dcc-mcp-blender) — Blender integration
> - [dcc-mcp/dcc-mcp-houdini](https://github.com/dcc-mcp/dcc-mcp-houdini) — Houdini integration
> - [dcc-mcp/dcc-mcp-3dsmax](https://github.com/dcc-mcp/dcc-mcp-3dsmax) — 3ds Max integration
> - [dcc-mcp/dcc-mcp-photoshop](https://github.com/dcc-mcp/dcc-mcp-photoshop) — Photoshop integration
> - [dcc-mcp/dcc-mcp-zbrush](https://github.com/dcc-mcp/dcc-mcp-zbrush) — ZBrush integration
> - [dcc-mcp/dcc-mcp-openusd](https://github.com/dcc-mcp/dcc-mcp-openusd) — USD integration
>
> This repository will no longer receive active updates. Please update your references accordingly.

<div align="center">

[![PyPI version](https://badge.fury.io/py/dcc-mcp.svg)](https://badge.fury.io/py/dcc-mcp)
[![Build Status](https://github.com/loonghao/dcc-mcp/workflows/Build%20and%20Release/badge.svg)](https://github.com/loonghao/dcc-mcp/actions)
[![Documentation Status](https://readthedocs.org/projects/dcc-mcp/badge/?version=latest)](https://dcc-mcp.readthedocs.io/en/latest/?badge=latest)
[![Python Version](https://img.shields.io/pypi/pyversions/dcc-mcp.svg)](https://pypi.org/project/dcc-mcp/)
[![License](https://img.shields.io/github/license/loonghao/dcc-mcp.svg)](https://github.com/loonghao/dcc-mcp/blob/main/LICENSE)
[![Downloads](https://static.pepy.tech/badge/dcc-mcp)](https://pepy.tech/project/dcc-mcp)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Ruff](https://img.shields.io/badge/ruff-enabled-brightgreen)](https://github.com/astral-sh/ruff)

</div>

DCC-MCP is a unified implementation of the Model-Context-Protocol (MCP) for Digital Content Creation (DCC) software, designed to provide a consistent interface for various DCC applications used in the VFX and animation industry.

> **Note:** Frontend API is currently under development. Stay tuned for updates!
>
> Related components (dcc-mcp-core, dcc-mcp-maya, dcc-mcp-rpyc) are also under active development.

## Features

- Standardized implementation of MCP for DCC applications
- Consistent API across different DCC software (Maya, Houdini, Nuke, etc.)
- Cross-platform compatibility (Windows, Linux, macOS)
- Extensible architecture for custom integrations

## Installation

```bash
pip install dcc-mcp
```

Or with Poetry:

```bash
poetry add dcc-mcp
```

## Usage

```python
import dcc_mcp

# Example usage will be available once the API is finalized
```

## Development

### Setup

```bash
# Clone the repository
git clone https://github.com/loonghao/dcc-mcp.git
cd dcc-mcp

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

This project uses GitHub Actions for CI/CD. The following workflows are included:

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

## Download History

[![Download History](https://skill-history.com/chart/loonghao/dcc-mcp-creator.svg)](https://skill-history.com/loonghao/dcc-mcp-creator)
