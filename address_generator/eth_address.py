# ETH EOA via BIP-44
from bip_utils import Bip44, Bip44Coins, Bip44Changes

def eth_address(seed_bytes: bytes, account: int = 0, index: int = 0) -> str:
    """m/44'/60'/account'/0/index -> 0x-address (EIP-55)."""
    ctx = Bip44.FromSeed(seed_bytes, Bip44Coins.ETHEREUM)
    node = ctx.Purpose().Coin().Account(account).Change(Bip44Changes.CHAIN_EXT).AddressIndex(index)
    return node.PublicKey().ToAddress()
