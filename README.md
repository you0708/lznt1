# LZNT1
Python implementation of LZNT1 compression/decompression.

Note that the compression algorithm is not perfect, but compressed data can be decompressed by RtlDecompressBuffer.

# How to use

## Compress / decompress
```
>>> import lznt1
>>> compressed = lznt1.compress(data)
>>> decompressed = lznt1.decompress(data)
```
## Test
```
C:\Users\you\Desktop>lznt1.py lznt1.py
[*] input size = 6610 bytes, sha1 hash = 933dffa94c6ad78fb7f0396b2b1c39aa90065d57
[*] size of compressed1: 2961
[*] size of compressed2: 2512
[*] sha1 hash of compressed1: d1116a2e5b0471de956e0df031466231c8cc7831
[*] sha1 hash of compressed2: 6e8262dbe4988fe9b6d119b203c94201b0f6a4c4
[*] sha1 hash of decompressed11: 933dffa94c6ad78fb7f0396b2b1c39aa90065d57
[*] sha1 hash of decompressed12: 933dffa94c6ad78fb7f0396b2b1c39aa90065d57
[*] sha1 hash of decompressed21: 933dffa94c6ad78fb7f0396b2b1c39aa90065d57
[*] sha1 hash of decompressed22: 933dffa94c6ad78fb7f0396b2b1c39aa90065d57
```

## References
* [MS-XCA]: LZNT1 Algorithm Details
  * https://msdn.microsoft.com/en-us/library/jj665697.aspx
* coderforlife/ms-compress: Open source implementations of Microsoft compression algorithms
  * https://github.com/coderforlife/ms-compress

## License
Apache License 2.0. See [LICENSE](/LICENSE).
