import math
def n_choose_one(n):
    return 1/n
def choose_same_m_times(n,m):
    return n_choose_one(n)**m
def number_of_draws_for_probability(n,p):
    
    return math.ceil(math.log(1-p,1-n_choose_one(n)))
def n_from_probability(p_item):
    n = 1/p_item
    
    return 

def main():
    p = float(input("Enter a probability:"))
    print(n_from_probability(p))

if __name__ == "__main__":
    main()
