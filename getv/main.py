import os
import subprocess

GIT_COMMANDS = {
    "get_tag_list": "git tag -l",
}

PATH_TO_VIRTUAL_ENV = os.environ['VIRTUAL_ENV']

PROJECT_DIR = os.path.dirname(PATH_TO_VIRTUAL_ENV)


def run_shell_command(command, shell=True, stdout=subprocess.PIPE):
    result = subprocess.run(command, shell=shell, stdout=stdout)
    return result


def get_versions_list():
    git_tags_list = run_shell_command(GIT_COMMANDS["get_tag_list"])
    v_list = []
    for v in git_tags_list.stdout.decode('utf-8').splitlines():
        v_list.append(v)
    return v_list


def get_last_version():
    v_list = get_versions_list()
    if v_list:
        return v_list[-1]
    return "No versions yet!"


def write_or_create_version_file(path_to_dir, filename='version.txt'):
    last_v = get_last_version()
    with open(os.path.join(path_to_dir, filename), 'w') as f:
        f.write(last_v)


write_or_create_version_file(PROJECT_DIR)

if __name__ == '__main__':
    last_v = get_last_version()
    print("The last version is %s" % last_v)
