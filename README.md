# cryptographic hash prefix and last few bytes finding-algorithm

## what is it
This is a CLI script, that when given a 64-byte string, it finds a suitable 4-byte prefix so that, a SHA256 hash of the prefix combined with the original string of bytes, has two last bytes as 0xca, 0xfe that mades cofe you can change it so it finds hash with last to byte what ever you want or you can make it start with 30 zeros like how bitcoin work. Script should expect the original string to be passed in hexadecimal format and should return two lines, first being the SHA256 string found and second 4-byte prefix used (in hexadecimal format). all made from scratch in python.

For example:
```
python3 main.py 129df964b701d0b8e72fe7224cc71643cf8e000d122e72f742747708f5e3bb6294c619604e52dcd8f5446da7e9ff7459d1d3cefbcc231dd4c02730a22af9880c
```
Should return:
9100cfcd92292bf65ea84ab448db234807f341f90861f6ed0f052d93e8e3``cafe``
## how to run it

```
git clone https://github.com/Toni-d-e-v/cryptographic-hash-finding-algorithm/
python3 main.py your hash or string
```
