import re
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

repo_name_regex = re.compile(config.get('pipeline_naming', 'repo_name_regex'))
description_regex = re.compile(config.get('pipeline_naming', 'description_regex'))

def validate_pipeline_name(pipeline_name):
    repo_name_match = repo_name_regex.match(pipeline_name)
    if not repo_name_match:
        return False
    
    description_match = description_regex.search(pipeline_name)
    if not description_match:
        return False

    return True

if __name__ == "__main__":
    pipeline_name_1 = "ai-apply-sqlserver-cu"
    pipeline_name_2 = "qa-testing"
    pipeline_name_3 = "New-pipeline123"
    pipeline_name_4 = "TeamQA-pipeline/321"
    if validate_pipeline_name(pipeline_name):
        print(f"{pipeline_name_1} is a valid pipeline name")
        print(f"{pipeline_name_2} is a valid pipeline name")
        print(f"{pipeline_name_3} is a valid pipeline name")
        print(f"{pipeline_name_4} is a valid pipeline name")
    else:
        print(f"{pipeline_name_1} is not a valid pipeline name")
        print(f"{pipeline_name_2} is not a valid pipeline name")
        print(f"{pipeline_name_3} is not a valid pipeline name")
        print(f"{pipeline_name_4} is not a valid pipeline name")


