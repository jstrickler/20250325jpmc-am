from pprint import pprint
import yaml
try:
    from yaml import CLoader as Loader  # faster!
except ImportError:
    from yaml import Loader


with open('../DATA/invoice.yaml') as invoice_in:
    invoice_data = yaml.load(invoice_in, Loader=Loader)

pprint(invoice_data)


