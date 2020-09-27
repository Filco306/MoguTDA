


class CechComplex:
    """
        Cech Complex class.
        Generally very hard to compute.

        Improve computational time:
        - Dynamic Programming
            - Keep all connections in memory
            - 1. Take all 2-combinations. save the ones which still are a simplicial complex
              2. Take all 3-combinations based on the 2-simplicial complexes. Save the ones which still constitute a simplicial complex.
              3. Take all 4-combinations based on the 3-simplicial complexes.
                 Here, check that the intersection (that must be n-1 in size, i.e., 2 here when 3) is n-1 (3), and if it is,
                 check that the distance of these are < epsilon*2. If yes, then it survives until the next round.
              4. Continue until none are left. All simplicial complexes are then constructed.

              Complexity:
              O(n^3) (or is it O(n*4)?)

              WRONG
        TODO:
        https://math.stackexchange.com/questions/605826/check-whether-n-disks-intersect
        Create a generalized

        First, sort the disks by size, and discard any disk that entirely contains another. If only a single disk remains, return True. Iterate over all remaining pairs of disks.

        For each pair:
        - If they are disjoint, return False.
        - Otherwise, their boundaries intersect at exactly one or two points. Check whether the intersection point(s) are contained in all the remaining disks. If they are, return True; otherwise continue.
        Finally, if all pairs have been checked, return False.
    """
    def __init__(self, points, epsilon, labels=None, distfcn=distance.euclidean):
        self.pts = points
        self.labels = (range(len(self.pts))
                       if (labels is None or len(labels) != len(self.pts))
                       else labels)
        self.epsilon = epsilon
        self.distfcn = distfcn
        self.import_simplices(self.construct_simplices(self.pts,
                                                       self.labels,
                                                       self.epsilon,
                                                       self.distfcn))
    def construct_simplices(self, points, labels, epsilon, distfcn):
        self.distdict = calculate_distmatrix(points, labels, distfcn)


    def sphere_in_another(self, point1, point2, eps1, eps2):
        # Check if an n-dim sphere is contained within another.
        if eps1 == eps2 and point1 != point2:
            return False
        elif eps1 == eps2 and point1 == point2:
            return True

        if eps1 < eps2:
            # if eps1 < eps2 we should check if point1 is
            # contained within
            # In other words, the


        pass

    def is_a_face(self, combo):
        # combo is a combination of edges
        # for the combo to constitute a cech complex subset,
        # it must be
        # e.g., for 4 unique nodes, we should have 6 edges
        # for 3 unique nodes, we should 3 edges
        # In short, it should be fully connected
        for i in range(len(combo) - 1):
            for j in range(i + 1, len(combo)):
                if (combo[i].i, combo[j].i) not in self.edges:
                    return False
        return True

    def faces(self):
        if self.face_set is not None:
            return self.face_set
        self.face_set = set()

        # First of all, include all 0-dim faces.
        for node in self.nodes:
            self.face_set.add((node.i,))
        # Now, construct all the faces with more than 1 dimension!
        # Just use all the combinations of all different edges and see if they
        # constitute

        # Either we use all the nodes

        # Or all the edges.

        # Use all nodes: take all possible combinations of nodes
        # and see if all edges exist that are necessary
        for i in range(2, len(self.nodes) + 1):
            for combo in combinations(self.nodes, i):
                if self.is_a_face(combo):
                    self.face_set.add(tuple(sorted([node.i for node in combo])))
        return self.face_set
