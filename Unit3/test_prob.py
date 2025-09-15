import math,prob
def test_n_choose_one():
    #setup
    x=5
    expected = 1/5
    #invoke
    actual = prob.n_choose_one(x)
    #analyze
    assert math.isclose(actual,expected)
def test_same_m_times():
    #setup
    x=2
    y=3
    expected = 1/2 ** 3
    #invoke
    actual = prob.choose_same_m_times(2,3)
    #analyze
    assert math.isclose(actual,expected)
def test_number_of_draws_for_probability():
    #setup
    x = 10
    y = 0.8
    expected = 16
    #invoke
    actual = prob.number_of_draws_for_probability(x,y)
    #analyze
    assert math.isclose(actual,expected)