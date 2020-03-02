ciphertext = open("ciphertext.txt", "r")
decripted_message = ciphertext.read()
ciphertext.close()

plaintext = open("plaintext.txt", "r")
original_message = plaintext.read()
plaintext.close()

key = open("key.txt", "r")
first_key = key.read()
key.close()

IC_difference = [100.0] * 30
arra = []
IC_for_english = 0.0686
original_freq = [0.0815, 0.0144, 0.0276, 0.0379, 0.1311, 0.0292, 0.0199, 0.0526, 0.0635, 0.0013, 0.0042, 0.0339, 0.0254,
                 0.0710, 0.0800, 0.0198, 0.0012, 0.0683, 0.0610, 0.1047, 0.0246, 0.0092, 0.0154, 0.0017, 0.0198, 0.0008]


def shift_string(string, idx):
    ans = ''
    for i in range(0, len(string)):
        x = ord(string[i]) - idx
        if x < 97:
            x += 26
        ans += chr(x)
    return ans


def get_IC(length, msg):
    coset = [''] * length
    for i in range(0, len(msg)):
        index = i % length
        coset[index] += msg[i]

    h, w = length, 26
    local_freq = [[0.0 for x in range(w)] for y in range(h)]

    d = 0.0
    average = 0.0

    for i in range(0, length):
        sz = len(coset[i])

        for j in range(0, 26):
            local_freq[i][j] = 0.0
        for j in range(0, sz):
            local_freq[i][ord(coset[i][j]) - 97] += 1

        for j in range(0, 26):
            temp = local_freq[i][j]
            temp *= (temp - 1)
            d += temp

        d /= (sz * 1.0)
        d /= (sz - 1.0)
        average += d
    ic = average / length
    return ic


def get_key_size(message):
    icValues = [0.0] * 30
    for i in range(3, 30):
        icValues[i] = get_IC(i, message)

    min_diff = 100000
    key_length = 2

    for i in range(3, 30):
        temp = IC_for_english - icValues[i]
        if temp < 0:
            temp *= -1
        IC_difference[i] = temp
        if temp < min_diff:
            min_diff = temp
            key_length = i
            print(key_length)
    return key_length


def guessed_key(message, key_size):
    coset = [''] * 30
    for i in range(0, len(message)):
        index = i % key_size
        coset[index] += message[i]

    h, w = key_size, 26
    local_freq = [[0.0 for x in range(w)] for y in range(h)]
    coset_size = (len(message) + key_size - 1) // key_size
    h, w = 26, coset_size + 5
    x2 = [[0.0 for x in range(w)] for y in range(h)]

    flag = 0
    for k in range(0, 26):

        for i in range(0, key_size):
            coset[i] = shift_string(coset[i], flag)

        for i in range(0, key_size):
            sz = len(coset[i])

            for j in range(0, 26):
                local_freq[i][j] = 0.0
            for j in range(0, sz):
                local_freq[i][ord(coset[i][j]) - 97] += 1
            for j in range(0, 26):
                local_freq[i][j] /= (sz * 1.0)

            for j in range(0, 26):
                temp = local_freq[i][j] - original_freq[j]
                temp *= temp
                temp /= original_freq[j]
                x2[k][i] += temp


            # print(local_freq[i])

        flag = 1

    key = ''

    for i in range(0, key_size):
        pos = 0
        minVal = x2[0][i]
        for j in range(1, 26):
            print(x2[j][i])
            if x2[j][i] < minVal:
                minVal = x2[j][i]
                #print(minVal)
                pos = j

        key += chr(97 + pos)
        arra.append(key)
        print(arra)

    return arra


def formatText(message):
    filteredMessage = ''
    for i in range(0, len(message)):
        if message[i] != ' ':
            filteredMessage += message[i]

    filteredMessage = filteredMessage.lower()
    return filteredMessage


def format_original_message(message):
    filteredMessage = ''
    for i in range(0, len(message)):
        if 65 <= ord(message[i]) <= 90:
            filteredMessage += message[i]

        if 97 <= ord(message[i]) <= 122:
            filteredMessage += message[i]

    filteredMessage.lower()
    return filteredMessage


def decode(message, key):
    decript_message = ''
    for i in range(0, len(message)):
        if int(ord(message[i])) < 91:
            a = int(ord(message[i])) - 65
        if int(ord(message[i])) > 96:
            a = int(ord(message[i])) - 97
        if int(ord(key[i])) < 91:
            b = int(ord(key[i])) - 65
        if int(ord(key[i])) > 96:
            b = int(ord(key[i])) - 97
        temp = (a - b) % 26
        if int(ord(message[i])) < 91:
            decript_message += chr(temp + 65)
        if int(ord(message[i])) > 96:
            decript_message += chr(temp + 97)

    return decript_message


def get_encrypted_message(message, key):
    demoKey = key
    for i in range(len(key), len(message)):
        demoKey += key[i % len(key)]
    # print(message)
    # print(demoKey)
    decript_message = decode(message, demoKey)
    return decript_message


def compare_function(originalMessage, message, originalKey, key):
    print('Original key size: ' + str(len(originalKey)))
    print('Predicted key: ' + key)
    print('Original key: ' + originalKey)

    matched, unmatched = 0, 0
    for i in range(0, min(len(key), len(originalKey))):
        if key[i] == originalKey[i]:
            matched += 1
        else:
            unmatched += 1

    unmatched += abs(len(key) - len(originalKey))
    temp = (100.0 * matched) / (matched + unmatched)
    print('Matched : ' + str(matched))
    temp = 100 - temp
    print('Unmatched : ' + str(unmatched))

    print('Original message: \n' + originalMessage)
    print('Predicted message: \n' + message)
    matched, unmatched = 0, 0
    for i in range(0, min(len(message), len(originalMessage))):
        if message[i] == originalMessage[i]:
            matched += 1
        else:
            unmatched += 1
    unmatched += abs(len(originalMessage) - len(message))
    temp = (100.0 * matched) / len(message)
    print('Matched character: ' + str(matched) + ', accuracy = ' + str(temp)[0:5] + '%')
    temp = 100 - temp
    print('Unmatched character: ' + str(unmatched) + ', deviation = ' + str(temp)[0:5] + '%')

    return


message = formatText(decripted_message)
original_Messsage = format_original_message(original_message)
key_size = get_key_size(message)
#print('Possible key size: ' + str(key_size))
key_array = guessed_key(message, key_size)
for i in range(len(key_array)):
    decript_message = get_encrypted_message(message, key_array[i])
    compare_function(original_Messsage, decript_message, first_key, key_array[i])
