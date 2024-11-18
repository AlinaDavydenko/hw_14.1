class Workers:
    list_of_data: list
    payment = 50000
    hour = 10

    list_of_data = []

    def __init__(self, payment, hour):
        self._payment = payment
        self._hour = hour

    @staticmethod
    def add_into_list(data):
        Workers.list_of_data.append(data)
