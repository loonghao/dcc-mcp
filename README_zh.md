# 项目名称

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

项目描述

## 特性

- 特性 1
- 特性 2
- 特性 3

## 安装

```bash
pip install your-project-name
```

或者使用 Poetry:

```bash
poetry add your-project-name
```

## 使用方法

```python
import your_project_name

# 在此添加使用示例
```

## 开发

### 环境设置

```bash
# 克隆仓库
git clone https://github.com/username/your-project-name.git
cd your-project-name

# 使用 Poetry 安装依赖
poetry install
```

### 测试

```bash
# 使用 nox 运行测试
nox -s pytest

# 运行代码检查
nox -s lint

# 修复代码风格问题
nox -s lint_fix
```

### 文档

```bash
# 构建文档
nox -s docs

# 启动带有实时重载功能的文档服务器
nox -s docs-serve
```

## 许可证

MIT

## GitHub Actions 配置

此模板使用 GitHub Actions 进行 CI/CD。包含以下工作流：

- **构建和发布**：在多个 Python 版本和操作系统上测试包，并在创建新版本时发布到 PyPI。
- **文档**：构建文档并部署到 GitHub Pages。
- **依赖审查**：扫描依赖项中的安全漏洞。
- **Scorecards**：分析项目的安全健康状况。

发布工作流使用 PyPI 的可信发布（trusted publishing）功能，这意味着您不需要设置任何 PyPI API 令牌。相反，您需要在创建包后在 PyPI 项目设置中配置可信发布。有关更多信息，请参阅 [PyPI 关于可信发布的文档](https://docs.pypi.org/trusted-publishers/)。

### 发布流程

创建新版本的步骤：

1. 更新 `pyproject.toml` 中的版本号
2. 更新 `CHANGELOG.md`，添加新版本和变更内容
3. 提交并推送更改
4. 创建一个带有版本号的新标签（例如 `1.0.0`）
5. 将标签推送到 GitHub

```bash
# 发布流程示例
git add pyproject.toml CHANGELOG.md
git commit -m "Release 1.0.0"
git tag 1.0.0
git push && git push --tags
```

GitHub Actions 工作流将自动构建包并发布到 PyPI。
