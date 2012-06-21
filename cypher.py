phrase = str(raw_input('Please a enter phrase you would like to encode: '))
shift_value = int(raw_input('Your shift value: '))
encoded_phrase = ''

for c in phrase:
    ascii_code = ord(c) + shift_value
    encoded_phrase = ascii_code
    encode_phrase = encoded_phrase + c 
    print encoded_phrase
