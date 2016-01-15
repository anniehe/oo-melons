class AbstractMelonOrder(object):
    """A general melon order."""

    def __init__(self, species, qty, order_type, tax):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = None
        self.tax = 0

        # GOOD MORNING BEAUTIFUL
        # TODO: Part two
        # calc xmas melon price
        # calc internation order for <10 melons

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

    def __init__(self, species, qty):
        """Initialize domestic melon order attributes"""

        super(DomesticMelonOrder, self).__init__(species, qty, "domestic", 0.08)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty):
        """Initialize international melon order attributes"""

        super(InternationalMelonOrder, self).__init__(species, qty, "international", 0.17)

    def get_total(self):
        """Calculate price of international melon orders."""

        base_price = 5

        if self.qty < 10:
            total = 3 + ((1 + self.tax) * self.qty * base_price)
        else:
            total = (1 + self.tax) * self.qty * base_price

        return total

    def get_country_code(self, country_code):
        """Return the country code."""

        self.country_code = country_code

        return self.country_code
