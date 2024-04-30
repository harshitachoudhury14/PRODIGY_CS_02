from PIL import Image

def encrypt_image(image_path, key):
    try:
        img = Image.open(image_path)
        width, height = img.size
        pixels = img.load()

        encrypted_pixels = []
        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]
                r = (r + key) % 256
                g = (g + key) % 256
                b = (b + key) % 256
                encrypted_pixels.append((r, g, b))

        encrypted_img = Image.new(img.mode, img.size)
        encrypted_img.putdata(encrypted_pixels)
        encrypted_img.save("encrypted_image.png")
        print("Image encrypted successfully.")
    except Exception as e:
        print("Error:", e)

def decrypt_image(image_path, key):
    try:
        img = Image.open(image_path)
        width, height = img.size
        pixels = img.load()

        decrypted_pixels = []
        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]
                r = (r - key) % 256
                g = (g - key) % 256
                b = (b - key) % 256
                decrypted_pixels.append((r, g, b))

        decrypted_img = Image.new(img.mode, img.size)
        decrypted_img.putdata(decrypted_pixels)
        decrypted_img.save("decrypted_image.png")
        print("Image decrypted successfully.")
    except Exception as e:
        print("Error:", e)

# Take user input
image_path = input("Enter the path of the image file: ")
encryption_key = int(input("Enter the encryption key (an integer): "))

encrypt_image(image_path, encryption_key)
decrypt_image("encrypted_image.png", encryption_key)
