class AbstractMelonOrder(object):
    """An abstract base class that other melon orders can inherit from."""

    def __init__(self, species, qty, order_type, tax):
        """Initialize melon order attributes for species, quanity, order type, tax, and shipped."""

        self.species = species
        self.qty = qty
        self.order_type = order_type
        self.tax = tax
        self.shipped = False

    def get_total(self):
        """Calculate total price of melon orders, including tax."""

        base_price = 5

        if self.species == "Christmas":
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == "international" and self.qty < 10:
            total += 3

        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17

    def get_country_code(self, country_code):
        """Return the country code."""

        self.country_code = country_code

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    """A US Government melon order."""

    order_type = "government"
    tax = 0.0
    passed_inspection = False

    def inspect_melons(self):
        """Updates passed_inspection to true."""

        self.passed_inspection = True
