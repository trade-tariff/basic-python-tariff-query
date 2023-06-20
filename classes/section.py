class Section(object):
    def __init__(self, item):
        self.numeral = item["attributes"]["numeral"]
        self.title = item["attributes"]["title"]
        self.position = item["attributes"]["position"]
        self.section_note = item["attributes"]["section_note"]
