import pytest

from hccpy.utils import read_hier

AVAILABLE_HIER_FILES = {'22': 'V22H79H1.TXT', '23': 'V23H83H1.TXT'}

@pytest.fixture(scope='module', params=AVAILABLE_HIER_FILES.values(),
                ids=['v{}_hier'.format(key) for key in AVAILABLE_HIER_FILES.keys()])
def cc_hier_fn(request):
    return 'data/{}'.format(request.param)

def test_valid_filename(cc_hier_fn):
    hier = read_hier(cc_hier_fn)
    assert isinstance(hier, dict)
    assert len(hier) > 0

def test_invalid_filename():
    fn = 'fake_dir/makeup_file.txt'
    with pytest.raises(FileNotFoundError):
        data = read_hier(fn)

def test_cc_hier_structure(cc_hier_fn):
    hier = read_hier(cc_hier_fn)
    assert hier['HCC17'] == ['HCC18', 'HCC19']
    assert hier['HCC18'] == ['HCC19']
    assert 'HCC19' not in hier
    assert '19' not in hier
