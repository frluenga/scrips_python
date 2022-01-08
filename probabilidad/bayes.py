from typing import Callable


def calc_bayes(prior_A, Prob_B_dado_A , prob_B):
    return (prior_A * Prob_B_dado_A)/prob_B


if __name__ == "__main__":
    prob_cancer = 1/100000
    prob_sintoma_dado_cancer = 1
    prob_sintoma_dado_no_cancer = 10/99990
    proba_no_cancer = 1 - prob_cancer

    prob_sintoma = (prob_sintoma_dado_cancer * prob_cancer) + (prob_sintoma_dado_no_cancer * proba_no_cancer)

    prob_cancer_dado_sintoma = calc_bayes(prob_cancer,prob_sintoma_dado_cancer,prob_sintoma)

    print(prob_cancer_dado_sintoma) 
