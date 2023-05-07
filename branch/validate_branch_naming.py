import os
import re
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

#regular expressions from config.ini
acronym_set = set(config.get('settings', 'acronym_set').split(','))
category = set(config.get('settings', 'category').split(','))
team_name_regex = re.compile(config.get('regex', 'team_name_regex'))
work_category_regex = re.compile(config.get('regex', 'work_category_regex'))
task_number_regex = re.compile(config.get('regex', 'task_number_regex'))
task_description_regex = re.compile(config.get('regex', 'task_description_regex'))

#define validate branch function
def validate_branch_name(branch_name):
    if branch_name == 'main':
        return True

    branch_name_split = branch_name.split("-")
    num_parts = len(branch_name_split)
    if num_parts != 3:
        return False

    team_name = branch_name_split[0]
    work_category = branch_name_split[1]
    task_number = ""
    task_description = ""

    if num_parts == 3:
        task_parts = branch_name_split[2].split("/")
        if len(task_parts) != 2:
            return False
        task_number, task_description = task_parts

    # validate team name
    team_name_match = team_name_regex.match(team_name)
    if not team_name_match:
        return False

    # validate work category
    work_category_match = work_category_regex.match(work_category)
    if not work_category_match:
        return False

    # validate task number
    task_number_match = task_number_regex.match(task_number)
    if not task_number_match:
        return False

    # validate task description
    task_description_match = task_description_regex.match(task_description)
    if not task_description_match:
        return False

    # validate branch name
    if work_category in category:
        pass
    else:
        return False

    return True

#set environment variable and validate if the branch name meets conventions
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

