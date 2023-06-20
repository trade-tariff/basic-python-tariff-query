import sys
import os
import requests
from dotenv import load_dotenv

from classes.section import Section
from classes.chapter import Chapter
from classes.heading import Heading
from classes.ancestor import Ancestor
from classes.footnote import Footnote
from classes.measure_type import MeasureType
from classes.geographical_area import GeographicalArea
from classes.additional_code import AdditionalCode
from classes.measure import Measure
from classes.measure_condition import MeasureCondition
from classes.measure_component import MeasureComponent
from classes.duty_expression import DutyExpression


class Commodity(object):
    def __init__(self):
        self.section = None
        self.chapter = None
        self.heading = None
        self.ancestors = []
        self.footnotes = []
        self.measure_types = []
        self.geographical_areas = []
        self.additional_codes = []
        self.measures = []
        self.measure_conditions = []
        self.measure_components = []
        self.duty_expressions = []

        load_dotenv('.env')
        self.get_arguments()
        self.get_url_pattern()
        self.load_api_data()

    def get_arguments(self):
        if len(sys.argv) > 1:
            self.goods_nomenclature_item_id = sys.argv[1]
        else:
            print("Please provide a commodity code")
            sys.exit()

        if len(sys.argv) > 2:
            self.geographical_area_id = sys.argv[2]
        else:
            self.geographical_area_id = None

    def get_url_pattern(self):
        if self.geographical_area_id is None:
            self.api_url_pattern = os.getenv('api_url_pattern_basic')
        else:
            self.api_url_pattern = os.getenv('api_url_pattern_filtered')

        self.url = self.api_url_pattern.format(
            commodity=self.goods_nomenclature_item_id,
            geographical_area_id=self.geographical_area_id
        )

    def load_api_data(self):
        ret = requests.get(url=self.url)
        self.response_data = ret.json()
        self.data = self.response_data["data"]
        self.relationships = self.data["relationships"]
        self.included = self.response_data["included"]

        self.get_attributes()
        self.get_included_data()

    def get_attributes(self):
        attributes = self.data["attributes"]
        self.goods_nomenclature_sid = self.data["id"]
        self.description = attributes["formatted_description"]
        self.number_indents = attributes["number_indents"]
        self.validity_start_date = attributes["validity_start_date"]
        self.validity_end_date = attributes["validity_end_date"]
        self.declarable = attributes["declarable"]

    def get_included_data(self):
        for item in self.included:
            if item["type"] == "section":
                self.get_section(item)
            elif item["type"] == "chapter":
                self.get_chapter(item)
            elif item["type"] == "heading":
                self.get_heading(item)
            elif item["type"] == "ancestor":
                self.ancestors.append(self.get_ancestor(item))
            elif item["type"] == "footnote":
                self.footnotes.append(self.get_footnote(item))
            elif item["type"] == "measure_type":
                self.measure_types.append(self.get_measure_type(item))
            elif item["type"] == "geographical_area":
                self.geographical_areas.append(
                    self.get_geographical_area(item))
            elif item["type"] == "additional_code":
                self.additional_codes.append(self.get_additional_code(item))
            elif item["type"] == "measure":
                self.measures.append(self.get_measure(item))
            elif item["type"] == "measure_condition":
                self.measure_conditions.append(
                    self.get_measure_condition(item))
            elif item["type"] == "measure_component":
                self.measure_components.append(
                    self.get_measure_component(item))
            elif item["type"] == "duty_expression":
                self.duty_expressions.append(self.get_duty_expression(item))

        self.get_measure_relations()

    def get_section(self, item):
        self.section = Section(item)

    def get_chapter(self, item):
        self.section = Chapter(item)

    def get_heading(self, item):
        self.section = Heading(item)

    def get_ancestor(self, item):
        ancestor = Ancestor(item)
        return ancestor

    def get_footnote(self, item):
        footnote = Footnote(item)
        return footnote

    def get_measure_type(self, item):
        footnote = MeasureType(item)
        return footnote

    def get_geographical_area(self, item):
        geographical_area = GeographicalArea(item)
        return geographical_area

    def get_additional_code(self, item):
        additional_code = AdditionalCode(item)
        return additional_code

    def get_measure(self, item):
        measure = Measure(item)
        return measure

    def get_measure_condition(self, item):
        measure_condition = MeasureCondition(item)
        return measure_condition

    def get_measure_component(self, item):
        measure_component = MeasureComponent(item)
        return measure_component

    def get_duty_expression(self, item):
        duty_expression = DutyExpression(item)
        return duty_expression

    def get_measure_relations(self):
        for measure in self.measures:
            self.get_measure_footnotes(measure)
            self.get_measure_conditions(measure)
            self.get_measure_components(measure)
            self.get_measure_geographical_area(measure)
            self.get_measure_additional_code(measure)
            self.get_measure_measure_type(measure)
            self.get_measure_duty_expression(measure)

    def get_measure_footnotes(self, measure):
        for footnote in self.footnotes:
            for item in measure.relationships["footnotes"]["data"]:
                if footnote.footnote_id == item["id"]:
                    measure.footnotes.append(footnote)
                    break

    def get_measure_conditions(self, measure):
        for measure_condition in self.measure_conditions:
            for item in measure.relationships["measure_conditions"]["data"]:
                if measure_condition.measure_condition_sid == item["id"]:
                    measure.measure_conditions.append(measure_condition)
                    break

    def get_measure_components(self, measure):
        for measure_component in self.measure_components:
            for item in measure.relationships["measure_components"]["data"]:
                if measure_component.measure_component_id == item["id"]:
                    measure.measure_components.append(measure_component)
                    break

    def get_measure_geographical_area(self, measure):
        for geographical_area in self.geographical_areas:
            item = measure.relationships["geographical_area"]["data"]
            if geographical_area.geographical_area_id == item["id"]:
                measure.geographical_area = geographical_area
                break

    def get_measure_additional_code(self, measure):
        for additional_code in self.additional_codes:
            try:
                item = measure.relationships["additional_code"]["data"]
                if additional_code.additional_code_sid == int(item["id"]):
                    measure.additional_code = additional_code
                    break
            except Exception as e:
                pass

    def get_measure_measure_type(self, measure):
        for measure_type in self.measure_types:
            item = measure.relationships["measure_type"]["data"]
            if measure_type.measure_type_id == item["id"]:
                measure.measure_type = measure_type
                break

    def get_measure_duty_expression(self, measure):
        for duty_expression in self.duty_expressions:
            item = measure.relationships["duty_expression"]["data"]
            if duty_expression.duty_expression_id == item["id"]:
                measure.duty_expression = duty_expression
                break

    def get_basic_info(self):
        print("\n\nCommodity code {goods_nomenclature_item_id} has a description of ...\n\n{description}".format(
            goods_nomenclature_item_id=self.goods_nomenclature_item_id,
            description=self.description
        ))

    def get_third_country_duty(self):
        print("\nGetting third country duty")
        print("==========================\n")
        for measure in self.measures:
            if measure.measure_type.measure_type_id in ["103", "105"]:
                print("Measure {sid} of type {measure_type_id} has a duty of {duty_expression}".format(
                    sid=measure.measure_sid,
                    measure_type_id=measure.measure_type.measure_type_id,
                    duty_expression=measure.duty_expression.duty
                ))
                break

    def get_vat_measures(self):
        print("\nGetting VAT measures")
        print("====================\n")
        for measure in self.measures:
            if measure.measure_type.measure_type_id == "305":
                print("Measure {sid} of type {measure_type_id}, assigned to geo area {geographical_area_id} has a duty of {duty_expression} and a VAT type of {additional_code}".format(
                    sid=measure.measure_sid,
                    measure_type_id=measure.measure_type.measure_type_id,
                    geographical_area_id=measure.geographical_area.geographical_area_id,
                    duty_expression=measure.duty_expression.duty,
                    additional_code=measure.additional_code.additional_code if measure.additional_code is not None else "VATS (derived)"
                ))

    def get_preferences(self):
        print("\nGetting Preferences")
        print("===================\n")
        for measure in self.measures:
            if measure.measure_type.measure_type_id in ["142", "145"]:
                print("Measure {sid} of type {measure_type_id}, assigned to geo area {geographical_area_id} has a duty of {duty_expression}".format(
                    sid=measure.measure_sid,
                    measure_type_id=measure.measure_type.measure_type_id,
                    geographical_area_id=measure.geographical_area.geographical_area_id,
                    duty_expression=measure.duty_expression.duty
                ))
