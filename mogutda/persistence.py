# Calculate the barcodes and stuff.

#from .abssimcomplex import SimplicialComplex

from mogutda.vrcomplex import VietorisRipsComplex


class Edge:
    def __init__(self, node1, node2, distance):
        self.node1 = node1
        self.node2 = node2
        self.distance = distance


class Node:
    def __init__(self, i, value):
        self.i = i
        self.value = value


def generate_barcodes(X, eps_min=1e-2, eps_max=5, n_samples=100, type="VR"):
    # Generate the barcodes
    type = {"VR" : VietorisRipsComplex,
            "AC" : SimplicialComplex}
