import random

from collections import defaultdict
from language_rules.utils import weighted_choice
class ProbGrammar:

    def __init__(self, name, rules, lexicon):
        """A grammar has a set of rules and a lexicon.
        Each rule has a probability."""
        self.name = name
        self.rules = rules
        self.lexicon = lexicon
        self.categories = defaultdict(list)

        for lhs in lexicon:
            for word, prob in lexicon[lhs]:
                self.categories[word].append((lhs, prob))

    def rewrites_for(self, cat):
        """Return a sequence of possible rhs's that cat can be rewritten as."""
        return self.rules.get(cat, ())

    def isa(self, word, cat):
        """Return True iff word is of category cat"""
        return cat in [c for c, _ in self.categories[word]]

    def cnf_rules(self):
        """Returns the tuple (X, Y, Z, p) for rules in the form:
        X -> Y Z [p]"""
        cnf = []
        for X, rules in self.rules.items():
            for (Y, Z), p in rules:
                cnf.append((X, Y, Z, p))

        return cnf

    def generate_random(self, S='S'):
        """Replace each token in S by a random entry in grammar (recursively).
        Returns a tuple of (sentence, probability)."""
        import random

        def rewrite(tokens, into):
            for token in tokens:
                if token in self.rules:
                    non_terminal, prob = weighted_choice(self.rules[token])
                    into[1] *= prob
                    rewrite(non_terminal, into)
                elif token in self.lexicon:
                    terminal, prob = weighted_choice(self.lexicon[token])
                    into[0].append(terminal)
                    into[1] *= prob
                else:
                    into[0].append(token)
            return into

        rewritten_as, prob = rewrite(S.split(), [[], 1])
        return (' '.join(rewritten_as), prob)

    def __repr__(self):
        return '<Grammar {}>'.format(self.name)
