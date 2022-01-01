from setuptools import setup

APP = ["src/tinybar.py"]
DATA_FILES = []
OPTIONS = {
    "argv_emulation": True,
    "iconfile": "icon.png",
    "plist": {"CFBundleShortVersionString": "1.0.0", "LSUIElement": True},
    "packages": ["rumps", "requests"],
}

setup(
    app=APP,
    name="TinyBar",
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
    install_requires=[
        "rumps",
        "requests",
        "tinyman-py-sdk",
        "py-algorand-sdk",
        "tinyman-py-sdk @ git+ssh://git@github.com/tinymanorg/tinyman-py-sdk@main#egg=tinyman-py-sdk",
    ],
)
