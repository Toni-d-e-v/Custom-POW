# cryptographic-hash-finding-algorithm
This is a CLI script, that when given a 64-byte string, it finds a suitable 4-byte prefix so that, a SHA256 hash of the prefix combined with the original string of bytes, has two last bytes as 0xca, 0xfe that mades cofe you can change it so it finds hash with last to byte what ever you want or you can make it start with 30 zeros like how bitcoin work. Script should expect the original string to be passed in hexadecimal format and should return two lines, first being the SHA256 string found and second 4-byte prefix used (in hexadecimal format). all made from scratch in python.

For example:
```
python3 main.py 129df964b701d0b8e72fe7224cc71643cf8e000d122e72f742747708f5e3bb6294c619604e52dcd8f5446da7e9ff7459d1d3cefbcc231dd4c02730a22af9880c
```
Should return:
6681edd1d36af256c615bf6dcfcda03c282c3e0871bd75564458d77c529d```cafe```
