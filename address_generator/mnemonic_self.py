import hashlib
import secrets

# Load English wordlist(2048 words)
# https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt
word_list_path = "word_list/english.txt"
with open(word_list_path, "r", encoding="utf-8") as word_list:
    words = [w.strip() for w in word_list]

""" Generate a 24-word mnemonic (256-bit entropy -> 24x11-bit indices). """
def self_generate_mnemonic_24() -> str:
    # Generate entropy randomly by using secrets library. Entropy length is 32 bytes.
    entropy = secrets.token_bytes(32)

    # Convert into string (padding with leading zeros) and total is 256 bits.
    # :08b is mean to format each byte as an 8-bit binary string with leading zeros and it is still binary format.
    entropy_bits = "".join(f"{b:08b}" for b in entropy)
    
    # Apply SHA-256 to entropy by using hashlib library and take the first 8 bits as checksum_bits.    
    checksum_bits = f"{hashlib.sha256(entropy).digest()[0]:08b}"
                                                                
    # Combine entropy(256 bits) and checksum(8 bits) to get 264 bits.
    final_bits = entropy_bits + checksum_bits

    # Split into 24 chunks of 11 bits each; Each chunk maps to a word.
    # The word_list/english.txt has 2048 words(2^11), so each chunk's value is the index in the word list.
    numbers = [int(final_bits[i:i+11], 2) for i in range(0, 264, 11)]

    # Map to words according to wordlist.
    mnemonics = " ".join(words[i] for i in numbers)
    return mnemonics
