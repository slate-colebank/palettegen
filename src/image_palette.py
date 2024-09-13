import sys
import numpy as np
from PIL import Image
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def load_image(image_path):
    # Loads the image for processing
    img = Image.open(image_path)
    img = img.resize((256,256))
    img_array = np.array(img)
    return img_array

def process_image(img_array):
    # Creates an array of RGB values from the image
    pixels = img_array.reshape((-1, 3))
    return pixels

def find_colors(pixels, palette_size):
    # Use KMeans to find the color palette
    kmeans = KMeans(n_clusters = palette_size, n_init = 'auto')
    kmeans.fit(pixels)
    colors = kmeans.cluster_centers_.astype(int)
    return colors

def display_palette(colors, save_path):
    # display the completed palette
    fig, ax = plt.subplots(figsize=(4, 2))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    for i, color in enumerate(colors):
        row = i // 4
        col = i % 4
        ax.add_patch(plt.Rectangle((col/4, 1-row/2-0.5), 0.25, 0.5, fc=color/255, ec='none'))

    plt.subplots_adjust(left=0, right=1, top=1, bottom=0, wspace=0, hspace=0)
    plt.savefig(save_path, dpi=300, bbox_inches='tight', pad_inches=0)
    plt.close(fig)
    
    print(f"Color palette saved as {save_path}")

def gen_palette(image_name, image_path):
    img_array = load_image(image_path)
    pixels = process_image(img_array)
    colors = find_colors(pixels, 8)
    save_path = "../palettes/" + image_name + "_palette.png"
    display_palette(colors, save_path)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python image_palette.py <image filename>")
        sys.exit(1)

    image_name = sys.argv[1]
    image_path = "../images/" + image_name

    gen_palette(image_name, image_path)


