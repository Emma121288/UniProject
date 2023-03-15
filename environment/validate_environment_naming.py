import os
import re

def validate_environment_name(env_name):
    env_name_regex = re.compile(r"^[a-z]{2,5}-[0-9]{3}$")
    return bool(env_name_regex.match(env_name))

if __name__ == "__main__":
    os.environ["CI_COMMIT_ENVIRONMENT"] = "sec-001"
    env_name = os.environ.get("CI_COMMIT_ENVIRONMENT")
    if env_name:
        if validate_environment_name(env_name):
            print(f"Environment name '{env_name}' is valid")
        else:
            print(f"Environment name '{env_name}' is invalid")
            exit(1)
    else:
        print("CI_COMMIT_ENVIRONMENT environment variable is not set")
        exit(1)
        
# Example environment names
example_environment_name1 = "sec-001"
example_environment_name2 = "dev-002"
example_environment_name3 = "qa-001"

# print results
print(validate_environment_name(example_environment_name1))
print(validate_environment_name(example_environment_name2))
print(validate_environment_name3(example_environment_name3))
