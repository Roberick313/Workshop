def encode_decode(password: str = None,
                  decode_password: str = None):

    out_put = ''

    if not decode_password:

        reverse_input = first_reverse(password)

        for i in reverse_input:

            def encrypt(input_parameter) -> int:

                en_bowl = ((input_parameter * 7) // 2) - 1

                return en_bowl

            out_put += chr(encrypt(ord(i)))

        return out_put

    else:
        for i in decode_password:

            def decryption(input_parameter) -> int:

                en_bowl = ((input_parameter * 2) // 7) + 1

                return en_bowl

            out_put += chr(decryption(ord(i)))

        return first_reverse(out_put)


def first_reverse(entry_parameter):
    """this func will make the entered string revers"""

    string = ''
    length = len(entry_parameter)

    for i in range(length - 1, -1, -1):
        string += entry_parameter[i]

    return string


if __name__ == "__main__":
    print(encode_decode('Roberick'))