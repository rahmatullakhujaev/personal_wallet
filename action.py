class Action:
    def __init__(self, type, date, amount, description):
        self.type = type
        self.date = date
        self.amount = amount
        self.description = description

    def get_date(self):
        return self.date


    def get_amount(self):
        return self.amount


    def get_description(self):
        return self.description