import pytest

from hccpy.utils import read_dx2cc

AVAILABLE_MAPPING_FILES = {'22': 'F2218O1P.TXT', '23': 'F2318P1Q.TXT'}

@pytest.fixture(scope='module', params=AVAILABLE_MAPPING_FILES.values(),
                ids=['v{}_mapping'.format(key) for key in AVAILABLE_MAPPING_FILES.keys()])
def dx_mapping_fn(request):
    return 'data/{}'.format(request.param)

def test_valid_filename(dx_mapping_fn):
    mapping = read_dx2cc(dx_mapping_fn)
    assert isinstance(mapping, dict)
    assert len(mapping) > 0

def test_invalid_filename():
    fn = 'fake_dir/makeup_file.txt'
    with pytest.raises(FileNotFoundError):
        data = read_dx2cc(fn)

def test_mapping_content(dx_mapping_fn):
    mapping = read_dx2cc(dx_mapping_fn)
    assert mapping['E119'] == 'HCC19'
    assert mapping['E1165'] == 'HCC18'
    assert 'E11.9' not in mapping
    assert 'E11.65' not in mapping
