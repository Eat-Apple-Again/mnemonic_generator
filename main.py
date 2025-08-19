# Unified CLI: --mode gen|input, --coin BTC|ETH|ADA|ALL
import argparse
from address_generator.mnemonic_util import generate_mnemonic_24, mnemonic_to_seed
from address_generator.btc_address import btc_address
from address_generator.eth_address import eth_address
from address_generator.ada_address import ada_address

COINS = ["BTC", "ETH", "ADA", "ALL"]

def derive_all(seed: bytes, account: int, index: int):
    """Derive three coins from one seed."""
    return {
        "BTC": btc_address(seed, account, index),
        "ETH": eth_address(seed, account, index),
        "ADA": ada_address(seed, account, index),
    }

def main():
    p = argparse.ArgumentParser(description="Mnemonic -> BTC/ETH/ADA address")
    p.add_argument("--mode", choices=["gen", "input"], required=True,
                   help="gen=generate 24 words; input=type your mnemonic")
    p.add_argument("--coin", choices=COINS, default="ALL", help="Select coin or ALL")
    p.add_argument("--account", type=int, default=0, help="HD account index")
    p.add_argument("--index", type=int, default=0, help="Address index")
    p.add_argument("--passphrase", default="", help="Optional BIP-39 passphrase")
    args = p.parse_args()

    if args.mode == "gen":
        mnemonic = generate_mnemonic_24()
        print(f"[Mnemonic 24] WRITE DOWN & KEEP OFFLINE:\n{mnemonic}\n")
    else:
        mnemonic = input("Enter mnemonic (12/15/18/21/24 words):\n").strip()

    seed = mnemonic_to_seed(mnemonic, args.passphrase)
    derived = derive_all(seed, args.account, args.index)

    print(f"(Passphrase: {'YES' if args.passphrase else 'NO'})")
    print(f"Account={args.account}, Index={args.index}")
    if args.coin == "ALL":
        for k, v in derived.items():
            print(f"{k}: {v}")
    else:
        print(f"{args.coin}: {derived[args.coin]}")

if __name__ == "__main__":
    main()

"""
uv run main.py --mode gen --coin ALL
"""