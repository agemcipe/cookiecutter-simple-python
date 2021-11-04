if "{{cookiecutter.create_remote}}" == "yes":

    import subprocess

    print("--- Creating git repository ---")


    # check git version
    # make sure you have git version > 2.28.0 , see https://stackoverflow.com/questions/42871542/how-can-i-create-a-git-repository-with-the-default-branch-name-other-than-maste
    git_version_str = git_version_str = subprocess.check_output(["git", "--version"], text=True).strip()
    
    if git_version_str <= "git version 2.28.0":
        print(f"You need git version > 2.28.0 . Current: {git_version_str} . Update git to use create remote.")
        return 1 
    
    subprocess.call(
        ["git", "init", "-b", "main"]
    )      subprocess.call(["git", "add", "."])
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
