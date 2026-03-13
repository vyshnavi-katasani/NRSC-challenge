import numpy as np
import matplotlib.pyplot as plt
import rasterio

# === Load the bands ===
with rasterio.open("/home/vyshnavi/silver_clouds/R2F09MAY2024067746010000063SSANSTUC00GTDB/BH_R2F09MAY2024067746010000063SSANSTUC00GTDB/BAND2.tif") as b2:
    band2 = b2.read(1)
with rasterio.open("/home/vyshnavi/silver_clouds/R2F09MAY2024067746010000063SSANSTUC00GTDB/BH_R2F09MAY2024067746010000063SSANSTUC00GTDB/BAND3.tif") as b3:
    band3 = b3.read(1)
with rasterio.open("/home/vyshnavi/silver_clouds/R2F09MAY2024067746010000063SSANSTUC00GTDB/BH_R2F09MAY2024067746010000063SSANSTUC00GTDB/BAND4.tif") as b4:
    band4 = b4.read(1)

# === Crop image (move slightly left and down) ===
x, y = 6000, 8000  # Adjusted for new crop
width, height = 1000, 1000
band2_crop = band2[y:y+height, x:x+width]
band3_crop = band3[y:y+height, x:x+width]
band4_crop = band4[y:y+height, x:x+width]

# === Normalize bands for display (0–255) ===
def normalize(band):
    band = band.astype(np.float32)
    norm = (band - band.min()) / (band.max() - band.min())
    return (norm * 255).astype(np.uint8)

norm_b2 = normalize(band2_crop)
norm_b3 = normalize(band3_crop)
norm_b4 = normalize(band4_crop)

# === Create false color composite (R=Band4, G=Band3, B=Band2) ===
false_color_img = np.stack((norm_b4, norm_b3, norm_b2), axis=-1)

# === Classification ===
classification = np.zeros_like(norm_b2)

# --- Thresholds ---
CLOUD_B2 = 200
CLOUD_B3 = 200
CLOUD_B4 = 180

SHADOW_B2 = 60
SHADOW_B3 = 60
SHADOW_B4 = 40

WATER_THRESHOLD = 70

# --- Masks ---
cloud_mask = (
    (norm_b2 > CLOUD_B2) &
    (norm_b3 > CLOUD_B3) &
    (norm_b4 > CLOUD_B4)
)

shadow_mask = (
    (norm_b2 < SHADOW_B2) &
    (norm_b3 < SHADOW_B3) &
    (norm_b4 < SHADOW_B4) &
    (norm_b3 < norm_b2 + 10)  # helps exclude terrain shadows
)

water_mask = (
    (norm_b4 < WATER_THRESHOLD) &
    (norm_b3 < WATER_THRESHOLD) &
    (norm_b2 < WATER_THRESHOLD) &
    (np.abs(norm_b4 - norm_b3) <= 10)
)

classification[cloud_mask] = 1
classification[shadow_mask] = 2
classification[water_mask] = 3

# === Display side-by-side ===
plt.figure(figsize=(12, 6))

# Original false color
plt.subplot(1, 2, 1)
plt.imshow(false_color_img)
plt.title("Original False Color Composite")
plt.axis('off')

# Classification (color-coded)
classification_rgb = np.zeros((*classification.shape, 3), dtype=np.uint8)
classification_rgb[classification == 1] = [255, 255, 255]  # white for clouds
classification_rgb[classification == 2] = [0, 0, 255]      # blue for shadows
classification_rgb[classification == 3] = [0, 255, 255]    # cyan for water

plt.subplot(1, 2, 2)
plt.imshow(classification_rgb)
plt.title("Rule-Based Classification")
plt.axis('off')

plt.tight_layout()
plt.show()

