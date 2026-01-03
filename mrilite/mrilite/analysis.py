import numpy as np
from scipy.ndimage import label, generate_binary_structure

def connected_components(mask: np.ndarray):
    mask_bin = (mask > 0).astype(np.uint8)
    struct = generate_binary_structure(3, 3)  # 26-connect
    labeled, n = label(mask_bin, structure=struct)
    return labeled, n