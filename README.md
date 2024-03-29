<p align="center"><img  width=100%  src="https://i.imgur.com/v7r1AWr.png"  alt="687474703a2f2f6936332e74696e797069632e636f6d2f333031336c67342e706e67"  border="0" /></p>

<p align="center">
    <a href="https://algorand.com"><img src="https://img.shields.io/badge/Powered by-Algorand-blue.svg" alt="Frontend" /></a>
    <a href="https://tinyman.org"><img src="https://img.shields.io/badge/Powered by-TinyMan-yellow.svg" alt="Frontend" /></a>
    <a href="https://tinybar.app"><img src="https://img.shields.io/badge/Project-Website-Green.svg" /></a>
    <a><img src="https://visitor-badge.glitch.me/badge?page_id=aorumbayev.tinybar&right_color=green" /></a>
    <a href="https://algoexplorer.io/address/RKHBPXNJ2FLDLTMLY6622WFP6S7YGNATLPI2PFVULQPQBQI7C5IY3N3US4"><img src="https://img.shields.io/badge/Tips-Algo-black.svg" alt="Frontend" /></a>
    <br>
    <br>
    <a href="https://github.com/aorumbayev/tinybar/releases/download/v0.4.0/TinyBar.zip"><img src="https://img.shields.io/badge/Click to-Download-cyan.svg" /></a>
</p>

## 📃 About

A simple MacOS menu bar app to display current coins from most popular Liquidity Pools on [TinyMan.org](https://tinyman.org/) 🤖

![Alt Text](https://media0.giphy.com/media/AuM0IkgPk8JnzBiDyM/giphy.gif?cid=790b761191e349aa088248e8fdad6edfd657e1471ed5bd49&rid=giphy.gif&ct=g)

_**⚠️ NOTE: This is a pre-release version, utility is under active development.**_

---

## Prerequisites

- [python 3.9.x](https://www.python.org/)
- [poetry](https://python-poetry.org/)
- [pre-commit](https://pre-commit.com/)

## 🚀 Quick start

If you are looking for quick executable installation refer to links below:

- [MacOS latest](https://github.com/aorumbayev/tinybar/releases/)

Afterwards, you can download latest `TinyBar.zip` file and move `*.app` file to `Applications` folder.

> Currently available on M1 Macs via Rosseta only.
> Additionally, note that the .app artifact is not signed, you need to navigate to `System Preferences` -> `Security & Privacy` -> `Click lock to make changes` -> allow `TinyBar.app` to run.

### Features

Be aware that by default the tool displays a `USDC` equivalent of `ALGO` after performing a swap between 1 `UNIT` of selected `ASA` and `ALGO`.

- ✅ - 5 Pairs available by default. _(Available)_
- ✅ - Add any Asset by ASA ID. _(Available)_
- ⚠️ - CI/CD _(Partially configured)_
- 🚧 - Custom base currency. _(only ALGO at the moment)_
- 🚧 - Code signed MacOS executables _(TBD)_

## ⚙️ Installation

_(for devs/contributors only )_

This section assumes that `poetry` and `pre-commit` are installed and executed from the root folder of this repository.

1. Clone the repo

```bash
git clone https://github.com/aorumbayev/tinybar
```

2. Install `python` requirements

```bash
poetry install # install all dependencies
poetry shell # activate virtual env
```

3. Configure `pre-commit` hooks

```bash
pre-commit install
```

4. Run tinybar in dev mode

```bash
(.venv) PYTHONPATH="." python src/tinybar.py
```

5. (optional) Build app executable

```bash
(.venv) PYTHONPATH="." python3 setup.py py2app
```

## 🧪 Testing

TBD

## 🙋‍♂️ Contribution guideline

TBD

## ⭐️ Stargazers

Special thanks to everyone who forked or starred the repository ❤️

[![Stargazers repo roster for @aorumbayev/tinybar](https://reporoster.com/stars/dark/aorumbayev/tinybar)](https://github.com/aorumbayev/tinybar/stargazers)

[![Forkers repo roster for @aorumbayev/tinybar](https://reporoster.com/forks/dark/aorumbayev/tinybar)](https://github.com/aorumbayev/tinybar/network/members)
