#!/usr/bin/env python3
"""
CTF Crypto Challenge Generator
Applies Caesar cipher (+7 shift) followed by Base64 encoding
"""

import base64


def caesar_shift(text, shift):
    """
    Apply Caesar cipher shift to alphabetical characters only.
    Preserves case and non-alphabetical characters.
    
    Args:
        text: Input string
        shift: Number of positions to shift (positive or negative)
    
    Returns:
        Caesar-shifted string
    """
    result = []
    
    for char in text:
        if char.isalpha():
            # Determine if uppercase or lowercase
            if char.isupper():
                # Shift within A-Z range
                shifted = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                # Shift within a-z range
                shifted = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result.append(shifted)
        else:
            # Preserve non-alphabetical characters (braces, underscore, etc.)
            result.append(char)
    
    return ''.join(result)


def generate_challenge(plaintext, shift):
    """
    Generate the CTF challenge by applying Caesar cipher and Base64 encoding.
    
    Args:
        plaintext: Original flag
        shift: Caesar shift amount
    
    Returns:
        tuple: (caesar_shifted_text, base64_ciphertext)
    """
    # Step 1: Apply Caesar cipher
    caesar_text = caesar_shift(plaintext, shift)
    
    # Step 2: Encode with Base64
    base64_bytes = base64.b64encode(caesar_text.encode('utf-8'))
    base64_text = base64_bytes.decode('utf-8')
    
    return caesar_text, base64_text


def verify_solution(base64_ciphertext, expected_plaintext, shift):
    """
    Verify the challenge by reversing the operations.
    
    Args:
        base64_ciphertext: Base64 encoded ciphertext
        expected_plaintext: Original flag to verify against
        shift: Caesar shift amount used in encryption
    
    Returns:
        bool: True if verification succeeds
    """
    try:
        # Step 1: Decode Base64
        decoded_bytes = base64.b64decode(base64_ciphertext)
        decoded_text = decoded_bytes.decode('utf-8')
        
        # Step 2: Reverse Caesar cipher (shift by negative amount)
        recovered_plaintext = caesar_shift(decoded_text, -shift)
        
        # Step 3: Verify
        is_correct = recovered_plaintext == expected_plaintext
        
        print("\n--- Verification ---")
        print(f"Base64 decoded: {decoded_text}")
        print(f"Caesar reversed: {recovered_plaintext}")
        print(f"Expected: {expected_plaintext}")
        print(f"Verification: {'✓ PASS' if is_correct else '✗ FAIL'}")
        
        return is_correct
    
    except Exception as e:
        print(f"Verification failed with error: {e}")
        return False


def main():
    # Challenge parameters
    ORIGINAL_FLAG = "HBT{psg_1024}"
    CAESAR_SHIFT = 7
    
    print("=== CTF Crypto Challenge Generator ===\n")
    print(f"Original Flag: {ORIGINAL_FLAG}")
    print(f"Caesar Shift: +{CAESAR_SHIFT}\n")
    
    # Generate challenge
    caesar_text, base64_ciphertext = generate_challenge(ORIGINAL_FLAG, CAESAR_SHIFT)
    
    print("--- Challenge Generation ---")
    print(f"After Caesar (+{CAESAR_SHIFT}): {caesar_text}")
    print(f"After Base64 encoding: {base64_ciphertext}")
    
    # Verify solution
    verify_solution(base64_ciphertext, ORIGINAL_FLAG, CAESAR_SHIFT)
    
    print("\n=== Challenge for Participants ===")
    print(f"Ciphertext: {base64_ciphertext}")
    print("\nHint: The flag has been encrypted with Caesar cipher and then Base64 encoded.")


if __name__ == "__main__":
    main()
