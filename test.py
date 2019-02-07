import moyasar

moyasar.api_key = 'sk_test_DUtsJkXP9hdJYyG4dVTdevz9R5QzbCDrF3KTPDNV'
# fetch = moyasar.Invoice.fetch('b4317684-4870-494d-8823-830fab146ab7')
# print(moyasar.Invoice.list())
# print(fetch.cancel())
data = {
    "amount": 7500,
    "currency": "SAR",
    "source": {
        "type": "creditcard",
        "name": "Nuha Almozaini",
        "number": "4222948503332818",
        "cvc": 744,
        "month": 8,
        "year": 2022,

    },
    "callback_url": "http://nuha.io/payment"
}
moyasar.Payment.create(data)
payment = moyasar.Payment.fetch('dc409895-0208-43f9-be11-6dcc8ad30a01')
refund = moyasar.Payment.refund(payment, amount=3500)
payment.refund(amount=3333)
payment.update({"description": "test test test"})