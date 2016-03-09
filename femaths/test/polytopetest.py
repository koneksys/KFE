import unittest
from femath.polytope import Polytopedimension, Polytopetype, Polytope


class PolytopeTest(unittest.TestCase):

    def test_simplexline(self):
        polytopetype = Polytopetype.simplex
        polytopedim = Polytopedimension.dim1
        polytope = Polytope(polytopetype, polytopedim)
        print(polytope.__dict__)

    def test_simplextriangle(self):
        polytopetype = Polytopetype.simplex
        polytopedim = Polytopedimension.dim2
        polytope = Polytope(polytopetype, polytopedim)
        print(polytope.__dict__)

    def test_simplextetrahedron(self):
        polytopetype = Polytopetype.simplex
        polytopedim = Polytopedimension.dim3
        polytope = Polytope(polytopetype, polytopedim)
        print(polytope.__dict__)

    def test_cubeline(self):
        polytopetype = Polytopetype.cube
        polytopedim = Polytopedimension.dim1
        polytope = Polytope(polytopetype, polytopedim)
        print(polytope.__dict__)

    def test_cubesquare(self):
        polytopetype = Polytopetype.cube
        polytopedim = Polytopedimension.dim2
        polytope = Polytope(polytopetype, polytopedim)
        print(polytope.__dict__)

    def test_cubecube(self):
        polytopetype = Polytopetype.cube
        polytopedim = Polytopedimension.dim3
        polytope = Polytope(polytopetype, polytopedim)
        print(polytope.__dict__)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(PolytopeTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
