import re

def validate_environment_name(env_name):
    env_name_regex = re.compile(r"^[a-z]{2,5}-[0-9]{3}$")
    return bool(env_name_regex.match(env_name))

example_environment_name = "sec-001"

if validate_environment_name(example_environment_name):
    print("Valid environment name")
else:
    print("Invalid environment name")
