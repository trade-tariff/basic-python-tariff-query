class MeasureType(object):
    def __init__(self, item):
        self.measure_type_id = item["id"]
        self.description = item["attributes"]["description"]
        self.measure_type_series_id = item["attributes"]["measure_type_series_id"]
        self.measure_type_series_description = item["attributes"]["measure_type_series_description"]
        self.measure_component_applicable_code = item["attributes"]["measure_component_applicable_code"]
        self.trade_movement_code = item["attributes"]["trade_movement_code"]
        self.validity_start_date = item["attributes"]["validity_start_date"]
        self.validity_end_date = item["attributes"]["validity_end_date"]
