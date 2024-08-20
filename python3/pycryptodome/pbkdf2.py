'''
Reference
    Getting Started with Python in VS Code: https://code.visualstudio.com/docs/python/python-tutorial
    
    pbkdf2: https://pycryptodome.readthedocs.io/en/latest/src/protocol/kdf.html#pbkdf2
    
    create requirements.txt: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/
'''

## Code executed in VS Code (1.92.2)

from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA256
import base64


def show_result(language, expected_B64, key):
    
    '''
    Computes the Base64 codification of key.
    Displays the programming language, key in hex and base64.
    Returns whether the derived key matches the expected value.
    '''
    b64_key = base64.b64encode(key)
    print ('Programming Language: {}'.format(language))
    print ('key : {}'.format(key.hex()))
    print ('b64_key : {}'.format(b64_key))

    return b64_key.decode("utf-8") == expected_B64


def main():
    '''
    This is the module that is invoked when the program is called from the command prompt.
    '''    
    PROGRAMMING_LANGUAGE = 'Python'
    EXPECTED_B64 = 'HUHmmDYsT+QAmY7nx4kFUy588szRTf4cPzXlOMfTuMw='
    password = b'my super secret'
    salt = b'\x41\x6C\x61\x6E\x42\x6F\x6E\x6E\x69\x63\x69\x2E\x63\x6F\x6D'
    key_length = 32
    iterations = 10000

    key = PBKDF2(password, salt, key_length, 10000, hmac_hash_module=SHA256)

    print ('The hash values match : {}'. format(show_result(PROGRAMMING_LANGUAGE, EXPECTED_B64, key)))
    

if __name__ == "__main__":
    main()