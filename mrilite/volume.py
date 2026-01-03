import numpy as np
import nibabel as nib
from dataclasses import dataclass

    
@dataclass
class MRIVolume:
    """Basic container for MRI volume and metadata."""
    data: np.ndarray
    affine: np.ndarray | None = None
    header: nib.Nifti1Header | None = None
    voxel_sizes: np.ndarray | None = None
    orientation: np.ndarray | None = None
    axcodes: str | None = None
    path: str | None = None
    shape: tuple | None = None

    def describe(self) -> dict:
        return {
            "shape"        : self.data.shape,
            "voxel_sizes"  : tuple(self.voxel_sizes.tolist()) if isinstance(self.voxel_sizes, np.ndarray) else self.voxel_sizes,
            "axcodes"      : self.axcodes,
            "intensity_min": float(np.nanmin(self.data)),
            "intensity_max": float(np.nanmax(self.data)),
        }