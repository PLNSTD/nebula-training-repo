# Lecture: Setting Up and Using Git & GitHub in Python Development

## Objectives
- Configure Git for local development.
- Understand the difference between local and remote repositories.
- Clone the example Python project repository.
- Learn the basic Git commands: `init`, `add`, `commit`, `push`, `pull`.
- Understand the use of branching and pull requests in GitHub.

## Git and GitHub: Understanding Their Roles

- **Git**: A version control system that helps manage the history of your software project. It enables you to track changes, revert to previous stages, and handle project versions effectively.
- **Usage**: Primarily used through a Bash CLI (Command Line Interface).
- **GitHub**: A cloud-based hosting service that works with Git. It's where your Git-tracked projects, known as repositories, live. It's an industry standard for collaboration, allowing visibility and synchronization of project changes.
- **Integration**: Git is used locally on your computer, while GitHub is used to host your Git repositories online. It would help if you synced local changes with GitHub to ensure consistency and collaboration.

- **Videos for Better Understanding**:
  - [What is GitHub?](https://www.youtube.com/watch?v=w3jLJU7DT5E&ab_channel=GitHub)
  - [Why GitHub Matters as a Developer](https://www.youtube.com/watch?v=yaRwYYdiHxo&ab_channel=SimpleProgrammer)

## Configuring Git Locally

Before using Git, you need to configure it with your details. It would help if you did this now, as you cannot commit to a repository without doing it.

- **Setting Up**:
  - Your Git configuration should match your GitHub account details.
  - Use these commands in your CLI (Terminal / Git Bash):
    - `git config --global user.name "Your Name"`
    - `git config --global user.email youremail@example.com`

## Git / GitHub Workflow: A Visual Guide

The workflow in Git and GitHub can be understood through this visual representation. It shows how changes are made locally and then pushed to a central remote repository on GitHub. This workflow will be our standard workflow, especially during group projects.

![Git/GitHub Workflow](https://www.codeproject.com/KB/applications/1165512/image1.png)

## Branching and Pull Requests in GitHub

- **Branching**: Allows you to diverge from the main line of development and continue to work independently without affecting the main line. For example, creating a branch for a new feature in a Python project.
- **Creating a Branch**: Use `git branch [branch-name]`.
- **Switching Branches**: Use `git checkout [branch-name]`.
- **Pull Requests**: After pushing your branch to GitHub, you can open a pull request. This is a request to merge your changes into the main branch, usually followed by code review and discussion.
- **Merging**: Once a pull request is approved, it can be merged into the main branch, incorporating your changes into the project.

## Cloning the Python Project Repository

We'll begin with what I'll refer to as our "Python Project Repository". We will clone this repository and regularly update our local copy with new changes.

- **Cloning a Repository**:
  - Use the URL provided by the instructor: `https://github.com/YourPythonProject/Repository.git` (Note: Replace with the actual URL).
  - In your CLI, navigate to the desired directory and use:
    - `git clone https://github.com/YourPythonProject/Repository.git`
  - Explore the cloned repository to familiarize yourself with its contents.

## Essential Git Commands

These commands are the backbone of your day-to-day interaction with Git and GitHub.

- **Checking Repository Status**:
  - `git status`: Shows the state of your working directory and staging area.
- **Initializing a New Repository**:
  - `git init`: Converts a directory into a Git repository.
- **Staging Changes**:
  - `git add .`: Stages all your changes for the next commit.
- **Committing Changes**:
  - `git commit -m 'Description of changes'`: Securely stores your staged changes as a new version in the repository.
- **Pushing Changes to GitHub**:
  - `git push`: Uploads your local commits to the remote repository on GitHub.
- **Pulling Latest Changes**:
  - `git pull`: Fetches and merges changes from the remote repository to your local repository.

## Conclusion and Resources

Today's lecture covered the basics of setting up and using Git and GitHub in Python development, emphasizing branching and pull requests. These tools are essential for effective version control and collaboration in software projects.

- **Further Learning Resources**:
  - [Git Documentation](https://git-scm.com/doc)
  - [GitHub Learning Lab](https://lab.github.com/)