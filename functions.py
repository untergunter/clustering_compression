from io import StringIO

def compress(uncompressed:str):
    """Compress a string to a list of output symbols."""

    last = ''
    compression_dictionary = {last:0}
    last_char_id = 1
    compressed = [last]
    for character in uncompressed:
        lc = last + character
        if lc in compression_dictionary:
            last = lc
        elif lc not in compression_dictionary:
            compression_dictionary[lc] = last_char_id
            last_char_id += 1
            if lc != character:
                code_of_last = compression_dictionary[last]
                compressed.append(code_of_last)
            compressed.append(character)
            last = ''
    if last !='':
        # off by one
        code_of_last = compression_dictionary[lc]
        compressed.append(code_of_last)
    return compressed, compression_dictionary


def decompress(compressed:list):
    """Decompress a list of output ks to a string."""
    decrypting = dict()

    last_char_id = 0
    result = StringIO()
    current_index = 0
    last_index = len(compressed)
    while current_index < last_index:
        next_enc = compressed[current_index]
        current_index += 1

        if type(next_enc) == int:
            # it is already in our decrypting dict
            decrypted = decrypting[next_enc]

            if current_index==last_index:
                # this is not the end
                result.write(decrypted)

            else:
                # this is not the end yet
                letter = compressed[current_index]
                current_index += 1
                current = decrypted + letter
                decrypting[last_char_id] = current
                last_char_id += 1
                result.write(current)

        elif type(next_enc) == str:
            # first time we see that character
            decrypting[last_char_id] = next_enc
            last_char_id += 1
            result.write(next_enc)


    result_string = result.getvalue()
    return result_string


# %%
txt = 'aababbabbaabac'
#txt = 'abc'
c, d = compress(txt)
print(c)
print(d)
dc = decompress(c)
print(dc)
print(txt == dc)
