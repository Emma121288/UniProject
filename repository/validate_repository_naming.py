
import re
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

def validate_repo_name(repo_name):
    separator = config.get('repo_settings', 'separator')
    parts = repo_name.split(separator)
    
    if len(parts) != 2:
        return False
    
    area_regex = re.compile(config.get('repo_settings', 'area_regex'))
    area_match = area_regex.match(parts[0])
    if not area_match:
        return False
    
    indication_regex = re.compile(config.get('repo_settings', 'indication_regex'))
    indication_match = indication_regex.match(parts[1])
    if not indication_match:
        return False
    
    return True

# Example repo names
repo_name1 = "Security.Infrastructure"
repo_name2 = "Data.Config"
repo_name3 = "AI.PE"
repo_name4 = "Security.Data.Infrastructure"
repo_name5 = "Uni.Project"

# print results
print(validate_repo_name(repo_name1))
print(validate_repo_name(repo_name2))
print(validate_repo_name(repo_name3))
print(validate_repo_name(repo_name4))
print(validate_repo_name(repo_name5))
