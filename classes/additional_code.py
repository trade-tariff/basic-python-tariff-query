class AdditionalCode(object):
    def __init__(self, item):
        self.additional_code_sid = int(item["id"])
        self.additional_code = item["attributes"]["code"]
        self.description = item["attributes"]["formatted_description"]
