# Mnemonic Generator

All policies follow [BIP-39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki).

## Purpose

Generate BIP-39 mnemonics with two modes:  
- **`gen_self`**: a self-implemented flow using Python standard libraries (`secrets`, `hashlib`).  
- **`gen_auto`**: uses the `bip_utils` library for convenience.  

The goal is to enable fully offline mnemonic generation using `gen_self`.

## Quick Start

Make sure you have [`uv`](https://docs.astral.sh/uv/getting-started/installation/) installed, then choose one of the commands below.  
The `uv run` command will install all dependencies automatically.

```bash
uv run main.py --mode gen_self
```
```bash
uv run main.py --mode gen_auto
```