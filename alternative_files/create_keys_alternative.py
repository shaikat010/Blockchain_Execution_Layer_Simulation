import os
from ecdsa import NIST384p, SigningKey
from ecdsa.util import randrange_from_seed__trytryagain

def make_key(seed):
  secexp = randrange_from_seed__trytryagain(seed, NIST384p.order)
  return SigningKey.from_secret_exponent(secexp, curve=NIST384p)

seed = os.urandom(NIST384p.baselen) # or other starting point
sk1a = make_key(seed)
sk1b = make_key(seed)
# note: sk1a and sk1b are the same key
assert sk1a.to_string() == sk1b.to_string()
sk2 = make_key(b"2-"+seed)  # different key
assert sk1a.to_string() != sk2.to_string()

