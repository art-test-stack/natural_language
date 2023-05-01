import random

def weighted_choice(choices):
    """A weighted version of random.choice"""
    # NOTE: should be replaced by random.choices if we port to Python 3.6

    total = sum(w for _, w in choices)
    r = random.uniform(0, total)
    upto = 0
    for c, w in choices:
        if upto + w >= r:
            return c, w
        upto += w


def Rules(**rules):
    """Create a dictionary mapping symbols to alternative sequences.
    >>> Rules(A = "B C | D E")
    {'A': [['B', 'C'], ['D', 'E']]}
    """
    for (lhs, rhs) in rules.items():
        rules[lhs] = [alt.strip().split() for alt in rhs.split('|')]
    return rules


def Lexicon(**rules):
    """Create a dictionary mapping symbols to alternative words.
    >>> Lexicon(Article = "the | a | an")
    {'Article': ['the', 'a', 'an']}
    """
    for (lhs, rhs) in rules.items():
        rules[lhs] = [word.strip() for word in rhs.split('|')]
    return rules


def ProbRules(**rules):
    """Create a dictionary mapping symbols to alternative sequences,
    with probabilities.
    >>> ProbRules(A = "B C [0.3] | D E [0.7]")
    {'A': [(['B', 'C'], 0.3), (['D', 'E'], 0.7)]}
    """
    for (lhs, rhs) in rules.items():
        rules[lhs] = []
        rhs_separate = [alt.strip().split() for alt in rhs.split('|')]
        for r in rhs_separate:
            prob = float(r[-1][1:-1])  # remove brackets, convert to float
            rhs_rule = (r[:-1], prob)
            rules[lhs].append(rhs_rule)

    return rules


def ProbLexicon(**rules):
    """Create a dictionary mapping symbols to alternative words,
    with probabilities.
    >>> ProbLexicon(Article = "the [0.5] | a [0.25] | an [0.25]")
    {'Article': [('the', 0.5), ('a', 0.25), ('an', 0.25)]}
    """
    for (lhs, rhs) in rules.items():
        rules[lhs] = []
        rhs_separate = [word.strip().split() for word in rhs.split('|')]
        for r in rhs_separate:
            prob = float(r[-1][1:-1])  # remove brackets, convert to float
            word = r[:-1][0]
            rhs_rule = (word, prob)
            rules[lhs].append(rhs_rule)

    return rules
