from sympy.logic.boolalg import to_cnf, Or
from entailment import *
from utils import _to_cnf # TODO IMPLEMENT CUSTOM CNF FUNCTION TO ALL AND TEST FOR BI-IMPLICATION


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
        Delete a beliefs equal to 'other'
        """
        self.beliefs = [belief for belief in self.beliefs if belief.proposition != other.proposition]                

    def delete_belief_idx(self, idx):
        """
        Deletes a belief by index.
        """
        self.beliefs.pop(idx)


    def revise(self, other):
        prop_cnf = to_cnf(other.proposition)
        _check_order(other.order)

        # Check for contradiction in proposition
        if not entailment([], ~prop_cnf):
            # If tautology change order to maximum (always true)
            if entailment([], prop_cnf):
                other.order = 1
            else:
                # Levi Identity for revision
                self.contract(Belief(~to_cnf(other.proposition), other.order))
                self.expand(other)

        

    def highest_degree(self, other):
        """
        Returns highest order from the belief in the belief base which entails prop
        """
        prop_cnf = to_cnf(other.proposition)
        if entailment([], prop_cnf):
            return 1

        for belief in self.beliefs:
            if entailment(belief.proposition, prop_cnf):
                return belief.order
        return 0

    def contract(self, other):
        """
        Removes any belief from the belief base needed so there are no contradictions
        """
        # Set of maximal subset of KB that not imply other
        prop_cnf = to_cnf(other.proposition)
        _check_order(other.order)
        
        _to_delete = []
        for i, belief in enumerate(self.beliefs):
            if entailment(self.beliefs[0:i+1], prop_cnf) and other > belief:
                _to_delete.append(belief)

        self.beliefs = [belief for belief in self.beliefs if belief not in _to_delete]

    def expand(self, other):
        prop_cnf = other.proposition
        _check_order(other.order)

        self.add_belief(other)

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
