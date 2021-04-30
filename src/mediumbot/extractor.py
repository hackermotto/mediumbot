import json
import yaml
import configparser
import xml.etree.ElementTree as etree


class DataExtractorBase:
    def __init__(self, *args, **kwargs):
        self.data = dict()

    @property
    def parsed_data(self):
        return self.data


class YAMLDataExtractor(DataExtractorBase):
    """YAML Data Extractor"""

    def __init__(self, filepath):
        self.data = dict()

        with open(filepath, mode="r", encoding="utf-8") as f:
            self.data = yaml.load(f, Loader=yaml.Loader)


class JSONDataExtractor(DataExtractorBase):
    """JSON Data Extractor"""

    def __init__(self, filepath):
        self.data = dict()

        with open(filepath, mode="r", encoding="utf-8") as f:
            self.data = json.load(f)


class ConfigDataExtractor(DataExtractorBase):
    """Config Data Extractor"""

    def __init__(self, filepath):
        self.data = dict()

        config = configparser.ConfigParser(allow_no_value=True)
        with open(filepath, mode="r", encoding="utf-8") as f:
            config.read_string(f.read())
            self.data = config


class XMLDataExtractor:
    """XML Data Extractor"""

    def __init__(self, filepath):
        self.etree = etree.parse(filepath)

    @property
    def parsed_data(self):
        return self.etree


class PYDataExtractor(DataExtractorBase):
    """JSON Data Extractor"""

    def __init__(self, filepath):
        self.data = dict()

        with open(filepath, mode="r", encoding="utf-8") as f:
            self.data = exec(f.read())


def dataextraction_factory(filepath):
    if filepath.endswith("yaml"):
        extractor = YAMLDataExtractor
    elif filepath.endswith("xml"):
        extractor = XMLDataExtractor
    elif filepath.endswith("json"):
        extractor = JSONDataExtractor
    elif filepath.endswith("ini"):
        extractor = ConfigDataExtractor
    elif filepath.endswith("conf"):
        extractor = ConfigDataExtractor
    elif filepath.endswith("py"):
        extractor = PYDataExtractor
    else:
        raise ValueError("Cannot extract data from {}".format(filepath))

    return extractor(filepath)


def extract_data_from(filepath):
    factory_obj = None
    try:
        factory_obj = dataextraction_factory(filepath)
    except ValueError as e:
        print(e)
    return factory_obj
