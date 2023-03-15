import os
import re

def validate_pipeline_name(pipeline_name):
    # Rule 1: Start with repo name - eg security, data, ai, ml, etc
    # no more than 5 letters
    # no less than 2 letters
    # lowercase
    repo_name_regex = re.compile(r"^[a-z]{2,5}-")
    repo_name_match = repo_name_regex.match(pipeline_name)
    if not repo_name_match:
        return False

    # Rule 2: Follow repo name with clear description of what the pipeline does
    # no more than 6 words
    # no less than 2 words
    # Separate each word by a hyphen
    description_regex = re.compile(r"(-[a-z]+){2,6}$")
    description_match = description_regex.search(pipeline_name)
    if not description_match:
        return False

    return True

if __name__ == "__main__":
    example_pipeline_name = "ai-apply-sqlserver-cu"
    if validate_pipeline_name(example_pipeline_name):
        print(f"{example_pipeline_name} is a valid pipeline name")
        os.environ["CI_COMMIT_PIPELINE"] = example_pipeline_name
    else:
        print(f"{example_pipeline_name} is not a valid pipeline name")
        exit(1)


