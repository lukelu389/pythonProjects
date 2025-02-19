from PIL import Image, ImageEnhance, ImageOps

# Load the original image
original_image = Image.open("./imagepath").convert("RGB")

# Step 1: Enhance contrast more
contrast_enhancer = ImageEnhance.Contrast(original_image)
enhanced_contrast_image = contrast_enhancer.enhance(2.0)  # Stronger contrast boost

# Step 2: Slightly increase brightness
brightness_enhancer = ImageEnhance.Brightness(enhanced_contrast_image)
brightened_image = brightness_enhancer.enhance(1.6)  # Increase brightness more

# Step 3: Optional - Apply gamma correction to bring out details in shadows
def apply_gamma(image, gamma):
    # Gamma correction to boost darker areas
    gamma_correction = ImageOps.autocontrast(image)
    return ImageEnhance.Brightness(gamma_correction).enhance(gamma)

final_image = apply_gamma(brightened_image, 1.2)  # Adjust gamma factor as needed

# Save and show the final image
final_image.save("image")
final_image.show()
