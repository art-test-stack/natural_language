from collections import defaultdict

class Grammar:

    def __init__(self, name, rules, lexicon):
        """A grammar has a set of rules and a lexicon."""
        self.name = name
        self.rules = rules
        self.lexicon = lexicon
        self.categories = defaultdict(list)
        for lhs in lexicon:
            for word in lexicon[lhs]:
                self.categories[word].append(lhs)

    def rewrites_for(self, cat):
        """Return a sequence of possible rhs's that cat can be rewritten as."""
        return self.rules.get(cat, ())

    def isa(self, word, cat):
        """Return True iff word is of category cat"""
        return cat in self.categories[word]

    def cnf_rules(self):
        """Returns the tuple (X, Y, Z) for rules in the form:
        X -> Y Z"""
        cnf = []
        for X, rules in self.rules.items():
            for (Y, Z) in rules:
                cnf.append((X, Y, Z))

        return cnf

    def generate_random(self, S='S'):
        """Replace each token in S by a random entry in grammar (recursively)."""
        import random

        def rewrite(tokens, into):
            for token in tokens:
                if token in self.rules:
                    rewrite(random.choice(self.rules[token]), into)
                elif token in self.lexicon:
                    into.append(random.choice(self.lexicon[token]))
                else:
                    into.append(token)
            return into

        return ' '.join(rewrite(S.split(), []))

    def __repr__(self):
        return '<Grammar {}>'.format(self.name)

