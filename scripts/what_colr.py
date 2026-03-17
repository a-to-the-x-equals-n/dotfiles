from PIL import Image

# Open the image file
image_path = "c.png"
image = Image.open(image_path)

# Get the most common color (assuming solid color background)
most_common_color = image.convert("RGB").getpixel((0, 0))

# Convert RGB to hex
hex_color = "#{:02X}{:02X}{:02X}".format(*most_common_color)
print(hex_color)



# from PIL import Image

# # Open the image file
# image_path = "c.png"
# image = Image.open(image_path).convert("RGB")



# # ----------------------------------------------
# # Collect UNIQUE COLORS ONLY
# # ----------------------------------------------
# width, height = image.size
# hx = set()

# for y in range(height):
#     for x in range(width):
#         r, g, b = image.getpixel((x, y))
#         hx.add("#{0:02X}{1:02X}{2:02X}".format(r, g, b))

# # ----------------------------------------------
# # Write unique colors to pixels.md
# # ----------------------------------------------
# with open("pixels.md", "w", encoding="utf-8") as f:
#     f.write("# Unique Hex Colors\n\n")
#     for hx in sorted(hx):
#         f.write(hx + "\n")

# print("Hex colors written to pixels.md")
