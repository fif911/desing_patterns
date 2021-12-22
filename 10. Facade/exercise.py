from random import randint


class Generator:
    def generate(self, count):
        return [randint(1, 9) for x in range(count)]


class Splitter:
    def split(self, array):
        result = []

        row_count = len(array)
        col_count = len(array[0])

        for r in range(row_count):
            the_row = []
            for c in range(col_count):
                the_row.append(array[r][c])
            result.append(the_row)

        for c in range(col_count):
            the_col = []
            for r in range(row_count):
                the_col.append(array[r][c])
            result.append(the_col)

        diag1 = []
        diag2 = []

        for c in range(col_count):
            for r in range(row_count):
                if c == r:
                    diag1.append(array[r][c])
                r2 = row_count - r - 1
                if c == r2:
                    diag2.append(array[r][c])

        result.append(diag1)
        result.append(diag2)

        return result


class Verifier:
    def verify(self, arrays):
        first = sum(arrays[0])

        for i in range(1, len(arrays)):
            if sum(arrays[i]) != first:
                return False

        return True


class MagicSquareGenerator:
    def generate(self, size):
        # todo - return a magic square of the given size
        # magic_square = []
        g = Generator()
        s = Splitter()
        v = Verifier()

        i = 0
        while True:
            i += 1
            print(i)

            random_lists = []
            for line in range(size):
                random_lists.append(g.generate(size))

            possible_magic_square = s.split(random_lists)
            if v.verify(possible_magic_square):
                break

        return possible_magic_square
        # magic_square = Generator().generate(size)
        # Splitter().split(magic_square)


if __name__ == '__main__':
    result = MagicSquareGenerator().generate(3)
    print(result)
