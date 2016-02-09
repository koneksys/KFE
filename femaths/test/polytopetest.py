import unittest
from femaths.polytope import Polytope


class Polytopetest(unittest.TestCase):
    def test_get_topo_triangle(self):
        polytopetype = 'simplex'
        polytopedim = 2
        triangle = Polytope(polytopetype, polytopedim)
        self.assertEquals(triangle.get_topo())

    if __name__ == "__main__":
        unittest.main()
