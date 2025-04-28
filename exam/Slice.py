class Slice:
    def __init__(self, data, start=None, stop=None, step=None):
        self._data = data
        self._slice = slice(start, stop, step)

    def __iter__(self):
        start, stop, step = self._slice.indices(len(self._data))
        idx = start
        while (step > 0 and idx < stop) or (step < 0 and idx > stop):
            yield self._data[idx]
            idx += step


data = [10, 20, 30, 40, 50, 60, 70, 80]
smart = Slice(data, start=5, stop=1, step=-1)
for item in smart:
    print(item)