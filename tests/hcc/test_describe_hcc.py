def test_description_of_valid_cc(he):
    cc = 'HCC19'
    output = he.describe_hcc(cc)
    assert output['description'] == 'Diabetes without Complication'

    cc = 'HCC18'
    output = he.describe_hcc(cc)
    assert output['description'] == 'Diabetes with Chronic Complications'

    cc = 'HCC17'
    output = he.describe_hcc(cc)
    assert output['description'] == 'Diabetes with Acute Complications'

def test_parents_of_valid_cc(he):
    cc = 'HCC19'
    output = he.describe_hcc(cc)
    assert output['parents'] == ['HCC17', 'HCC18']

    cc = 'HCC18'
    output = he.describe_hcc(cc)
    assert output['parents'] == ['HCC17']

    cc = 'HCC17'
    output = he.describe_hcc(cc)
    assert output['parents'] == []

def test_children_of_valid_cc(he):
    cc = 'HCC19'
    output = he.describe_hcc(cc)
    assert output['children'] == []

    cc = 'HCC18'
    output = he.describe_hcc(cc)
    assert output['children'] == ['HCC19']

    cc = 'HCC17'
    output = he.describe_hcc(cc)
    assert output['children'] == ['HCC18', 'HCC19']

def test_invalid_cc(he):
    cc = 'HCCfake'
    output = he.describe_hcc(cc)
    assert output['description'] == 'N/A'
    assert output['parents'] == []
    assert output['children'] == []

def test_various_input_format(he):
    for cc in ['19', 'HCC19', 'hcc19']:
        output = he.describe_hcc(cc)
        assert output['description'] == 'Diabetes without Complication'
        assert output['parents'] == ['HCC17', 'HCC18']
        assert output['children'] == []
