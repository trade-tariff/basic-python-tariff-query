class Heading(object):
    def __init__(self, item):
        self.id = item["id"]
        self.goods_nomenclature_item_id = item["attributes"]["goods_nomenclature_item_id"]
        self.description = item["attributes"]["formatted_description"]
        self.validity_start_date = item["attributes"]["validity_start_date"]
        self.validity_end_date = item["attributes"]["validity_end_date"]
