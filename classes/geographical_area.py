class GeographicalArea(object):
    def __init__(self, item):
        self.geographical_area_id = item["id"]
        self.geographical_area_sid = None
        self.members = []
        self.member_string = ""

        if len(self.geographical_area_id) == 2:
            try:
                self.geographical_area_sid = item["attributes"]["geographical_area_sid"]
            except Exception as e:
                pass

        self.description = item["attributes"]["description"]
        self.description_plus_id = "{description} ({geographical_area_id})".format(
            description=self.description,
            geographical_area_id=self.geographical_area_id
        )

        # Get relationships
        self.children_geographical_areas = None
        try:
            self.children_geographical_areas = item["relationships"]["children_geographical_areas"]["data"]
        except Exception as e:
            pass

    def get_members(self, geographical_areas_dict):
        for geo_area in self.children_geographical_areas:
            self.members.append(geographical_areas_dict[geo_area["id"]])

        self.member_string = ', '.join([str(x.description_plus_id) for x in self.members])

    def to_dict(self):
        return {
            "geographical_area_id": self.geographical_area_id,
            "member_string": self.member_string
        }
