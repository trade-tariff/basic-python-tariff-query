class MeasureComponent(object):
    def __init__(self, item):
        self.measure_component_id = item["id"]
        self.duty_expression_id = item["attributes"]["duty_expression_id"]
        self.duty_amount = item["attributes"]["duty_amount"]
        self.monetary_unit_code = item["attributes"]["monetary_unit_code"]
        self.monetary_unit_abbreviation = item["attributes"]["monetary_unit_abbreviation"]
        self.measurement_unit_code = item["attributes"]["measurement_unit_code"]
        self.measurement_unit_qualifier_code = item["attributes"]["measurement_unit_qualifier_code"]
        self.duty_expression_description = item["attributes"]["duty_expression_description"]
        self.duty_expression_abbreviation = item["attributes"]["duty_expression_abbreviation"]
