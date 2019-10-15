import analysis

def test_average():
    avg = analysis.average_inflammations(0)
    assert(avg == 5.45)