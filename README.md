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
C:\Users\you\Desktop\ln>python test.py lznt1.py
[*] input size = 4067 bytes, sha1 hash = 9887522d4088152ca434a5f275adcd99c2de338d
[*] size of compressed1: 1280
[*] size of compressed2: 1553
[*] sha1 hash of compressed1: 64b9b5f92274e60d10f3ef0e517f563cc8d46bd6
[*] sha1 hash of compressed2: 92e737ee1d2b468800169cc7b28854b392ac8395
[*] sha1 hash of decompressed11: 9887522d4088152ca434a5f275adcd99c2de338d
[*] sha1 hash of decompressed12: 9887522d4088152ca434a5f275adcd99c2de338d
[*] sha1 hash of decompressed21: 9887522d4088152ca434a5f275adcd99c2de338d
[*] sha1 hash of decompressed22: 9887522d4088152ca434a5f275adcd99c2de338d
```

## References
* [MS-XCA]: LZNT1 Algorithm Details
  * https://msdn.microsoft.com/en-us/library/jj665697.aspx
* coderforlife/ms-compress: Open source implementations of Microsoft compression algorithms
  * https://github.com/coderforlife/ms-compress

## License
Apache License 2.0. See [LICENSE](/LICENSE).
