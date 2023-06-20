class Footnote(object):
    def __init__(self, item):
        self.footnote_id = item["attributes"]["code"]
        self.description = item["attributes"]["formatted_description"]
