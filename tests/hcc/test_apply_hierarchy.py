def test_neoplasm_family(he):
    cc_list = ['HCC9', 'HCC10', 'HCC11', 'HCC12']
    clean_cc_list = he._apply_hierarchy(cc_list)
    assert clean_cc_list == ['HCC9']

def test_diabetes_family(he):
    cc_list = ['HCC17', 'HCC18', 'HCC19']
    clean_cc_list = he._apply_hierarchy(cc_list)
    assert clean_cc_list == ['HCC17']

def test_liver_family(he):
    cc_list = ['HCC27', 'HCC28', 'HCC29', 'HCC80']
    clean_cc_list = he._apply_hierarchy(cc_list)
    assert clean_cc_list == ['HCC27']

def test_blood_family(he):
    cc_list = ['HCC46', 'HCC48']
    clean_cc_list = he._apply_hierarchy(cc_list)
    assert clean_cc_list == ['HCC46']

def test_sa_family(he):
    cc_list = ['HCC54', 'HCC55']
    if he.version == '23':
        cc_list.append('HCC56')
    clean_cc_list = he._apply_hierarchy(cc_list)
    assert clean_cc_list == ['HCC54']

def test_psychiatric_family(he):
    cc_list = ['HCC57', 'HCC58']
    if he.version == '23':
        cc_list.extend(['HCC59', 'HCC60'])
    clean_cc_list = he._apply_hierarchy(cc_list)
    assert clean_cc_list == ['HCC57']

def test_spinal_family(he):
    cc_list = ['HCC70', 'HCC71', 'HCC72', 'HCC103', 'HCC104', 'HCC169']
    clean_cc_list = he._apply_hierarchy(cc_list)
    assert clean_cc_list == ['HCC70']

def test_arrest_family(he):
    cc_list = ['HCC82', 'HCC83', 'HCC84']
    clean_cc_list = he._apply_hierarchy(cc_list)
    assert clean_cc_list == ['HCC82']

def test_heart_family(he):
    cc_list = ['HCC86', 'HCC87', 'HCC88']
    clean_cc_list = he._apply_hierarchy(cc_list)
    assert clean_cc_list == ['HCC86']

def test_cvd_family(he):
    cc_list = ['HCC99', 'HCC100']
    clean_cc_list = he._apply_hierarchy(cc_list)
    assert clean_cc_list == ['HCC99']

    cc_list = ['HCC103', 'HCC104']
    clean_cc_list = he._apply_hierarchy(cc_list)
    assert clean_cc_list == ['HCC103']

def test_vascular_family(he):
    cc_list = ['HCC106', 'HCC107', 'HCC108', 'HCC161', 'HCC189']
    clean_cc_list = he._apply_hierarchy(cc_list)
    assert clean_cc_list == ['HCC106']

def test_lung_family(he):
    cc_list = ['HCC110', 'HCC111', 'HCC112']
    clean_cc_list = he._apply_hierarchy(cc_list)
    assert clean_cc_list == ['HCC110']

    cc_list = ['HCC114', 'HCC115']
    clean_cc_list = he._apply_hierarchy(cc_list)
    assert clean_cc_list == ['HCC114']

def test_kidney_family(he):
    cc_list = ['HCC134', 'HCC135', 'HCC136', 'HCC137']
    if he.version == '23':
        cc_list.append('HCC138')
    clean_cc_list = he._apply_hierarchy(cc_list)
    assert clean_cc_list == ['HCC134']

def test_skin_family(he):
    cc_list = ['HCC157', 'HCC158', 'HCC161']
    clean_cc_list = he._apply_hierarchy(cc_list)
    assert clean_cc_list == ['HCC157']

def test_injury_family(he):
    cc_list = ['HCC166', 'HCC80', 'HCC167']
    clean_cc_list = he._apply_hierarchy(cc_list)
    assert clean_cc_list == ['HCC166']
