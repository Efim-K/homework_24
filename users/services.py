import stripe

from config.settings import STRIPE_API_KEY
from forex_python.converter import CurrencyRates

stripe.api_key = STRIPE_API_KEY


def convert_rur_to_usd(amount):
    """
    Преобразуем руби в доллары.
    """
    c = CurrencyRates()
    rate = c.get_rate("RUB", "USD")
    return int(amount * rate)


def create_stripe_price(amount):
    """
    Создаем цену в Stripe.
    """
    return stripe.Price.create(
        currency="USD",
        unit_amount=amount * 100,
        product_data={"name": "Payments"},
    )


def create_stripe_session(price):
    """
    Создаем сессию на оплату в Stripe.
    """
    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{"price": price.get('id'), "quantity": 1}],
        mode="payment",
    )
    return session.get('id'), session.get('url')
