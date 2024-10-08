def drug_user(prob_th=0.8, sensitivity=0.79, specificity=0.79, prevalence=0.02, verbose=True):
    p_user = prevalence
    p_non_user = 1 - prevalence
    p_pos_user = sensitivity
    p_neg_user = specificity
    p_pos_non_user = 1 - specificity

    num = p_pos_user * p_user
    den = p_pos_user * p_user + p_pos_non_user * p_non_user

    prob = num / den

    if verbose:
        if prob > prob_th:
            print("The test taker could be a user")
        else:
            print("The test taker may not be a user")

    return prob

print("Sam Jones")

p = drug_user(prob_th=0.5, sensitivity=0.97, specificity=0.95, prevalence=0.005)

print("Probability of the test taker being a drug user is:", round(p, 3))