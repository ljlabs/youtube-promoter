import couchdb
from copy import deepcopy


def filter_items(id, items):
    for item in items:
        if item['id'] == id:
            items.remove(item)
    return items


class CouchHandler:
    def __init__(self, server_url, db_name):
        self.couch = couchdb.Server(server_url)
        try:
            self.db = self.couch.create(db_name)
        except:
            self.db = self.couch[db_name]

    def get_new_items(self, items):
        new_items = deepcopy(items)
        for id in self.db:
            new_items = filter_items(id, new_items)
        return new_items

    def upload(self, item):
        item['_id'] = item['id']
        self.db.save(item)
