# BTC P2PKH via BIP-44
from bip_utils import Bip44, Bip44Coins, Bip44Changes

def btc_address(seed_bytes: bytes, account: int = 0, index: int = 0) -> str:
    """m/44'/0'/account'/0/index -> Base58Check P2PKH."""
    ctx = Bip44.FromSeed(seed_bytes, Bip44Coins.BITCOIN)
    node = ctx.Purpose().Coin().Account(account).Change(Bip44Changes.CHAIN_EXT).AddressIndex(index)
    return node.PublicKey().ToAddress()
