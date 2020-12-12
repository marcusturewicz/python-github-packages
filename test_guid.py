import guid

def test_not_empty():
    g = guid.new_guid()
    assert g is not None