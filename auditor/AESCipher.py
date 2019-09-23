from hashlib import md5
from base64 import b64decode, b64encode

from Crypto.Cipher import AES
from Crypto import Random

PADDING = '{'
BLOCK_SIZE = 32

pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING

class AESCipher:
  def __init__(self, key): 
        self.bs = 32
        self.key = self._pad(key).encode("utf8")

  def encrypt(self, raw):
    raw = self._pad('{}'.format(raw))
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(self.key, AES.MODE_CBC, iv)
    return b64encode(iv + cipher.encrypt(raw.encode("utf8")))

  def decrypt(self, enc):
    enc = b64decode(enc.decode("utf8"))
    iv = enc[:AES.block_size]
    cipher = AES.new(self.key, AES.MODE_CBC, iv)

    return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

  def _pad(self, s):
    return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

  @staticmethod
  def _unpad(s):
      return s[:-ord(s[len(s)-1:])]