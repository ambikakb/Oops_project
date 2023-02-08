import pytest
import NA
def test_login():
    expected='Ambika'
    assert NA.login()==expected


if __name__ == '__main__':
    pytest.main()
