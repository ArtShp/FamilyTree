from family_tree import FamilyTree, Members

Tree = FamilyTree()

Artem = Members('Artem', 'm')
Artem.add_parent('Olga', 'w')
Artem.add_parent('Dima', 'm')
Artem.add_child('Polina', 'w')
Artem.add_child('Danil', 'm')
Artem.about_me()
Artem.delete_child('Polina', 'w')
Artem.about_me()

Dima = Members('Dima', 'm')

Tree.show_all_members()
