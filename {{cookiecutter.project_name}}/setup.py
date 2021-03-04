import setuptools

setuptools.setup(
    name="{{cookiecutter.package_name}}",
    version="{{cookiecutter.version}}",
    author="{{cookiecutter.full_name}}",
    author_email="{{cookiecutter.email}}",
    description="{{cookiecutter.description}}",
    url="https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}",
    setup_requires=["setuptools_scm"],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
)
