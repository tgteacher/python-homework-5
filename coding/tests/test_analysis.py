import analysis

def test_average():
    avg = analysis.average_inflammations(0)
    assert(avg == 5.45)

def test_max():
    m = analysis.max_inflammations(3)
    assert(m == 17)

def test_acute_patient():
    p = analysis.acute_patient()
    assert( p == 46)