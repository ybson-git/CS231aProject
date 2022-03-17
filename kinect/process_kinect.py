from matplotlib import pyplot as plt
import os
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

IMG_FOLDERS = [
    "kinect_mirror",
    "kinect_mirror2",
    "kinect_mirror2_close",
    "kinect_mirror3",
    "kinect_mirror4",
    "kinect_sofa",
    "kinect_tv",
]

for folder in IMG_FOLDERS:
    base_path = os.path.join(os.getcwd(), folder)
    # Load RGB image
    rgb_path = os.path.join(base_path, "color_00.png")
    rgb = mpimg.imread(rgb_path)

    # Load Depth image
    dep_path = os.path.join(base_path, "depth_aligned_00.npy")
    dep = np.load(dep_path)

    # Plot
    f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
    ax1.imshow(rgb)
    ax1.set_title("RBG image")
    ax2.imshow(dep)
    ax2.set_title("Depth image")
    f.suptitle(folder, fontsize=20)
    plt.tight_layout()
    plt.show()
