from sympy.logic.boolalg import to_cnf, Or


def _check_order(n):
        if not((0 <= n) and (n <= 1)):
            raise Exception('The order of a belief must be between 0 and 1')


class Belief:
    def __init__(self, proposition=None, order=None):
        self.proposition = proposition
        self.order = order

    def __eq__(self, other):
        return self.proposition == other.proposition and self.order == other.order

    def __ne__(self, other):
        return not self == other

    def __ge__(self, other):
        return self.order >= other.order

    def __gt__(self,other):
        return self.order > other.order

    def __repr__(self):
        return f'Belief: {self.proposition} || Order: {self.order}'



class BeliefBase:
    def __init__(self):
        self.beliefs = []

    def add_belief(self, other):
        """
        Add a belief to the belief base sorted by order, the highest order first.
        In case the belief is already in the belief base it is ignored.
        """
        # Checks if the order is within range
        _check_order(other.order)

        # Update in case belief already exists
        self.delete_belief(other)
        
        if len(self.beliefs) == 0 or self.beliefs[-1] >= other:
            self.beliefs.append(other)
        else:
            for idx, b in enumerate(self.beliefs):
                if other >= b:
                    self.beliefs.insert(idx, other)
                    break

    def delete_belief(self, other):
        """
        Delete a belief that is equal to 'other'
        """
        for belief in self.beliefs:
            if belief.proposition == other.proposition:
                self.beliefs.remove(belief)
                break

    def delete_belief_idx(self, idx):
        """
        Deletes a belief by index.
        """
        self.beliefs.pop(idx)


    def revise(self):
        pass

    def highest_degree(self, other):
        """
        Returns highest order from the belief in the belief base which entails prop
        """
        prop_cnf = to_cnf(other.proposition)
        if entails([], prop_cnf): # TODO check proper implementation of entails and for tautology
            return 1

        for belief in self.beliefs:
            if entails(belief.proposition, prop_cnf):
                return belief.order
        return 0

    def contract(self, other):
        """
        Removes any belief from the belief base needed so there are no contradictions
        """
        # Set of maximal subset of KB that not imply p
        prop_cnf = to_cnf(other.proposition)
        _check_order(other.order)

        for belief in self.beliefs:
            if belief > other:
                prop_cnf_hd = self.highest_degree(prop_cnf)
                props_disjunction = Or(prop_cnf_hd, belief.proposition)
                props_disjunction_hd = self.highest_degree(props_disjunction)
                if props_disjunction == props_disjunction_hd:
                    self.add_belief(Belief(belief, other.order))

    def expand(self):
        pass

    def clear(self):
        """
        Empty the Belief base
        """
        self.beliefs.clear()

    def __repr__(self):
        if len(self.beliefs) == 0:
            return '\nBelief base: Empty'
        return '\n'.join(str(belief) for belief in self.beliefs)

    def __len__(self):
        return len(self.beliefs)


