from PIL import Image
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64


def extract_message(image_path):
    """
    Extract the hidden binary message from the least significant bits (LSBs) of the image.
    """
    img = Image.open(image_path).convert("RGB")
    pixels = img.load()
    binary_msg = ""

    for y in range(img.height):
        for x in range(img.width):
            r, g, b = pixels[x, y]
            binary_msg += str(r & 1)  # Extract LSB from Red channel

    # Convert binary to text and stop at EOF marker
    binary_msg = [binary_msg[i : i + 8] for i in range(0, len(binary_msg), 8)]
    message = ""
    for char in binary_msg:
        if char == "11111110":  # EOF marker
            break
        try:
            decoded_char = chr(int(char, 2))
            message += decoded_char
        except ValueError:
            print(f"Skipping invalid binary sequence: {char}")
    return message


def decrypt_message(ciphertext, key):
    """
    Decrypt the ciphertext using AES (ECB mode) and the provided key.
    """
    try:
        # Decode base64
        decoded_ciphertext = base64.b64decode(ciphertext)
        cipher = AES.new(key, AES.MODE_ECB)
        decrypted_flag = unpad(cipher.decrypt(decoded_ciphertext), 16)
        return decrypted_flag.decode()
    except Exception as e:
        print(f"Error during decryption: {e}")
        return None


if __name__ == "__main__":
    # Step 1: Extract the hidden message
    challenge_image_path = "challenge_image.png"
    ciphertext = extract_message(challenge_image_path)
    print(f"Extracted Ciphertext: {ciphertext}")

    # Step 2: Decrypt the message
    decryption_key = b"mysecretkey12345"
    flag = decrypt_message(ciphertext, decryption_key)
    if flag:
        print(f"Decrypted Flag: {flag}")
    else:
        print(
            "Failed to decrypt the message. Ensure the extracted ciphertext is correct."
        )
