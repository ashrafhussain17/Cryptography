capital = list(range(65, 65 + 26))
small = list(range(97, 97 + 26))
special_char = [32, 33, 40, 41, 44, 45, 46, 63]
valid_chars = set(capital + small + special_char)

C1 = [32, 14, 162, 166, 143, 97, 199, 84, 128, 186, 67, 246, 43, 37, 76, 222, 75, 131, 131, 185, 79, 149, 100, 201, 116,
      219, 101, 188, 112, 206, 25, 63, 147, 142, 153, 112, 190, 67, 231, 37, 246, 85, 249, 123, 161, 135, 215, 124, 193,
      143, 135, 201, 67, 237, 54, 246, 74, 196, 77, 80]
C2 = [39, 0, 27, 44, 224, 51, 18, 23, 10, 43, 233, 81, 198, 215, 123, 142, 182, 124, 137, 167, 108, 187, 67, 244, 104,
      192, 128, 151, 142, 174, 124, 225, 32, 250, 13, 90, 212, 35, 82, 206, 41, 3, 33, 236, 84, 242, 7, 60, 0, 21, 20,
      36, 167, 143, 136, 201, 104, 164, 119, 218]
C3 = [36, 10, 29, 37, 8, 28, 68, 254, 37, 16, 233, 93, 197, 133, 236, 29, 5, 36, 253, 57, 138, 216, 26, 34, 58, 82, 169,
      192, 66, 8, 22, 123, 140, 135, 140, 137, 158, 96, 200, 64, 219, 111, 217, 82, 252, 100, 164, 158, 186, 155, 108,
      193, 75, 254, 38, 167, 159, 105, 184, 157]
C4 = [35, 6, 19, 53, 170, 127, 168, 114, 203, 116, 131, 188, 100, 181, 139, 153, 140, 136, 220, 78, 218, 52, 196, 114,
      170, 203, 159, 246, 47, 18, 17, 56, 201, 64, 207, 94, 214, 43, 19, 9, 250, 30, 9, 5, 114, 206, 86, 251, 18, 52,
      239, 77, 144, 180, 121, 163, 151, 141, 146, 164]
C5 = [58, 204, 20, 103, 216, 44, 2, 14, 54, 235, 45, 25, 9, 26, 42, 234, 67, 249, 8, 36, 250, 19, 164, 143, 140, 237,
      80, 245, 55, 27, 227, 75, 203, 20, 236, 60, 233, 45, 19, 15, 226, 6, 59, 248, 55, 9, 16, 59, 23, 63, 135, 205, 66,
      230, 75, 197, 109, 170, 126, 143]
C6 = [57, 205, 18, 17, 70, 214, 112, 183, 108, 207, 47, 29, 20, 33, 72, 204, 51, 232, 51, 236, 45, 246, 19, 3, 35, 13,
      47, 8, 75, 247, 13, 114, 130, 142, 138, 146, 159, 127, 190, 8, 227, 7, 39, 236, 78, 182, 69, 255, 79, 244, 40, 49,
      243, 72, 254, 47, 27, 20, 231, 56]
C7 = [51, 23, 237, 70, 242, 6, 99, 132, 181, 111, 141, 177, 100, 251, 98, 162, 154, 134, 155, 139, 144, 159, 99, 210,
      67, 247, 10, 32, 163, 168, 123, 161, 103, 181, 71, 148, 134, 146, 130, 158, 125, 181, 215, 77, 242, 91, 191, 39,
      61, 19, 21, 107, 172, 150, 205, 91, 236, 43, 255, 16]
C8 = [39, 7, 25, 32, 28, 238, 27, 239, 94, 213, 103, 213, 91, 245, 76, 197, 99, 220, 34, 17, 242, 48, 216, 15, 17, 55,
      12, 38, 251, 64, 139, 164, 119, 192, 79, 156, 158, 125, 181, 111, 157, 142, 183, 107, 217, 81, 169, 152, 172, 193,
      90, 233, 63, 242, 44, 224, 4, 20, 225, 99]
