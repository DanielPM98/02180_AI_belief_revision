from queue import PriorityQueue

class Belief:
    def __init__(self, proposition, order=None):
        self.proposition = proposition
        self.order = order



class BeliefBase:
    def __init__(self):
        self.beliefs = PriorityQueue()

    def add_belief(self, belief):
        """
        Add a belief to the belief base sorted by order, the highest order first
        """
        self.beliefs.put((belief.order, belief.proposition))