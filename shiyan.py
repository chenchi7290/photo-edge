
import yaml

with open(r"F:\4_PycharmProject\semi-utils-build1518\config.yaml", 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)
    print(data, type(data))
    for key,value in data.items():
        print(key,value,type(value))
        print("\n"*2)

print()
