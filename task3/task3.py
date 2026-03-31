## Task 3
import sys
import json


def update(tests):
    for test in tests:
    
        if "value" in test.keys() and test["id"] in values.keys():
            test["value"] = values[test["id"]]
            
        if "values" in test.keys():
            test["values"] = update(test["values"])
            
    return tests


if __name__ == "__main__":
    
    dcd = json.JSONDecoder()

    with open(sys.argv[1]) as f:
        values = dcd.decode(f.read())
        values = dict((v["id"], v["value"]) for v in values["values"])
        
    with open(sys.argv[2]) as f:
        tests = dcd.decode(f.read())

    with open(sys.argv[3], "w") as f:
        json.dump(update(tests["tests"]), f, indent=2)