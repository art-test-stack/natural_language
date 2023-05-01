from language_rules.grammar import Grammar
from language_rules.prob_grammar import ProbGrammar
from language_rules.utils import Rules, Lexicon, ProbRules, ProbLexicon

E0 = Grammar('E0',
             Rules(  # Grammar for E_0 [Figure 22.4]
                 S='NP VP | S Conjunction S',
                 NP='Pronoun | Name | Noun | Article Noun | Digit Digit | NP PP | NP RelClause',
                 VP='Verb | VP NP | VP Adjective | VP PP | VP Adverb',
                 PP='Preposition NP',
                 RelClause='That VP'),

             Lexicon(  # Lexicon for E_0 [Figure 22.3]
                 Noun="stench | breeze | glitter | nothing | wumpus | pit | pits | gold | east",
                 Verb="is | see | smell | shoot | fell | stinks | go | grab | carry | kill | turn | feel",  # noqa
                 Adjective="right | left | east | south | back | smelly",
                 Adverb="here | there | nearby | ahead | right | left | east | south | back",
                 Pronoun="me | you | I | it",
                 Name="John | Mary | Boston | Aristotle",
                 Article="the | a | an",
                 Preposition="to | in | on | near",
                 Conjunction="and | or | but",
                 Digit="0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9",
                 That="that"
             ))

E_ = Grammar('E_',  # Trivial Grammar and lexicon for testing
             Rules(
                 S='NP VP',
                 NP='Art N | Pronoun',
                 VP='V NP'),

             Lexicon(
                 Art='the | a',
                 N='man | woman | table | shoelace | saw',
                 Pronoun='I | you | it',
                 V='saw | liked | feel'
             ))

E_NP_ = Grammar('E_NP_',  # Another Trivial Grammar for testing
                Rules(NP='Adj NP | N'),
                Lexicon(Adj='happy | handsome | hairy',
                        N='man'))

E_Prob = ProbGrammar('E_Prob',  # The Probabilistic Grammar from the notebook
                     ProbRules(
                         S="NP VP [0.6] | S Conjunction S [0.4]",
                         NP="Pronoun [0.2] | Name [0.05] | Noun [0.2] | Article Noun [0.15] \
                             | Article Adjs Noun [0.1] | Digit [0.05] | NP PP [0.15] | NP RelClause [0.1]",
                         VP="Verb [0.3] | VP NP [0.2] | VP Adjective [0.25] | VP PP [0.15] | VP Adverb [0.1]",
                         Adjs="Adjective [0.5] | Adjective Adjs [0.5]",
                         PP="Preposition NP [1]",
                         RelClause="RelPro VP [1]"
                     ),
                     ProbLexicon(
                         Verb="is [0.5] | say [0.3] | are [0.2]",
                         Noun="robot [0.4] | sheep [0.4] | fence [0.2]",
                         Adjective="good [0.5] | new [0.2] | sad [0.3]",
                         Adverb="here [0.6] | lightly [0.1] | now [0.3]",
                         Pronoun="me [0.3] | you [0.4] | he [0.3]",
                         RelPro="that [0.5] | who [0.3] | which [0.2]",
                         Name="john [0.4] | mary [0.4] | peter [0.2]",
                         Article="the [0.5] | a [0.25] | an [0.25]",
                         Preposition="to [0.4] | in [0.3] | at [0.3]",
                         Conjunction="and [0.5] | or [0.2] | but [0.3]",
                         Digit="0 [0.35] | 1 [0.35] | 2 [0.3]"
                     ))

E_Chomsky = Grammar('E_Prob_Chomsky',  # A Grammar in Chomsky Normal Form
                    Rules(
                        S='NP VP',
                        NP='Article Noun | Adjective Noun',
                        VP='Verb NP | Verb Adjective',
                    ),
                    Lexicon(
                        Article='the | a | an',
                        Noun='robot | sheep | fence',
                        Adjective='good | new | sad',
                        Verb='is | say | are'
                    ))

E_Prob_Chomsky = ProbGrammar('E_Prob_Chomsky',  # A Probabilistic Grammar in CNF
                             ProbRules(
                                 S='NP VP [1]',
                                 NP='Article Noun [0.6] | Adjective Noun [0.4]',
                                 VP='Verb NP [0.5] | Verb Adjective [0.5]',
                             ),
                             ProbLexicon(
                                 Article='the [0.5] | a [0.25] | an [0.25]',
                                 Noun='robot [0.4] | sheep [0.4] | fence [0.2]',
                                 Adjective='good [0.5] | new [0.2] | sad [0.3]',
                                 Verb='is [0.5] | say [0.3] | are [0.2]'
                             ))
E_Prob_Chomsky_ = ProbGrammar('E_Prob_Chomsky_',
                              ProbRules(
                                  S='NP VP [1]',
                                  NP='NP PP [0.4] | Noun Verb [0.6]',
                                  PP='Preposition NP [1]',
                                  VP='Verb NP [0.7] | VP PP [0.3]',
                              ),
                              ProbLexicon(
                                  Noun='astronomers [0.18] | eyes [0.32] | stars [0.32] | telescopes [0.18]',
                                  Verb='saw [0.5] | \'\' [0.5]',
                                  Preposition='with [1]'
                              ))

