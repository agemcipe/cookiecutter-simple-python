if "{{cookiecutter.create_remote}}" == "yes":

    import subprocess

    print("--- Creating git repository ---")
    subprocess.call(
        ["git", "init", "-b", "main"]
    )  # make sure you have git version > 2.28.0 , see https://stackoverflow.com/questions/42871542/how-can-i-create-a-git-repository-with-the-default-branch-name-other-than-maste
    subprocess.call(["git", "add", "."])
    subprocess.call(["git", "commit", "-m", "Initial commit"])

    subprocess.call(
        [
            "gh",
            "repo",
            "create",
            "{{cookiecutter.github_user}}/{{cookiecutter.project_name}}",
            "--description",
            "{{cookiecutter.description}}",
            "--confirm",  # skip confirmation
        ]
    )
    subprocess.call(["git", "remote", "-v"])
    subprocess.call(["git", "push", "--set-upstream", "origin", "main"])