C9 = [35, 6, 31, 114, 172, 120, 185, 81, 189, 126, 131, 183, 111, 128, 179, 119, 158, 133, 144, 185, 68, 138, 143, 142,
      135, 232, 120, 202, 95, 227, 39, 10, 23, 227, 48, 233, 47, 211, 2, 4, 31, 7, 105, 169, 147, 190, 64, 168, 172,
      149, 146, 164, 98, 199, 62, 249, 79, 222, 35, 116]
C10 = [32, 14, 162, 189, 125, 158, 131, 204, 108, 210, 45, 15, 67, 29, 10, 28, 19, 2, 4, 55, 219, 97, 189, 96, 220, 120,
       217, 99, 230, 106, 186, 223, 36, 226, 34, 228, 101, 191, 96, 234, 16, 60, 23, 10, 119, 217, 40, 3, 89, 231, 33,
       54, 237, 93, 218, 92, 128, 132, 157, 171]

tenciphs = [C1, C2, C3, C4, C5, C6, C7, C8, C9, C10]
print(tenciphs)


def encrypt(msg, pad, prev_c=0):
    assert len(msg) == len(pad)
    result = []
    for i in range(len(msg)):
        c = msg[i] ^ ((pad[i] + prev_c) % 256)
        result.append(c)
        prev_c = c
    return result


def decrypt(ctext, pad, prev_c=0):
    result = []
    for i in range(len(ctext)):
        b = ctext[i] ^ ((pad[i] + prev_c) % 256)
        result.append(b)
        prev_c = ctext[i]
    return result


def text_to_bytes(t):
    return [ord(c) for c in t]


def bytes_to_text(t):
    return [chr(c) for c in t]


def calculate_pad(ctext, msg, prev_c=0):
    assert len(ctext) == len(msg)
    pad = []
    for i in range(len(ctext)):
        p = ((ctext[i] ^ msg[i]) - prev_c) % 256
        pad.append(p)
        prev_c = ctext[i]
    return pad


def prev_c_at(ciph, index):
    return 0 if index == 0 else ciph[index - 1]


def ctext_at(ciph, index):
    return ciph[index: index + 1]


msglen = 60
possible_pad_bytes = [[] for _ in range(msglen)]
for index in range(msglen):
    for c in valid_chars:
        #print(ctext_at(tenciphs[0], index))
        possible_pad_bytes = calculate_pad(ctext_at(tenciphs[0], index), [c], prev_c=prev_c_at(tenciphs[0], index))
        #print(possible_pad_bytes)
        is_valid = True
        for ciph in tenciphs:
            msg = decrypt(ctext_at(ciph, index), possible_pad_bytes)
            print(msg)
            if not set(msg).issubset(valid_chars):
                is_valid = False
                break
        if is_valid:
            print(possible_pad_bytes[index])
            print(possible_pad_bytes[0])
            possible_pad_bytes[index].append(possible_pad_bytes[0])


def recursively_expand_pad(cur_pad, cur_index, words):
    if cur_index == msglen:
        texts = [bytes_to_text(decrypt(ciph[: msglen], cur_pad)) for ciph in tenciphs]
        text_to_score = '\n'.join(texts).lower()
        score = sum(len(word) ** 2 for word in words if word in text_to_score)
        return score, texts, cur_pad
    else:
        best_score = 0
        best_texts = None
        best_pad = None
        for p in possible_pad_bytes[cur_index]:
            score, texts, pad = recursively_expand_pad(cur_index + 1, cur_pad + [p], words)
            if best_score < score:
                best_score = score
                best_texts = texts
                best_pad = pad
        return best_score, best_texts, best_pad


with open('/usr/share/dict/words ', 'r') as words_file:
    words = set([word.lower() for word in words_file.read().split()])
    _, texts, pad = recursively_expand_pad(0, [], words)
    print('messages = %s, pad = %s' % (texts, pad))
