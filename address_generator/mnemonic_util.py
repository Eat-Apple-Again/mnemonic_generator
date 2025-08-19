# mnemonic_(util|utils).py
from bip_utils import Bip39MnemonicGenerator, Bip39SeedGenerator, Bip39WordsNum

def generate_mnemonic_24() -> str:
    """Generate 24-word mnemonic."""
    # Some bip-utils versions require instance method call
    return str(Bip39MnemonicGenerator().FromWordsNumber(Bip39WordsNum.WORDS_NUM_24))

def mnemonic_to_seed(mnemonic: str, passphrase: str = "") -> bytes:
    """Mnemonic -> 64-byte seed (PBKDF2-HMAC-SHA512)."""
    return Bip39SeedGenerator(mnemonic).Generate(passphrase)
