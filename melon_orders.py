class AbstractMelonOrder(object):
    """A general melon order."""

    def __init__(self, species, qty, order_type, tax):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax

    def get_total(self):
        """Calculate price of melon orders."""

        base_price = 5

        if self.species == "Christmas":
            total = (1 + self.tax) * self.qty * (1.5 * base_price)
        else:
            total = (1 + self.tax) * self.qty * base_price

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

    def get_total(self):
        """Calculate price of international melon orders."""

        if self.qty < 10:
            total = 3 + super(InternationalMelonOrder, self).get_total()        
        else:
            total = super(InternationalMelonOrder, self).get_total()

        return total


class GovernmentMelonOrder(AbstractMelonOrder):
    """A US Government melon order."""

    order_type = "government"
    tax = 0.0
    passed_inspection = False

    def inspect_melons(self):
        """Updates passed_inspection to true."""

        self.passed_inspection = True

