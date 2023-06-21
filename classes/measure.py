class Measure(object):
    def __init__(self, item):
        self.measure_sid = item["id"]
        self.is_import = item["attributes"]["import"]
        self.is_export = item["attributes"]["export"]
        self.effective_start_date = item["attributes"]["effective_start_date"]
        self.effective_end_date = item["attributes"]["effective_end_date"]
        self.excise = item["attributes"]["excise"]
        self.vat = item["attributes"]["vat"]
        self.relationships = item["relationships"]

        self.measure_conditions = []
        self.measure_components = []
        self.footnotes = []
        self.additional_code = None
        self.order_number = None
        self.measure_type = None
        self.geographical_area_id = None
