from PIL import Image

# Open the image and convert to RGBA
img = Image.open('images/logo.png').convert('RGBA')
width, height = img.size

# Background color observed: (24, 33, 109)
# We will use the Red channel (24) to estimate the alpha since white text has Red=255.
bg_r = 24
# Create a new image for the output
out = Image.new('RGBA', img.size)
out_pixels = out.load()
in_pixels = img.load()

for y in range(height):
    for x in range(width):
        r, g, b, a = in_pixels[x, y]
        
        # Calculate alpha based on how far R is from the background R
        # This will perfectly preserve anti-aliased edges of white text!
        alpha = int(max(0, min(255, (r - bg_r) * 255 / (255 - bg_r))))
        
        # Output pure white text, with the calculated alpha
        out_pixels[x, y] = (255, 255, 255, alpha)

# Overwrite the logo
out.save('images/logo.png')
print("Background removed from logo.png!")
