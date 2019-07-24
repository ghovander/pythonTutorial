from ecommerce.customer import contact  # absolute import
# from ..customer import contact # relative import

print("Sales Initialized", __name__)


def calc_tax():
    pass


def calc_shipping():
    pass


if __name__ == "__main__":  # __name__ is main if module is entry point for program
    print("Sales started")
    calc_tax()
