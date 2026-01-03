import numpy as np

from mrilite.preprocess import zscore
from mrilite.volume import MRIVolume


def test_zscore_normalization_basic():
    """Z-score normalization should produce zero mean and unit variance."""
    data = np.array(
        [
            [[1.0, 2.0], [3.0, 4.0]],
            [[5.0, 6.0], [7.0, 8.0]],
        ],
        dtype=np.float32,
    )

    volume = MRIVolume(
        data=data,
        affine=np.eye(4),
        header=None,
        voxel_sizes=np.array([1.0, 1.0, 1.0]),
        orientation=None,
        axcodes=None,
        path=None,
    )

    norm_volume = zscore(volume)
    norm_data = norm_volume.data

    mean = norm_data.mean()
    std = norm_data.std()

    assert np.isclose(mean, 0.0, atol=1e-6)
    assert np.isclose(std, 1.0, atol=1e-6)


def test_zscore_preserves_metadata():
    """Z-score normalization should not change spatial metadata."""
    data = np.random.rand(5, 5, 5).astype(np.float32)

    volume = MRIVolume(
        data=data,
        affine=np.eye(4),
        header="dummy_header",
        voxel_sizes=np.array([2.0, 2.0, 2.0]),
        orientation="RAS",
        axcodes=("R", "A", "S"),
        path="dummy_path",
    )

    norm_volume = zscore(volume)

    assert np.allclose(norm_volume.affine, volume.affine)
    assert norm_volume.header == volume.header
    assert np.allclose(norm_volume.voxel_sizes, volume.voxel_sizes)
    assert norm_volume.orientation == volume.orientation
    assert norm_volume.axcodes == volume.axcodes
    assert norm_volume.path == volume.path


def test_zscore_handles_constant_input():
    """Z-score should not produce NaNs for constant input."""
    data = np.ones((4, 4, 4), dtype=np.float32)

    volume = MRIVolume(
        data=data,
        affine=np.eye(4),
        header=None,
        voxel_sizes=np.array([1.0, 1.0, 1.0]),
        orientation=None,
        axcodes=None,
        path=None,
    )

    norm_volume = zscore(volume)

    assert np.all(np.isfinite(norm_volume.data))
    assert np.allclose(norm_volume.data, 0.0)