#!/usr/bin/env python
from setuptools import setup

setup(
    name="lznt1",
    version="0.2",
    author="You Nakatsuru",
    author_email="you0708@users.noreply.github.com",
    license="Apache License 2.0",
    description="Python module for LZNT1 compression/decompression",
    long_description="A Python module which provides compress/decompress features uzing LZNT1 algorithm. This doesn't reuqire ntdll.RtlCompressBuffer/RtlDecompressBuffer",
    py_modules=["lznt1"],
    url="https://github.com/you0708/lznt1/",
)
