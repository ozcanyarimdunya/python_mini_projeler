"""

"""
import crypt
from hmac import compare_digest as compare_hash

enc = crypt.crypt('pass', "hello")
print(enc)

dcr = compare_hash(enc, crypt.crypt('pass', enc))
print(dcr)
