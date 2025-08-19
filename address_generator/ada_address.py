# ADA Shelley base address via bip-utils CIP-1852 (avoid Byron differences)
from bip_utils import Cip1852, Cip1852Coins, Bip44Changes, CardanoShelley

def ada_address(seed_bytes: bytes, account: int = 0, index: int = 0) -> str:
    """m/1852'/1815'/account'/0/index + stake m/1852'/1815'/account'/2/0 -> addr1..."""
    ctx = Cip1852.FromSeed(seed_bytes, Cip1852Coins.CARDANO_ICARUS)
    acc = ctx.Purpose().Coin().Account(account)
    shelley = CardanoShelley.FromCip1852Object(acc)
    addr_obj = shelley.Change(Bip44Changes.CHAIN_EXT).AddressIndex(index)
    return addr_obj.PublicKeys().ToAddress()
