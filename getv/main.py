import subprocess


class GetVersion:
    GIT_COMMANDS = {
        "get_tag_list": "git tag -l",
    }

    @staticmethod
    def run_shell_command(command, shell=True, stdout=subprocess.PIPE):
        result = subprocess.run(command, shell=shell, stdout=stdout)
        return result

    def get_versions_list(self):
        git_tags_list = self.run_shell_command(__class__.GIT_COMMANDS["get_tag_list"])
        v_list = []
        for v in git_tags_list.stdout.decode('utf-8').splitlines():
            v_list.append(v)
        return v_list

    def get_last_version(self, v_list=None):
        if v_list is None:
            v_list = self.get_versions_list()
        return v_list[-1] if v_list else "No versions yet!"

    def write_or_create_version_file(self, path_to_file):
        last_v = self.get_last_version()
        with open(path_to_file, 'w') as f:
            f.write(last_v)


if __name__ == '__main__':
    getv = GetVersion()
    # return all version list
    list_versions = getv.get_versions_list()
    print("Version list %s" % list_versions)
