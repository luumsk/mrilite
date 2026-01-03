import numpy as np
import nibabel as nib

from mrilite.io import load_nifti, save_nifti
from mrilite.volume import MRIVolume


def test_load_nifti(tmp_path):
    """Test loading a NIfTI file into MRIVolume."""
    # Create synthetic data
    data = np.random.rand(10, 10, 10).astype(np.float32)
    affine = np.eye(4)

    img = nib.Nifti1Image(data, affine)
    nifti_path = tmp_path / "test.nii.gz"
    nib.save(img, nifti_path)

    volume = load_nifti(str(nifti_path))

    assert isinstance(volume, MRIVolume)
    assert volume.data.shape == data.shape
    assert volume.data.dtype == np.float32
    assert np.allclose(volume.affine, affine)
    assert volume.path == str(nifti_path)


def test_save_nifti(tmp_path):
    """Test saving an MRIVolume to a NIfTI file."""
    data = np.ones((8, 8, 8), dtype=np.float32)
    affine = np.eye(4)

    volume = MRIVolume(
        data=data,
        affine=affine,
        header=None,
        voxel_sizes=np.array([1.0, 1.0, 1.0]),
        orientation=None,
        axcodes=None,
        path=None,
    )

    output_path = tmp_path / "output.nii.gz"
    save_nifti(volume, str(output_path))

    assert output_path.exists()

    img = nib.load(str(output_path))
    loaded_data = img.get_fdata(dtype=np.float32)

    assert loaded_data.shape == data.shape
    assert np.allclose(loaded_data, data)
    assert np.allclose(img.affine, affine)