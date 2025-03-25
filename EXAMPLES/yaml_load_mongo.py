from pprint import pprint
import yaml
try:
    from yaml import CLoader as Loader  # faster!
except ImportError:
    from yaml import Loader



with open('../DATA/mongo.yaml') as mongo_in:
    mongo_data = yaml.load(mongo_in, Loader=yaml.Loader)

pprint(mongo_data)


