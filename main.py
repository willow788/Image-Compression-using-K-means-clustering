import cv2
import numpy as np

import matplotlib.pyplot as plt


#1st function
def read_image():

    #laoding the img
    image = cv2.imread('mr_turtle.jpg')

    #coverting bgr to rgb
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    #then dividing the image by 255 to get the values between 0 and 1, as in normalization
    image = image / 255.0

    return image

def initialize_means(image, clusters):
    #reshaping the img a 2d array of pixels
    points = image.reshape((-1, image.shape[2]))
    m, n = points.shape

    means = np.zeros((clusters, n)) #init an arrray of zeros for storing the means


    #initializing the mean randomly
    for i in range(clusters):
        #taking random indices to inintialize the means
        random_indices  = np.random.choice(m, size=10, replace=False) 

        means[i] = np.mean(points[random_indices], axis=0)

    return means, points

def euclidean_dist(x1, x2, y1, y2):
    val = np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return val

#definnig the main algo
def k_means(points, means, clusters):
    max_iterations = 10
    m,n = points.shape

    #index values is the array that is used to store the clusters index no. to a 
    #corresponding pixel
    index_values = np.zeros(m, dtype=int)

    for iteration in range(max_iterations):
        distances = np.linalg.norm(points[:, np.newaxis] - means[np.newaxis, :], axis=2)
        new_index_values = np.argmin(distances, axis=1)

        if np.array_equal(new_index_values, index_values):
            break

        index_values = new_index_values

        for k in range(clusters):
            cluster_points = points[index_values == k]
            if len(cluster_points) > 0:
                means[k] = np.mean(cluster_points, axis=0)

    return means, index_values


def compress_image(means, index_values, image):
    centroid = np.array(means)
    recovered = centroid[index_values.astype(int)]

    recovered = recovered.reshape(image.shape)

    #plotting the original and recovered image side by side
    fig, axes = plt.subplots(1, 2, squeeze=True, figsize=(12, 6))
    axes[0].imshow(image)
    axes[0].set_title('Original Image')
    axes[0].axis('off')

    axes[1].imshow(np.clip(recovered, 0, 1))
    axes[1].set_title('Compressed Image')
    axes[1].axis('off')

    fig.tight_layout()
    fig.savefig('compressed_image_preview.png', bbox_inches='tight')
    plt.show(block=True)

    #saving the recovered image
    plt.imsave('compressed_image.jpg', np.clip(recovered, 0, 1))


#driver code

if __name__ == "__main__":
    img = read_image()

    clusters = 10  # Number of clusters for k-means

    clusters = int(input("Enter the number of clusters: "))

    means, points = initialize_means(img, clusters)
    means, index_values = k_means(points, means, clusters)
    compress_image(means, index_values, img)

    size_of_image = img.shape[0] * img.shape[1] * img.shape[2]
    print("Size of the original image: ", size_of_image)
    compressed_size = clusters * img.shape[2] + points.shape[0]
    print("Size of the compressed image: ", compressed_size)

    #plotting a matric table to show the size of the original and compressed image
    plt.figure(figsize=(6, 4))
    plt.axis('off')
    plt.table(cellText=[["Original Image", size_of_image], ["Compressed Image", compressed_size]],
              colLabels=["Image Type", "Size (in bytes)"],
              cellLoc='center', loc='center')
    plt.show()
    
    


    
    