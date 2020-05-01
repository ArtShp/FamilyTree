class FamilyTree:
    members = {}

    def show_all_members(self):
        print('All Members:', self.members, end='\n\n')


class Members(FamilyTree):
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        self.parents = []
        self.children = []
        self.members[self.name] = {'sex': self.sex, 'parents': self.parents, 'children': self.children}

    def add_parent(self, parent, sex):
        self.parents.append([parent, sex])
        #self.members[parent] = {'sex': sex, 'parents': self.parents, 'children': self.children}

    def add_child(self, child, sex):
        self.children.append([child, sex])

    def delete_parent(self, parent, sex):
        self.parents.remove([parent, sex])

    def delete_child(self, child, sex):
        self.children.remove([child, sex])

    def about_me(self):
        print('Parents:', self.parents)
        print('Children:', self.children, end='\n\n')
