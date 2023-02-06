import yaml
class CodingUnit:
    def __init__(self,coding,data):
        with open(coding) as stream:
            print(yaml.load(stream))

if __name__ == "__main__":
    CodingUnit("config.yml",None)

