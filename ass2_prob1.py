C1 = [0xe9, 0x3a, 0xe9, 0xc5, 0xfc, 0x73, 0x55, 0xd5]
C2 = [0xf4, 0x3a, 0xfe, 0xc7, 0xe1, 0x68, 0x4a, 0xdf]

M1_XOR_M2 = [c ^ d for c, d in zip(C1, C2)]
with open('/usr/share/dict/words', 'r') as words_file:
    words = words_file.read().split()
    words = set([word for word in words if len(word) == len(M1_XOR_M2)])
    for word1 in words:
        M1 = [ord(c) for c in word1]
        M2 = [c ^ d for c, d in zip(M1, M1_XOR_M2)]
        word2 = ''.join([chr(c) for c in M2])
        if word2 in words:
            pad = [c ^ d for c, d in zip(M1, C1)]
            print('Word1 = %s, Word2 = %s, pad = %s' % (word1, word2, pad))
