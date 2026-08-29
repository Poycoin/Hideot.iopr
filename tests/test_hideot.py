from hideot import __version__, describe_project, repo_name


def test_describe_project_defaults():
    project = describe_project()

    assert project["name"] == "Hideot.iopr"
    assert project["status"] == "ready"
    assert project["summary"] == "Hideot.iopr is ready."
    assert __version__ == "0.1.0"


def test_repo_name_strips_whitespace():
    assert repo_name("  Hideot.iopr  ") == "Hideot.iopr"
    assert repo_name("") == "Hideot.iopr"
