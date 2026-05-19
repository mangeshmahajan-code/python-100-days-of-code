import random
import string


def generate_random_chars(length=3):
    """Generate random alphabetic characters."""
    return ''.join(random.choices(string.ascii_letters, k=length))


def encode_word(word):
    """Encode a single word."""
    if len(word) >= 3:
        prefix = generate_random_chars()
        suffix = generate_random_chars()

        # Move first letter to the end
        return prefix + word[1:] + word[0] + suffix

    elif len(word) == 2:
        # Swap letters
        return word[::-1]

    return word


def decode_word(word):
    """Decode a single word."""
    if len(word) >= 9:
        # Remove random chars and restore first letter
        core = word[3:-3]
        return core[-1] + core[:-1]

    elif len(word) == 2:
        # Swap back
        return word[::-1]

    return word


def encode_message(message):
    words = message.split()
    return " ".join(encode_word(word) for word in words)


def decode_message(message):
    words = message.split()
    return " ".join(decode_word(word) for word in words)


def main():
    message = input("Enter message: ")

    choice = input("Enter 1 for encode and 0 for decode: ")

    if choice == "1":
        result = encode_message(message)
        print("\nEncoded message:")
        print(result)

    elif choice == "0":
        result = decode_message(message)
        print("\nDecoded message:")
        print(result)

    else:
        print("Invalid choice. Please enter 1 or 0.")


if __name__ == "__main__":
    main()
