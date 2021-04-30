from mediumbot.extractor import extract_data_from


class basicConfig:

    def __init__(self, file, *args, **kwargs):
        pass

    def fileConfig(self, file):
        try:
            config = extract_data_from(file)

            for key, value in config.parsed_data.items():
                if hasattr(self, key):
                    setattr(self, key, value)
        except:
            raise ValueError("Can't load configuration from path '{}'".format(file))

    def kwargsConfig(self):
        pass