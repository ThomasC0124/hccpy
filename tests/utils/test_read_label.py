import pytest

from hccpy.utils import read_label

AVAILABLE_LABEL_FILES = {'22': 'V22H79L1.TXT', '23': 'V23H83L2.TXT'}

@pytest.fixture(scope='module', params=AVAILABLE_LABEL_FILES.values(),
                ids=['v{}_label'.format(key) for key in AVAILABLE_LABEL_FILES.keys()])
def cc_label_fn(request):
    return 'data/{}'.format(request.param)

def test_valid_filename(cc_label_fn):
    label = read_label(cc_label_fn)
    assert isinstance(label, dict)
    assert len(label) > 0

def test_invalid_filename():
    fn = 'fake_dir/makeup_file.txt'
    with pytest.raises(FileNotFoundError):
        data = read_label(fn)

def test_cc_label_content(cc_label_fn):
    label = read_label(cc_label_fn)
    assert label['19'] == 'Diabetes without Complication'
    assert label['85'] == 'Congestive Heart Failure'
    assert 'HCC19' not in label
    assert 'HCC85' not in label
