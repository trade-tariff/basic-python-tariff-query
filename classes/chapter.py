class Chapter(object):
    def __init__(self, item):
        self.goods_nomenclature_item_id = item["attributes"]["goods_nomenclature_item_id"]
        self.description = item["attributes"]["formatted_description"]
        self.validity_start_date = item["attributes"]["validity_start_date"]
        self.validity_end_date = item["attributes"]["validity_end_date"]
        self.chapter_note = item["attributes"]["chapter_note"]
