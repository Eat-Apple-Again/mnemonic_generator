import argparse
from address_generator.mnemonic_util import generate_mnemonic_24
from address_generator.mnemonic_self import self_generate_mnemonic_24

def main():
    p = argparse.ArgumentParser(description="Generate 24-word mnemonic.")
    p.add_argument("--mode", choices=["gen_auto", "gen_self"], required=True, help="gen_auto: Use bip-utils library; gen_self: Calculate by myself and only use 'hashlib' and 'secrets' libraries.")

    args = p.parse_args()

    if args.mode == "gen_auto":
        mnemonic = generate_mnemonic_24()
        print("Use Library bip-utils and pycardano to generate 24-word mnemonic.")
        print(f"[24 Mnemonic]:\n{mnemonic}\n")
    elif args.mode == "gen_self":
        mnemonic = self_generate_mnemonic_24()
        print(f"[24 Mnemonic]:\n{mnemonic}\n")
if __name__ == "__main__":
    main()

"""
uv run main.py --mode gen_self
"""