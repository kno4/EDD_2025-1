class Array2D:
    def __init__(self, ren, col):
        self._data = [[None] * col for _ in range(ren)]
        self._ren = ren
        self._cols = col

    def clear(self, dato):
        for row in range(self._ren):
            for col in range(self._cols):
                self._data[row][col] = dato

    def get_ren_size(self):
        return self._ren

    def get_col_size(self):
        return self._cols

    def set_item(self, ren, col, dato):
        if 0 <= ren < self._ren and 0 <= col < self._cols:
            self._data[ren][col] = dato
        else:
            raise IndexError("Índice fuera de rango")

    def get_item(self, ren, col):
        if 0 <= ren < self._ren and 0 <= col < self._cols:
            return self._data[ren][col]
        else:
            raise IndexError("Índice fuera de rango")

    def to_string(self):
        result = ""
        for row in self._data:
            result += " ".join(map(str, row)) + "\n"
        return result
