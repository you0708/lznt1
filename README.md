# LZNT1
Python implementation of LZNT1 compression/decompression.

Note that the compression algorithm is not perfect, but compressed data can be decompressed by RtlDecompressBuffer.

# How to use
## Install
```
pip install lznt1
```

## Compress / decompress
```
>>> import lznt1
>>> compressed = lznt1.compress(data)
>>> decompressed = lznt1.decompress(compressed)
```

## Test
```
C:\Users\you\Desktop>python test.py lznt1.py
[*] input size = 4034 bytes, sha1 hash = e19250d48c1e46d7d0fa46a5d345487d723559cd
[*] size of compressed1: 1264
[*] size of compressed2: 1559
[*] sha1 hash of compressed1: 720bd5775ee3273deaebabb29a412ea079fa79ae
[*] sha1 hash of compressed2: 8df2fe59dba7fa4d4d01a8f12f05d7b5799238cc
[*] sha1 hash of decompressed11: e19250d48c1e46d7d0fa46a5d345487d723559cd
[*] sha1 hash of decompressed12: e19250d48c1e46d7d0fa46a5d345487d723559cd
[*] sha1 hash of decompressed21: e19250d48c1e46d7d0fa46a5d345487d723559cd
[*] sha1 hash of decompressed22: e19250d48c1e46d7d0fa46a5d345487d723559cd
```

## References
* [MS-XCA]: LZNT1 Algorithm Details
  * https://msdn.microsoft.com/en-us/library/jj665697.aspx
* coderforlife/ms-compress: Open source implementations of Microsoft compression algorithms
  * https://github.com/coderforlife/ms-compress

## License
Apache License 2.0. See [LICENSE](/LICENSE).
