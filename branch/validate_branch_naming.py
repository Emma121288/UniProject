import re

acronym_set = ['bacchus','atlas','echo', 'nyx']
category = ['feature', 'story', 'bug', 'spike'] 

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

    return True

# exmaple valid branch names
example_branch_name = "bacchus/feature/721023-D278ImplementnewFeature"
example_branch_name2 = "bacchus/feature/55325-AbcdefGhijklMnopqrs"

# exmaple invalid branch names
example_branch_name_breaking_convention = "bacchus12345/featuretobeimplemented/44324-abcdef"
example_branch_name_breaking_convention = "bacchus12345/featuretobeimplemented/44324-abcdef-ghijklmnop"

# validate script

if validate_branch_name(example_branch_name):
    print("Valid branch name")
else:
    print("Invalid branch name")

if validate_branch_name(example_branch_name2):
    print("Valid branch name")
else:
    print("Invalid branch name")

if validate_branch_name(example_branch_name_breaking_convention):
    print("Valid branch name")
else:
    print("Invalid branch name")
