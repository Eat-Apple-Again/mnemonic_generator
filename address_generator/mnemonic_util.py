from bip_utils import Bip39MnemonicGenerator, Bip39SeedGenerator, Bip39WordsNum

def generate_mnemonic_24() -> str:
    """Generate 24-word mnemonic."""
    # Some bip-utils versions require instance method call
    return str(Bip39MnemonicGenerator().FromWordsNumber(Bip39WordsNum.WORDS_NUM_24))
