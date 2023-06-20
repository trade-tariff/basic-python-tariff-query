class GeographicalArea(object):
    def __init__(self, item):
        self.geographical_area_id = item["id"]
        if len(self.geographical_area_id) == 2:
            self.geographical_area_sid = item["attributes"]["geographical_area_sid"]
        else:
            self.geographical_area_sid = None
        self.description = item["attributes"]["description"]
