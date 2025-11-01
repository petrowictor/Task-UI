def postcode_to_name(postcode: str) -> str:
    digits = [int(postcode[i:i+2]) for i in range(0, 10, 2)]
    return ''.join(chr(ord('a') + (d % 26)) for d in digits)