from tree import Tree, Leaf
from print_tree import print_tree

lexicon = {
        Leaf('N', 'buffalo'), # beasts
        Leaf('V', 'buffalo'), # intimidate
        Leaf('J', 'buffalo'), # from New York
        Leaf('R', 'that')
        }

grammar = {
        'S':  [['NP', 'VP']],
        'NP': [['N'], ['J', 'N'], ['NP', 'RP']],
        'VP': [['V', 'NP']],
        'RP': [['R', 'NP', 'V']],
        }

def expand(tag):
    """Yield all trees rooted by tag."""
    for leaf in lexicon:
        if tag == leaf.tag:
            yield leaf
    if tag in grammar:
        for tags in grammar[tag]:
            for branches in expand_all(tags):
                yield Tree(tag, branches)

def expand_all(tags):
    """Yield all sequences of branches for a sequence of tags."""
    if len(tags) == 1:
        for branch in expand(tags[0]):
            yield [branch]
    else:
        first, rest = tags[0], tags[1:]
        for first_branch in expand(first):
            for rest_branches in expand_all(rest):
                yield [first_branch] + rest_branches
                
for tree in expand('S'):
    print_tree(tree)
