import os
import re
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

acronym_set = config.get('branch', 'acronym_set').split(',')
category = config.get('branch', 'category').split(',')

def validate_branch_name(branch_name):
    branch_name_split = branch_name.split("/")
    if len(branch_name_split) != 3:
        return False

    team_name = branch_name_split[0]
    work_category = branch_name_split[1]
    task = branch_name_split[2].split("-")
    if len(task) != 2:
        return False

    task_number = task[0]
    task_description = task[1]

    #validate team name
    team_name_regex = re.compile(r"^[a-z]{3,12}$")
    team_name_match = team_name_regex.match(team_name)
    if not team_name_match:
        return False

    #validate work category
    work_category_regex = re.compile(r"^[a-z]{3,12}$")
    work_category_match = work_category_regex.match(work_category)
    if not work_category_match:
        return False

    #validate task number
    task_number_regex = re.compile(r"^[\d]{5,10}$")
    task_number_match = task_number_regex.match(task_number)
    if not task_number_match:
        return False

    #validate task description
    task_description_regex = re.compile(r"^[A-Z][a-zA-Z0-9]{3,24}$")
    task_description_match = task_description_regex.match(task_description)
    if not task_description_match:
        return False

    #validate branch name
    if work_category == 'feature':
        if task_description.lower() not in acronym_set:
            return False
    elif work_category in category:
        pass
    else:
        return False

    if branch_name == 'main':
        return True

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
