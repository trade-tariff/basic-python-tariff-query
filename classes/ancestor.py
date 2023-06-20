class Ancestor(object):
    def __init__(self, item):
        self.goods_nomenclature_sid = item["id"]
        self.goods_nomenclature_item_id = item["attributes"]["goods_nomenclature_item_id"]
        self.productline_suffix = item["attributes"]["producline_suffix"]
        self.number_indents = item["attributes"]["number_indents"]
        self.productline_suffix = item["attributes"]["producline_suffix"]
        self.validity_start_date = item["attributes"]["validity_start_date"]
        self.validity_end_date = item["attributes"]["validity_end_date"]
        self.description = item["attributes"]["formatted_description"]
