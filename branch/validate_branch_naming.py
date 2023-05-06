import os
import re
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

team_name_regex = re.compile(config.get('regex', 'team_name_regex'))
work_category_regex = re.compile(config.get('regex', 'work_category_regex'))
task_number_regex = re.compile(config.get('regex', 'task_number_regex'))
task_description_regex = re.compile(config.get('regex', 'task_description_regex'))

def validate_branch_name(branch_name):
    team_name, work_category, task_number, task_description = branch_name.split("/")

    # validate team name
    if not team_name_regex.match(team_name):
        return False

    # validate work category
    if not work_category_regex.match(work_category):
        return False

    # validate task number
    if not task_number_regex.match(task_number):
        return False

    # validate task description
    if not task_description_regex.match(task_description):
        return False

    return True

if __name__ == "__main__":
    branch_name = os.environ.get("CI_COMMIT_BRANCH")
    if branch_name:
        if validate_branch_name(branch_name):
            print(f"Branch name '{branch_name}' is valid")
        else:
            print(f"Branch name '{branch_name}' is invalid")
            exit(1)
    else:
        print("CI_COMMIT_BRANCH environment variable is not set")
        exit(1)

