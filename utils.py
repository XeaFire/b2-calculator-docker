def bytes_to_bits_binary(byte_data):
    bits_data = bin(int.from_bytes(byte_data, byteorder='big'))[2:]
    bits_data = bits_data.zfill(len(byte_data) * 8)
    return bits_data