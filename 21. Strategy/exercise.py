import math
import cmath
from abc import ABC


class DiscriminantStrategy(ABC):
    """Interface for discriminant calculation strategy"""

    def calculate_discriminant(self, a, b, c): pass


class OrdinaryDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c) -> float:
        d = b ** 2 - 4 * a * c
        print(f"discriminant: {d}")

        return d


class RealDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c) -> float:
        d = b ** 2 - 4 * a * c
        print(f"discriminant: {d}")

        if d < 0:
            return float('nan')  # not a number
        else:
            return d


class QuadraticEquationSolver:
    def __init__(self, strategy: DiscriminantStrategy):
        self.strategy = strategy

    def solve(self, a: float, b: float, c: float):
        """ Returns a pair of complex (!) values """
        d = complex(self.strategy.calculate_discriminant(a, b, c), 0)

        first_part = (-b / 2 * a)
        second_part = cmath.sqrt(d) / 2 * a

        x1 = first_part + second_part
        x2 = first_part - second_part
        return x1, x2


if __name__ == '__main__':
    print("RealDiscriminantStrategy")
    qe = QuadraticEquationSolver(strategy=RealDiscriminantStrategy())
    print(qe.solve(6, 11, -35))
    print(qe.solve(1, -9, 14))  # There are two real roots.
    print(qe.solve(1, -2, 1))  # There is one real root.
    print(qe.solve(2, -5, 9))  # There are two complex roots

    print("OrdinaryDiscriminantStrategy")
    qe = QuadraticEquationSolver(strategy=OrdinaryDiscriminantStrategy())
    print(qe.solve(1, -9, 14))  # There are two real roots.
    print(qe.solve(1, -2, 1))  # There is one real root.
    print(qe.solve(2, -5, 9))  # There are two complex roots
