import Session4aProblems,random
seed = random.seed(1)

def test_solveThis():
    expected = None
    actual = Session4aProblems.solveThis()
    assert expected == actual

def test_SolveThis2():
    expected = ""
    actual = Session4aProblems.solveThis()
    assert expected != actual

def test_solveThat():
    x= 2
    y= 4
    expected = 18
    actual = Session4aProblems.solveThat(x,y)
    assert expected == actual

def test_howSolve():
    x = random.randint(2,5)
    expected = x * x * 2
    actual = Session4aProblems.howSolve(x)
    assert expected == actual



"""
def test_funcOne():
    #setup
    x = 5
    z = 2
    #invoke
    expected = Math.pow(x,z) + -x*z 
    actual = func.fOne(x,z)
    #analyze
    assert expected == actual

def test_funcTwo():
    #setup
    name = "Bob"
    addr = "Rochester, NY"
    #invoke
    expected = "Bob lives in Rochester, NY"
    actual = func.funcTwo(name,addr)
    #analyze
    assert expected == actual

"""