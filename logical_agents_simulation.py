from knowledge_base import *
from logical_agents import LogicalAgent


kb = KB([Clause('a', ['b', 'c']),
         Clause('b', ['g', 'e']),
         Clause('b', ['d', 'e']),
         Clause('c', ['e']),
         Askable('d'),
         Askable('k'),
         Clause('e'),
         Clause('f', ['a', 'g'])])

kb2 = KB([Clause('a', ['b', 'c']),
          Clause('b', ['e']),
          Clause('b', ['d']),
          Clause('c'),
          Clause('d', ['h']),
          Clause('e'),
          Clause('g', ['a', 'b', 'e']),
          Clause('f', ['h', 'b'])])

# print(kb2)
#[print(a) for a in kb.askables]
#[print(a) for a in kb.clauses]
#[print(a) for a in kb.c_for_a]
# #[print(a) for a in kb.c_for_a.items()]
#[print(c) for c in kb.clauses_for_atom('a')]
#[[print(c) for c in a[1]] for a in kb.c_for_a.items()]

#[print(a) for a in kb.statements]

# for a in kb.askables:
# aval = True if input(
# 'Is {} true / (yes/no):'.format(str(a))) == 'yes' else False

ag = LogicalAgent(kb2)

# Derive all the logical consequences of KB
#consequences = ag.bottom_up()
# print(consequences)

# Prove 'a'
print(ag.top_down(['g']))
