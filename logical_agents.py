class LogicalAgent():

    def __init__(self, KB):
        self.KB = KB

    # TODO
    def bottom_up(self):
        ''' Implements the botton up proof strategy and returns all the logical consequence odf the KB

        Returns:
            A list with all the logical consequences of KB
        '''
        consequenceList = []

        for ask in self.KB.askables:
            if ask not in consequenceList:
                answer = True if input(
                    'Is {} true / (yes/no):'.format(str(ask))) == 'yes' else False

                if answer:
                    consequenceList.append(ask.atom)

        while True:
            initialSize = len(consequenceList)
            clauses = self.KB.clauses
            for clause in clauses:
                if clause.head not in consequenceList:
                    if not clause.body:
                        consequenceList.append(clause.head)
                    else:
                        if all(map(lambda atom: atom in consequenceList, clause.body)):
                            consequenceList.append(clause.head)

            if initialSize == len(consequenceList):
                break
        return consequenceList

    # TODO
    def top_down(self, query):
        '''Implements the top down proof strategy. Given a query (the atom that it wants to prove) 
        it returns True if the query is a consequence of the knowledge base. 

        Args:
            querry: The atom that should be proved

        Returns: 
            True if the query is a logical consequence of KB, False otherwise

        '''

        questions = query
        askable = []
        askableTrue = []
        for ask in self.KB.askables:
            askable.append(ask.atom)

        while questions != []:
            atom = questions.pop(0)
            premise = self.KB.clauses_for_atom(atom)
            if len(premise) > 0:
                questions = premise[0].body + questions
            else:
                if atom not in askableTrue and atom in askable:
                    answer = True if input(
                        'Is {} true / (yes/no):'.format(str(atom))) == 'yes' else False
                    if answer:
                        askable.remove(atom)
                        askableTrue.append(atom)
                    else:
                        return False
                else:
                    return False
        return True

    # TODO

    def explain(self, g):
        '''Implements the process of abductions. It tries to explain the atoms  in the list g using
         the assumable in KB.

        Args:
            g: A set of atoms that should be explained

        Returns:
            A list of explanation for the atoms in g
        '''
        assumable = []
        consequenceList = []

        for assumed in self.KB.assumable:
            assumable.append(assumed.atom)

        for initial in g:
            if initial in assumable:
                consequenceList.append(initial)

        while g != []:
            atom = g.pop(0)
            clauses = self.KB.clauses_for_atom(atom)

            for premissa in clauses:
                for body in premissa.body:
                    if body in assumable:
                        clausesFalses = self.KB.clauses_for_atom('false')
                        add = True
                        for clausesFalse in clausesFalses:
                            if body in clausesFalse.body:
                                for a in clausesFalse.body:
                                    if a in consequenceList:
                                        add = False

                        if add:
                            consequenceList.append(body)
                    else:
                        g = [body] + g

        consequenceList = list(set(consequenceList))
        return consequenceList
