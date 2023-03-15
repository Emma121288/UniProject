import os
import re
# from configparser import ConfigParser

def validate_repo_name(repo_name):
    # split the repo name into two parts: the area of the company and the description of what the repo is for
    parts = repo_name.split(".")
    
    # check if the repo_name consists of the two parts specified in the description
    if len(parts) != 2:
        return False
    # validate first part: the area of the company
    area_regex = re.compile(r"^[A-Z][a-zA-Z]{1,15}$")
    area_match = area_regex.match(parts[0])
    if not area_match:
        return False
    
    # validate second part: the description of what the repo is for
    indication_regex = re.compile(r"^[A-Z][a-zA-Z]{1,15}$")
    indication_match = indication_regex.match(parts[1])
    if not indication_match:
        return False
    
    return True

if __name__ == "__main__":
    repo_name = os.environ.get("CI_COMMIT_REPO")
    if repo_name:
        if validate_repo_name(repo_name):
            print(f"Repo name '{repo_name}' is valid")
        else:
            print(f"Repo name '{repo_name}' is invalid")
            exit(1)
    else:
        print("CI_COMMIT_REPO environment variable is not set")
        exit(1)

# Example repo names
repo_name1 = "Security.Infrastructure"
repo_name2 = "Data.Config"
repo_name3= "AI.PE"
repo_name4 = "Security.Data.Infrastructure"

# print results
print(validate_repo_name(repo_name1))
print(validate_repo_name(repo_name2))
print(validate_repo_name(repo_name3))
print(validate_repo_name(repo_name4))
