from getv.main import run_shell_command, get_versions_list


def test_run_shell_command():
    res = run_shell_command('uname -a')
    assert res.returncode == 0


def test_get_version_list():
    v_list = get_versions_list()
    assert isinstance(v_list, list)
