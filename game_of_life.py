class Universe:
    def __init__(self, *seeds):
        self.living_cells = set(seeds)
        self.cells_to_add = set()
        self.cells_to_remove = set()
        self.neighbors_to_check = set()

    def tick(self):
        for x, y in self.living_cells:
            num_live_neighbors = 0
            for neighbor in ((x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x - 1, y), (x + 1, y), (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)):
                if neighbor in self.living_cells:
                    num_live_neighbors += 1
                else:
                    self.neighbors_to_check.add(neighbor)
            if num_live_neighbors < 2 or num_live_neighbors > 3:
                self.cells_to_remove.add((x, y))

        for x, y in self.neighbors_to_check:
            num_live_neighbors = 0
            for neighbor in ((x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x - 1, y), (x + 1, y), (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)):
                if neighbor in self.living_cells:
                    num_live_neighbors += 1
            if num_live_neighbors == 3:
                self.cells_to_add.add((x, y))

        for cell in self.cells_to_add:
            self.living_cells.add(cell)

        for cell in self.cells_to_remove:
            self.living_cells.remove(cell)

        self.cells_to_add.clear()
        self.cells_to_remove.clear()
        self.neighbors_to_check.clear()

    def show(self, bottom_left=(0, 0), top_right=(10, 10)):
        dimensions = (top_right[0] - bottom_left[0] + 1, top_right[1] - bottom_left[1] + 1)
        canvas = [" " * dimensions[0]] * dimensions[1]
        for living_cell in self.living_cells:
            if bottom_left[0] <= living_cell[0] <= top_right[0] and bottom_left[1] <= living_cell[1] <= top_right[1]:
                row_index = top_right[1] - living_cell[1]
                col_index = living_cell[0] - bottom_left[0]
                canvas[row_index] = canvas[row_index][:col_index] + "#" + canvas[row_index][col_index + 1:]
        return "\n".join(canvas)
