# Test Stability of a component

class StabilityTest:

    def __init__(self, nc, na, fi, fo):
        self._na = na
        self._nc = nc
        self._fo = fo
        self._fi = fi

    def calculate_abstractness(self):
        return self._na / self._nc

    def calculate_instability(self):
        return self._fo / (self._fi + self._fo)

    def calculate_distance_from_sequence(self):
        return abs(self.calculate_abstractness() + self.calculate_instability() - 1)


if __name__ == '__main__':
    nc = int(input("number of class: "))
    na = int(input("number of abstract class: "))
    fi = int(input("fan in: "))
    fo = int(input("fan out: "))
    test = StabilityTest(nc, na, fi, fo)

    print("Abstractness " + test.calculate_abstractness().__str__())
    print("Instability: " + test.calculate_instability().__str__())
    print("Distance from main sequence: " + test.calculate_distance_from_sequence().__str__())
