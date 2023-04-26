import os
import re
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

acronym_set = set(config.get('settings', 'acronym_set').split(','))
category = set(config.get('settings', 'category').split(','))
team_name_regex = re.compile(config.get('regex', 'team_name_regex'))
work_category_regex = re.compile(config.get('regex', 'work_category_regex'))
task_number_regex = re.compile(config.get('regex', 'task_number_regex'))
task_description_regex = re.compile(config.get('regex', 'task_description_regex'))

def validate_branch_name(branch_name):
    if branch_name == 'main':
        return True

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

if __name__ == "__main__":
    example_branch_name = "bacchus/feature/721023-D278ImplementnewFeature"
    example_branch_name2 = "bacchus/feature/55325-AbcdefGhijklMnopqrs"
    example_branch_name_breaking_convention = "bacchus12345/featuretobeimplemented/44324-abcdef"
    example_branch_name_breaking_convention2 = "bacchus12345/featuretobeimplemented/44324-abcdef-ghijklmnop"

    # validate example branch names
    if validate_branch_name(example_branch_name):
        print(f"Branch name '{example_branch_name}' is valid")
    else:
        print(f"Branch name '{example_branch_name}' is invalid")

    if validate_branch_name(example_branch_name2):
        print(f"Branch name '{example_branch_name2}' is valid")
    else:
        print(f"Branch name '{example_branch_name2}' is invalid")

    # validate example invalid branch names
    if validate_branch_name(example_branch_name_breaking_convention):
        print(f"Branch name '{example_branch_name_breaking_convention}' is valid")
    else:
        print(f"Branch name '{example_branch_name_breaking_convention}' is invalid")

    if validate_branch_name(example_branch_name_breaking_convention2):
        print(f"Branch name '{example_branch_name_breaking_convention2}' is valid")
    else:
        print(f"Branch name '{example_branch_name_breaking_convention2}' is invalid")
