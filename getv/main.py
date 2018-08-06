import subprocess

GIT_COMMANDS = {
    "get_tag_list": "git tag -l",
}


def run_shell_commad(command, shell=True, stdout=subprocess.PIPE):
    result = subprocess.run(command, shell=shell, stdout=stdout)
    return result


def get_versions_list():
    git_tags_list = run_shell_commad(GIT_COMMANDS["get_tag_list"])
    v_list = []
    for v in git_tags_list.stdout.decode('utf-8').splitlines():
        v_list.append(v)
    return v_list


def get_last_version():
    last_v = get_versions_list()
    if last_v:
        return last_v[-1]
    return "No versions yet!"


if __name__ == '__main__':
    last_v = get_last_version()
    print("The last version is %s" % last_v)
