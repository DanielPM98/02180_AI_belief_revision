

from numpy import delete


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

    def __repr__(self):
        return f'Belief: {self.proposition} || Order: {self.order}'



class BeliefBase:
    def __init__(self):
        self.beliefs = []

    def add_belief(self, belief):
        """
        Add a belief to the belief base sorted by order, the highest order first.
        In case the belief is already in the belief base it is ignored.
        """
        # Checks if the order is within range
        _check_order(belief.order)

        # Update in case belief already exists
        self.delete_belief(belief)
        
        if len(self.beliefs) == 0 or self.beliefs[-1] >= belief:
            self.beliefs.append(belief)
        else:
            for idx, b in enumerate(self.beliefs):
                if belief >= b:
                    self.beliefs.insert(idx, belief)
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

    def __repr__(self):
        if len(self.beliefs) == 0:
            return '\nEmpty Belief base'
        return '\n'.join(str(belief) for belief in self.beliefs)

    def __len__(self):
        return len(self.beliefs)


def _check_order(n):
        if not((0 <= n) and (n <= 1)):
            raise Exception('The order of a belief must be between 0 and 1')