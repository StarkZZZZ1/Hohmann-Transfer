import datetime
import pytest
import project as pro
import phy_functions as p
import task as t

def test_date_bad():
    with pytest.raises(pro.MyError):
        pro.date_validity("2026-5-6")
    with pytest.raises(pro.MyError):
        pro.date_validity("2026-apr-12")

def test_date_good():
    out = pro.date_validity("2026-05-05")
    assert out.groups() == ("2026", "05", "05")

def test_calc_window():
    year, month, day, hour = 2026, 4,23,10
    alt = 200
    target_alt = 50

    results = t.calculate_window(year, month, day, hour, alt, target_alt)

    assert 4.71 <= results["TOF"] <= 4.73
    assert 28.10 <= results["Inc"] <= 28.30
    assert results["target_alt"] == 50

def test_nextdate():
    year, month, day = 2026, 5, 5
    alt = 300
    target_alt = 100

    result,_ = t.next_date(year, month, day, alt, target_alt)

    assert result == datetime.datetime(2026, 5, 20, 18, 0)

def test_deltav():
    v1, v2 = 50, 100
    assert p.get_deltav(v1, v2, 0) == 50

def test_magnitude():
    vector = [3, 4, 0]
    assert p.magnitude(vector) == 5

def test_month():
    month = 5
    assert pro.month_valid(month) == 5
    month = 0
    with pytest.raises(pro.MyError):
        pro.month_valid(month)


def test_day():
    day = 5
    assert pro.month_valid(day) == 5
    month = "a"
    with pytest.raises(TypeError):
        pro.month_valid(month)

