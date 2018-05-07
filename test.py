import argparse
import ctypes
from hashlib import sha1
import lznt1

parser = argparse.ArgumentParser(description='LZNT1 tester (You must run this on Windows)')
parser.add_argument("FILE", help="Specify a file for compression/decompression test")
args = parser.parse_args()

def main():
    with open(args.FILE, 'rb') as fp:
        data = fp.read()
    #data = "Hello world!" * 800
    print('[*] input size = {} bytes, sha1 hash = {}'.format(len(data), sha1(data).hexdigest()))
    compressed1 = lznt1.compress(data)
    decompressed11 = lznt1.decompress(compressed1)

    buf_decompressed = ctypes.create_string_buffer(len(data)*2)
    final_size = ctypes.c_ulong(0)
    ctypes.windll.ntdll.RtlDecompressBuffer(2, buf_decompressed, ctypes.sizeof(buf_decompressed), ctypes.c_char_p(compressed1), len(compressed1), ctypes.byref(final_size))
    decompressed12 = buf_decompressed.raw[:final_size.value]

    buf_compressed = ctypes.create_string_buffer(len(data)*2)
    work_size = ctypes.c_ulong(0)
    work_frag_size = ctypes.c_ulong(0)
    ctypes.windll.ntdll.RtlGetCompressionWorkSpaceSize(2, ctypes.byref(work_size), ctypes.byref(work_frag_size))
    workspace = ctypes.create_string_buffer(work_size.value)
    final_size = ctypes.c_ulong(0)
    ctypes.windll.ntdll.RtlCompressBuffer(2, ctypes.c_char_p(data), len(data), buf_compressed, ctypes.sizeof(buf_compressed), 4096, ctypes.byref(final_size), workspace)
    compressed2 = buf_compressed.raw[:final_size.value]

    decompressed21 = lznt1.decompress(compressed2)

    buf_decompressed = ctypes.create_string_buffer(len(data)*2)
    final_size = ctypes.c_ulong(0)
    ctypes.windll.ntdll.RtlDecompressBuffer(2, buf_decompressed, ctypes.sizeof(buf_decompressed), buf_compressed, ctypes.sizeof(buf_compressed), ctypes.byref(final_size))
    decompressed22 = buf_decompressed.raw[:final_size.value]

    print('[*] size of compressed1: {}'.format(len(compressed1)))
    print('[*] size of compressed2: {}'.format(len(compressed2)))
    print('[*] sha1 hash of compressed1: {}'.format(sha1(compressed1).hexdigest()))
    print('[*] sha1 hash of compressed2: {}'.format(sha1(compressed2).hexdigest()))
    print('[*] sha1 hash of decompressed11: {}'.format(sha1(decompressed11).hexdigest()))
    print('[*] sha1 hash of decompressed12: {}'.format(sha1(decompressed12).hexdigest()))
    print('[*] sha1 hash of decompressed21: {}'.format(sha1(decompressed21).hexdigest()))
    print('[*] sha1 hash of decompressed22: {}'.format(sha1(decompressed22).hexdigest()))

if __name__ == '__main__':
    main()
