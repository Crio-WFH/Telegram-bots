## Contribution Guidelines

#### DISCLAIMER

    1. Do not touch any other files (Add/Update/Delete) in any of the repositories in the parent branch.
    2. Any type of changes should be carried out only from your local machine or personal github account. 
    3. Do not touch the following file(s)/folder(s) 
        - readme.md (Inside the repository. Your project specific readme is different.) 
        - .all-contributors-src
        - CONTRIBUTING.md - For your reference 
        - .github folder

#### How can you contribute to Crio Open Source in #IBelieveinDoing Remote Working Tools Edition?

`As a developer who can enhance the experience of the troubled WFH individual. :P`


Kindly refer the [getting started guide](https://docs.google.com/document/d/1z5cJHJkuhkMkWyAPTD7seIzH04MhD0dwNkEC6BvQwFk/edit) which will help gather ideas.

### Note for PR Proposals

Kindly utilise the template provided in the `.github` directory of the main branch to create relative PRs. You can also go adventurous if you have something fun in your mind, but kindly maintain a similar workflow by taking the already available templates as a reference.

For proposing a PR with a new piece of software, utilise PR template `pull_request_template.md` using GitHub API.

Kindly refer the [Submission Guidelines Document](https://docs.google.com/document/d/1DXgKki3EcEEb-99Oqyyq0WLItTBhXj3aZ1swtKkwg6U/edit) for detailed instructions regarding submission via GitHub UI. Note that you also have a demo video inside the document to assist you through the process.

### Instructions regarding traditional workflow

**</> Git Workflow </>**

```bash
## It all starts with forking the repository

## Clone the repo
$ git clone https://github.com/<User-Name>/<Repo-Name>.git
# - OR -
$ git clone git@github.com:<User-Name>/<Repo-Name>.git

## Add upstream remote
$ git remote add upstream https://github.com/Crio-WFH/Telegram-bots.git
# - OR -
$ git remote add upstream git@github.com:Crio-WFH/Telegram-bots.git

## Syncing with upstream/main branch
$ git fetch upstream
$ git checkout main
$ git merge upstream/main

## To create and shift to working branch
$ git checkout -b <github-username>/<project-name|issue>/{<add|update|additional-fixes>}
## Example: $ git checkout -b Ak-Shaw/my-lambda-function/add

## Types of additional-fixes:
# wip - Work in Progress; long term work; mainstream changes
# feat - New Feature; future planned; non-mainstream changes
# bug - Bug Fixes
# exp - Experimental; random experiemntal features

## Ensure branch
$ git branch

## Wildcard to add all folder and file changes in current branch
$ git add --all .

# Committing all changes with appropriate commit message and description
$ git commit -m "your-commit-message" -m "your-commit-description"

## To publish working branch to your forked repository
$ git push origin <branch-name>

## Creating the PR using GitHub UI
# Create Pull Request from the working branch in your forked repository to the master branch in the upstream repository
# Link Pull Request to appropriate Issue, or Project+Milestone (if no issue created)
# IMPORTANT: Do Not Merge the PR unless specifically asked to by an admin or approved by at least 2-3 maintainers.
# NOTE: Contributors who are among maintainers and/or collaborators have merge permissions.

```



**</> After PR Merge/Close </>**

```bash
## Syncing with upstream/main branch
$ git fetch upstream
$ git checkout main
$ git merge upstream/main

## Deleting the branch in local repository
# If PR is merged
$ git branch -d <branch-name>  
# If PR is closed/rejected
$ git branch -D <branch-name>  

## Deleting the branch in remote repository
$ git push origin --delete <branch-name>




#### References:

- [Fork a repo](https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/fork-a-repo)

- [About forks](https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/about-forks)
- [Fork-And-Branch workflow](https://blog.scottlowe.org/2015/01/27/using-fork-branch-git-workflow/)

- [Commit message standards](https://chris.beams.io/posts/git-commit/)
- [Configuring a remote for a fork](https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/configuring-a-remote-for-a-fork)
- [Syncing a fork](https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/syncing-a-fork)
