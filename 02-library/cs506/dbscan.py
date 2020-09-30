class DBC():

    def __init__(self, dataset, min_pts, epsilon):
        self.dataset = dataset
        self.min_pts = min_pts
        self.epsilon = epsilon

    def _get_neighborhood(self, p):
        Neighborhood = []
        for PN in range( len( self.dataset)):
            if euclidean_dist(self.dataset[p], self.dataset[PN]) <= self.epsilon:
                Neighborhood.append(PN)

        return Neighborhood

    def _explore_PNeighborhood(self, assignments, assignment, p, PNeighborhood):
        assignments[p] = assignment

        while PNeighborhood:
            NextP = PNeighborhood.pop()
            # NextPNeighborhood = self._get_neighborhood(NextP)

            if assignments[NextP] == -1:
                # border point
                assignments[NextP] = assignment
            
            if assignments[NextP] == 0:
                assignments[NextP] = assignment
                NextPNeighborhood = self._get_neighborhood(NextP)
        
                if len(NextPNeighborhood) >= self.min_pts:
                    PNeighborhood += NextPNeighborhood

        return assignments

    def dbscan(self):
        assignments = [0 for _ in range (len (self.dataset) ) ]
        assignment = 0

        for p in range (len (self.dataset) ):
            if assignments[p] != 0:
                continue
            
            PNeighborhood = self._get_neighborhood(p)
            
            if len(PNeighborhood) >= self.min_pts:
                # core point
                assignment += 1
                assignments = self._explore_PNeighborhood(assignments, assignment, p, PNeighborhood)
            else:
                # border or noise point
                assignments[p] = -1
        return assignments
        
