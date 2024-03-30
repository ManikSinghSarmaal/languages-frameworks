from sklearn.preprocessing import LabelEncoder
import numpy as np
import matplotlib.pyplot as plt
from skimage import io, color, transform
from sklearn.cluster import MeanShift
from joblib import Parallel, delayed

# Load the image
image = io.imread('/Users/maniksinghsarmaal/Downloads/Non-Eutectic/000072.jpg')  # Replace 'your_image.jpg' with the path to your image

# Convert the image to grayscale
gray_image = image  # No need to convert if the image is already grayscale
image_len = image.shape[0]
image_width = image.shape[1]

# Proportionally resize the image to (250, 200)
scaled_image = transform.resize(gray_image, (int(image_len*0.69), int(image_width*0.69)), anti_aliasing=True)

# Flatten the scaled grayscale image to get pixel values
pixel_values = scaled_image.flatten().reshape(-1, 1)

# Adjust the bandwidth parameter for Mean Shift
bandwidth = 0.1  # Adjust this parameter to optimize performance and accuracy

# Perform Mean Shift clustering with parallelization
ms = MeanShift(bandwidth=bandwidth, n_jobs=-1)  # Utilize all available CPU cores
ms.fit(pixel_values)

# Retrieve cluster labels and cluster centers
labels = ms.labels_
cluster_centers = ms.cluster_centers_

# Determine the number of clusters
n_clusters_ = len(np.unique(labels))
print("Estimated number of clusters:", n_clusters_)

# Reshape labels to match the shape of the original image
labels_image = labels.reshape(scaled_image.shape)

# Create masks for each cluster
masks = Parallel(n_jobs=-1)(delayed(lambda label: labels_image == label)(label) for label in range(n_clusters_))

# Calculate area fraction for each cluster group
total_pixels = scaled_image.size
area_fractions = []
for label in range(n_clusters_):
    cluster_pixels = np.sum(labels_image == label)
    area_fraction = cluster_pixels / total_pixels
    area_fractions.append(area_fraction)
    print(f"Cluster {label}: Area Fraction = {area_fraction:.4f}")

# Generate unique colors for each cluster
unique_colors = plt.cm.nipy_spectral(labels / n_clusters_)

# Display original image and masks for each cluster
plt.figure(figsize=(12, 6))

plt.subplot(1, n_clusters_ + 1, 1)
plt.imshow(scaled_image, cmap='gray')
plt.title('Resized Image (250x200)')
plt.axis('off')

for i, mask in enumerate(masks):
    plt.subplot(1, n_clusters_ + 1, i + 2)
    plt.imshow(mask, cmap='gray')
    plt.title(f'Cluster {i + 1}')
    plt.axis('off')

plt.tight_layout()
plt.show()
