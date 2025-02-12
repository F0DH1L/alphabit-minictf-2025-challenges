from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from Crypto.Cipher import AES

def extract_lsb_blue(image_path):
    img = Image.open(image_path)
    img_array = np.array(img)
    
    if len(img_array.shape) < 3 or img_array.shape[2] < 3:
        raise ValueError("The image is not in RGB format or does not have a Blue channel.")
    
    # Extract LSB from the Blue channel
    print("Extracting LSB from the Blue channel.")
    # print(img_array)
    lsb_array = img_array[:, :, 0] & 1  # Extracting LSB of the Blue channel
    binary_data = ''
    for row in lsb_array:
        # print(row[-1])
        binary_data += str(row[-1])
        print('----')
    # print(binary_data)
    # binary_data = '0101001101100101011000110100000101001001011110110110001100110100011101000110001101101000010111110110110100110011010111110011000101100110010111110111100100110000011101010101111101100011010000010110111001111101'
    return ''.join(hex(int(binary_data[i:i+8], 2))[2:] for i in range(0, len(binary_data), 8))
    
if __name__ == "__main__":
    image_path = "challenge_image.png"  # Replace with the path to your image
    ct = extract_lsb_blue(image_path)
    print(ct)
    key = b'secretsenhadji31'
    cipher = AES.new(key, AES.MODE_ECB)
    pt = cipher.decrypt(bytes.fromhex(ct))
