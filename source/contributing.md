# Documentation Contributing Guide

We welcome contributions from all users and the community. By contributing, you agree to the [Percona Community code of conduct](https://percona.community/contribute/coc/). Thank you for deciding to contribute and helping us improve the [ProxySQL Admin Tool documentation](https://www.percona.com/doc/proxysql/index.html).

You can contribute to the documentation in either of the following ways:

- [Add a forum topic](#add-a-forum-topic)
- [Request a doc change with a Jira issue](#request-a-change-with-a-jira-issue)
- [Contribute to the documentation yourself](#contribute-to-documentation-yourself)

## Add a forum topic

In the [Percona Product Documentation category](https://forums.percona.com/c/percona-product-documentation/71) in the Percona Community Forum, select New Topic. Complete the form and select Create Topic to add the topic to the forum.![Create a topic](./_res/images/new-topic.png "Create a topic")

## Request a change with a Jira issue

If you would rather not [contribute to the documentation yourself](#contribute-to-documentation-yourself) let us know about the issue by adding a Jira ticket. Use the following procedure to create a Jira ticket:

![Submit DOC bug](_images/submit-doc-bug.png)

- Select the **Submit DOC bug** link on the sidebar. This action opens the [Jira issue tracker](https://jira.percona.com/projects/PSQLADM/issues) for the doc project.

- Log in (create a Jira account if you don't have one) and select **Create** to open the Jira form.
  
![Complete the Jira form](_images/add-jira.png)

- In the following fields, describe the issue:

  - In the Summary, provide a brief description of the issue.

  - In the Description, provide more information about the issue. If needed, add a Steps To Reproduce section and information about your environment (version number, your operating system, etc.).
  
  - Select **CREATE** to create the ticket.

## Contribute to documentation yourself

In the sidebar, there is a **This Page** section. The **Edit in GitHub** link opens the source file of the page on GitHub. You make the changes, and merge your pull request into the documentation.

Before you contribute, please learn about the following technologies used to create our ProxySQL Admin tool documentation:

- [reStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html) (reST) markup language. This is the format used to write the documentation.
  
- [Sphinx](https://www.sphinx-doc.org/en/master/usage/quickstart.html) (reST) documentation generator used to convert the source `.rst` files to HTML or PDF documents.
  
- [git](https://git-scm.com/)
  
- [Docker](https://docs.docker.com/get-docker/). This tool lets you run Sphinx in a virtual environment.

Currently, the ProxySQL Admin Tool documentation is built using the **main** branch. All reStructuredText files or `.rst` files are stored in the `/source` directory.

### Edit documentation online with GitHub

Select the **Edit in GitHub** link on the sidebar. The source `.rst` file of the page opens in a GitHub editor in your browser. If you haven't worked with the repository before, GitHub creates a [fork](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo).

Edit the page. You should review your changes on the **Preview** tab.

  **NOTE**: GitHub's native markup language is [Markdown](https://daringfireball.net/projects/markdown/). GitHub's Markdown renders titles, headings, and lists correctly but does not render RestructuredText-specific elements such as directives or the variable class.

Commit your changes. 

In the **Commit changes** section, add the following:

  - Brief summary (72 characters or less) of what was changed
  
Then select the **Create a new branch for this commit and start a pull request** option. Accept the name for the branch and then Select **Commit changes**.

GitHub creates a branch and a commit for your changes. It loads a new page on which you can submit a pull request to Percona. The page shows the base branch - the one you offer your changes for, your commit message and a diff - a visual representation of your changes against the original page. At this time you can make a last-minute review. When you are ready, click the **Create pull request** button.

A core developer reviews the pull request for accuracy and merges your pull request into the repository, if everything is correct. The documentation  gets published on the site at the next release.

**NOTE**: The pull request may be redone to meet internal requirements, for example, aligning the Percona branch to the upstream branch.

### Edit documentation locally

This option is for users who prefer to work from their computer and/or have the full control over the documentation process.

The steps are the following:

1. Fork this repository

2. Clone the forked repository to your machine:

    ```bash
    git clone git@github.com:<your_name>/proxysql-admin-tool-doc.git
    cd <directory name>/proxysql-admin-tool-doc
    ```

3. Add the remote origin repository:

    ```sh
    git remote add origin 
    https://github.com/percona/proxysql-admin-tool-doc.git
    ```

4. Checkout the appropriate branch and pull the latest changes from origin

    ```sh
    git checkout main && git pull origin main
    ```

5. Create a separate branch for your changes

    ```sh
    git checkout -b <my_changes>
    ```

6. Do your work. Add code examples, if necessary. We recommend that you build an HTML file, either [on your machine](#Installing-Sphinx-and-building-locally) or [using Docker](#Using-Docker) to view your changes. You can run the command to `make clean html` to see the latest changes. If you have questions on formatting, use a [cheat sheet](https://sphinx-tutorial.readthedocs.io/cheatsheet/?highlight=-b#rst-cheat-sheet).

7. Add the changed files.

    ```sh
    git add <changed files>
    ```

8. Commit your changes

    ```sh
    git commit -m 'Fixed typing error in <document name>'
    ```

9. Open a pull request to Percona

    ```sh
    git push <my repo> <my_changes>
    ```

### Building the documentation

To verify how your changes look, generate the static site with the documentation. This process is called _building_. You can use the following methods:

- [Use Docker](#use-docker)
- [Install Sphinx and build locally](#install-sphinx-and-build-locally)

#### Using Docker

1. [Get Docker](https://docs.docker.com/get-docker/)
2. We use [this Docker image](https://hub.docker.com/r/ddidier/sphinx-doc) to build documentation. Run the following command:

    ```
    docker run --rm -i -v `pwd`:/doc -e USER_ID=$UID ddidier/sphinx-doc:0.9.0 make clean html
    ```

If Docker can't find the image locally, it first downloads the image, and then runs it to build the documentation.

1. Go to the `doc/build/html` directory and open the `index.html` file to see the documentation.
2. Your static site will look different from the one on the web site. We use a Percona theme that is rendered when the documentation is published to the website. You can add the following [sphinx-doc options](https://www.sphinx-doc.org/en/master/man/sphinx-build.html) to view the documentation with the [Alabaster](https://alabaster.readthedocs.io/en/latest/) theme

  - `-b` selects the builder. This example uses HTML.
  - `-D` overrides a selection in conf.py. The example phrase changes the html_theme to `alabaster`.

    The following example creates a HTML build with the Alabaster theme.

    ```sh
    docker run --rm -i -v `pwd`:/doc -e USER_ID=$UID ddidier/sphinx-doc:0.9.0 sphinx-build -b html -D 'html_theme=alabaster' source build/html
    ```

3. To create a PDF version of the documentation, run the following command:

    ```sh
    docker run -i -v `pwd`:/doc -e USER_ID=$UID ddidier/sphinx-doc:0.9.0 make clean latex && docker run -i -v `pwd`:/doc -e USER_ID=$UID ddidier/sphinx-doc:0.9.0 make clean latexpdf
    ```

The PDF document is in the `doc/build/latex` folder.

#### Installing Sphinx and building locally

1. Install [pip](https://pip.pypa.io/en/stable/installing/)
2. Install [Sphinx](https://www.sphinx-doc.org/en/master/usage/installation.html).
3. In the root directory of the doc project (which is **proxysql-admin-tool-doc** directory for this project), build the HTML files with the following command:

    ```sh
    make clean html
    ```

This command does two tasks. The `clean` command rebuilds the `/build` directory. The `html` command creates HTML files in the `/build/html` directory.

1. Go to the `doc/build/html` directory and open the `index.html` file to review the table of contents.

2. Your static site will look different from the Percona Documentation web site. When we publish to that web site, we use a Percona theme. You can add the [Alabaster](https://alabaster.readthedocs.io/en/latest/) theme when you build the HTML files:

    ```sh
    sphinx-build -b html -D 'html_theme=alabaster' source build/html
    ```

3. To create a PDF version of the documentation, run the following command:

    ```sh
    make clean latexpdf
    ```

This command does two tasks. The `clean` command rebuilds the `/build` directory. The `latexpdf` commands creates a PDF document in the `/build/latex` directory.

