import pytest

from hccpy.hcc import HCCEngine

AVAILABLE_VERSIONS = ['22', '23']

def test_valid_version():
    # GIVEN multiple `version` strings: `AVAILABLE_VERSIONS`
    for version in AVAILABLE_VERSIONS:
        # WHEN instantiate `HCCEngine` with `version`
        he = HCCEngine(version)
        # THEN version of `he` must be `version`
        assert he.version == version

def test_invalid_version():
    # GIVEN a `version` as string
    version = '00'
    # WHEN instantiate `HCCEngine` with a version that is not supported
    # THEN a `KeyError` will be raised
    with pytest.raises(KeyError):
        he = HCCEngine(version)

@pytest.fixture(scope='module', params=AVAILABLE_VERSIONS,
                ids=['engine_v{}'.format(v) for v in AVAILABLE_VERSIONS])
def he(request):
    return HCCEngine(request.param)

def test_engine_attributes(he):
    # GIVEN an `HCCEngine` instance `he`
    # WHEN the instantiation is successful
    # THEN `he` should have the following attributes:
    #      `dx2cc`: dict, `coefn`: dict, `label`: dict, `hier`: dict
    assert hasattr(he, 'dx2cc')
    assert isinstance(he.dx2cc, dict)
    assert hasattr(he, 'coefn')
    assert isinstance(he.coefn, dict)
    assert hasattr(he, 'label')
    assert isinstance(he.label, dict)
    assert hasattr(he, 'hier')
    assert isinstance(he.hier, dict)

def test_engine_methods(he):
    # GIVEN an `HCCEngine` instance `he`
    # WHEN the instantiation is successful
    # THEN `he` should have the following methods:
    #      `profile`, `describe_hcc`
    assert hasattr(he, 'profile')
    assert callable(he.profile)
    assert hasattr(he, 'describe_hcc')
    assert callable(he.describe_hcc)
