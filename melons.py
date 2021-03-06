"""This file should have our order classes in it."""
from random import randint
import datetime as dt

class TooManyMelonsError(ValueError):
    pass

class AbstractMelonOrder(object):
    """Melon Order"""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""
        self.species = species
        self.qty = qty
        self.shipped = False

    def get_base_price(self):
        base_price = randint(5, 9)
        now = dt.datetime.now()
        hour = now.hour
        day_of_week = now.weekday()
        if (day_of_week < 5) and (8 <= hour < 11):
            base_price += 4
        return base_price

    def get_total(self):
        """Calculate price."""
        base_price = self.get_base_price()
        if self.species == "Christmas melon":
            base_price = base_price * 1.5
        total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        super(DomesticMelonOrder, self).__init__(species, qty)
        self.order_type = "domestic"
        self.tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""

        super(InternationalMelonOrder, self).__init__(species, qty)
        self.country_code = country_code
        self.order_type = "international"
        self.tax = 0.17

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):
        total = super(InternationalMelonOrder, self).get_total()
        if self.qty < 10:
            total += 3
        return total


class GovernmentMelonOrder(AbstractMelonOrder):
    """Government melon order"""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        super(GovernmentMelonOrder, self).__init__(species, qty)
        self.order_type = "government"
        self.passed_inspection = False
        self.tax = 0.00

    def mark_inspection(self, did_pass):
        """Takes in True or False and updates passed_inspection variable with
        status"""

        self.passed_inspection = did_pass
