import pandas as pd
import requests
from dotenv import load_dotenv

from classes.geographical_area import GeographicalArea


class GeographicalAreaCollection(object):
    def __init__(self):
        self.geographical_areas = []
        self.geographical_areas_dict = {}
        self.get_url()
        self.load_api_data()

    def get_url(self):
        self.api_url = "https://www.trade-tariff.service.gov.uk/api/v2/geographical_areas/"

    def load_api_data(self):
        ret = requests.get(url=self.api_url)
        self.response_data = ret.json()
        self.data = self.response_data["data"]
        self.included = self.response_data["included"]
        a = 1

        self.get_group_data()
        self.get_included_data()
        self.get_members()

    def get_group_data(self):
        # Gets the groups files
        for item in self.data:
            if item["relationships"]["children_geographical_areas"]["data"]:
                self.geographical_areas.append(self.get_geographical_area(item))

    def get_included_data(self):
        # Gets the individual countries
        for item in self.included:
            if item["type"] == "geographical_area":
                self.geographical_areas_dict[item["id"]] = self.get_geographical_area(item)

    def get_geographical_area(self, item):
        geographical_area = GeographicalArea(item)
        return geographical_area

    def get_members(self):
        for geographical_area in self.geographical_areas:
            if geographical_area.children_geographical_areas is not None:
                geographical_area.get_members(self.geographical_areas_dict)

    def print_members(self):
        self.printable_geo_areas = []
        for geographical_area in self.geographical_areas:
            self.printable_geo_areas.append(geographical_area.to_dict())
        df = pd.DataFrame(self.printable_geo_areas, columns=['geographical_area_id', 'member_string'])
        with pd.option_context('display.max_rows', None,
                               'display.max_columns', None,
                               'display.width', None,
                               'display.max_colwidth', 120
                               ):
            print(df)
    a = 1
