import json


class SearchByTag:

    def __init__(self, data_file, query_tag):
        with open(data_file) as data_file:
            self._data = json.load(data_file)
        self.query = query_tag
        self.idx = 0
        self.length = len(self._data["items"])

    def search(self):
        items = self._data["items"]
        while self.idx < self.length:
            item = items[self.idx]
            if self.query in item['tags']:
                self.idx += 1
                yield item
            else:
                self.idx += 1
        self.idx = 0

    def first(self):
        return next(self.search())




search = SearchByTag('source.json', 'crime')
gen = search.search()
print(search.first())
for g in gen:
    print(g)
