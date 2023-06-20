class DutyExpression(object):
    def __init__(self, item):
        self.duty_expression_id = item["id"]
        self.duty = item["attributes"]["verbose_duty"]
