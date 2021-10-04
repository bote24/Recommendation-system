import sys


def guide():
    print('''\n
    The systems works by searching in a tree with the first word of the user input. 
    The tree is created between subjects and then its themes.
    Just type the first letter and the program will create a recommendation.
    If you want to break the program just type "break", if you want to restart write "restart"
    To see choices type "choices"
    ''')


class TreeNode:
    def __init__(self, subject_piece, name):
        self.subject_piece = subject_piece
        self.choices = []
        self.name = name
        self.choices_strings = []

    def add_child(self, node):
        self.choices.append(node)
        self.choices_strings.append(node.name)

    def traverse(self):
        subject_node = self
        print(subject_node.subject_piece)
        while subject_node.choices:
            choice = input().lower()
            answer = False
            if choice == 'break':
                sys.exit()
            if choice == 'restart':
                subject_node = self
                answer = True
                print('\nTree restarted, new choices:')
                for i in range(len(subject_node.choices_strings)):
                    element = subject_node.choices_strings[i]
                    print(f'---{element}')
                print(' ')
            if choice == 'choices':
                print(' ')
                print('Actual choices:')
                answer = True
                for i in range(len(subject_node.choices_strings)):
                    element = subject_node.choices_strings[i]
                    print(f'---{element}')
                print(' ')
            for i in range(len(subject_node.choices_strings)):
                if subject_node.choices:
                    element = subject_node.choices_strings[i]
                    if choice.startswith(element[0]):
                        result = input(f'\nIs {element} what you want to search? (y/n)').lower()
                        if result.startswith('y'):
                            chosen_child = subject_node.choices[i]
                            print(chosen_child.subject_piece)
                            answer = True
                            subject_node = chosen_child
                            print(' ')
                        else:
                            answer = True
                            break
            if not answer:
                print('''\n
    No result found, try typing again. 
    If want to have a quick guide type g.
    Else type n.''')
                not_answer = input().lower()
                if not_answer.startswith('g'):
                    guide()
        print('Would you like to restart (y/n)')
        answer = input().lower()
        if answer.startswith('y'):
            print(' ')
            self.traverse()


school_subjects = TreeNode('Welcome to the school repository, type the subject you want to see. Math(1) or Physics(2)',
                           'school_subjects')
mathematics = TreeNode('''
The abstract science of number, quantity, and space. Mathematics may be studied in its own right ( pure mathematics ), 
or as it is applied to other disciplines such as physics and engineering ( applied mathematics ).''', 'mathematics')
algebra = TreeNode('''
Algebra is a branch of mathematics dealing with symbols and the rules for manipulating those symbols.
In elementary algebra, those symbols (today written as Latin and Greek letters) represent quantities without fixed 
values,known as variables. The letters x and y represent the areas of the fields.''', 'algebra')
geometry = TreeNode('''
Geometry is the branch of mathematics concerned with the properties and relations of points, lines, surfaces, solids,
and higher dimensional analogs.''', 'geometry')
physics = TreeNode('''
The branch of mathematics concerned with the properties and relations of points, lines, surfaces, solids, and higher
dimensional analogs.''', 'physics')
thermodynamics = TreeNode('''
The branch of physical science that deals with the relations between heat and other forms of energy (such as mechanical,
electrical, or chemical energy), and, by extension, of the relationships between all forms of energy.''',
                          'thermodynamics')
nuclear = TreeNode('''
Nuclear physics is the field of physics that studies atomic nuclei and their constituents and interactions, 
in addition to the study of other forms of nuclear matter.''', 'nuclear')

school_subjects.add_child(mathematics)
school_subjects.add_child(physics)
mathematics.add_child(algebra)
mathematics.add_child(geometry)
physics.add_child(thermodynamics)
physics.add_child(nuclear)
