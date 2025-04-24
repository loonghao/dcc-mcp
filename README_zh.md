# DCC-MCP

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

DCC-MCP 是一个为数字内容创作工具实现的模型-上下文-协议框架，为VFX和动画行业中各种DCC应用程序提供统一接口。

> **注意：** 前置API目前正在开发中，敬请期待！
>
> 相关组件 (dcc-mcp-core, dcc-mcp-maya, dcc-mcp-rpyc) 也正在积极开发中。

## 特性

- 统一的模型-上下文-协议架构，适用于各种DCC工具
- 跨软件的一致性API（Maya、Houdini、Nuke等）
- 跨平台兼容性（Windows、Linux、macOS）
- 可扩展的插件系统

## 安装

```bash
pip install dcc-mcp
```

或者使用 Poetry:

```bash
poetry add dcc-mcp
```

## 使用方法

```python
import dcc_mcp

# API最终确定后将提供使用示例
```

## 开发

### 环境设置

```bash
# 克隆仓库
git clone https://github.com/loonghao/dcc-mcp.git
cd dcc-mcp

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

本项目使用 GitHub Actions 进行 CI/CD。包含以下工作流：

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
