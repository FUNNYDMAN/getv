def test_run_shell_command(get_v):
    res = get_v.run_shell_command('uname -a')
    assert res.returncode == 0


def test_get_version_list(get_v):
    v_list = get_v.get_versions_list()
    assert isinstance(v_list, list)


def test_get_last_version(get_v):
    version_list = ['0.0.1', '0.0.2', '0.0.3']
    last_v = get_v.get_last_version(version_list)
    assert last_v == version_list[-1]


def test_write_or_create_version_file(get_v, tmpdir):
    path_to_file = tmpdir.mkdir("sub").join("version.txt")
    get_v.write_or_create_version_file(path_to_file)
    assert path_to_file.read() == "No versions yet!"
