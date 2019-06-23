import pytest

from hccpy.utils import read_coefn

AVAILABLE_COEF_FILES = {'22': 'V22hcccoefn.csv', '23': 'V23hcccoefn.csv'}

@pytest.fixture(scope='module', params=AVAILABLE_COEF_FILES.values(),
                ids=['v{}_coefn'.format(key) for key in AVAILABLE_COEF_FILES.keys()])
def coef_fn(request):
    return 'data/{}'.format(request.param)

def test_valid_filename(coef_fn):
    coef = read_coefn(coef_fn)
    assert isinstance(coef, dict)
    assert len(coef) > 0

def test_invalid_filename():
    fn = 'fake_dir/makeup_file.txt'
    with pytest.raises(FileNotFoundError):
        data = read_coefn(fn)

def test_coef_content(coef_fn):
    coef = read_coefn(coef_fn)
    assert isinstance(coef['CNA_HCC19'], float)
    assert isinstance(coef['INS_HCC19'], float)
    assert 'CNA_19' not in coef
    assert 'INS_19' not in coef
