# Starting Up a New Project

A common set of steps to create a new project to work on. This is intended for students in the [GDI](https://gdiminneapolis.com) [Front-End Cohort](http://gdiminneapolis.com/front-end-developer-series/). *Don't be shy, Develop it!*

## Assumptions

This is a small web-site project, consisting only of HTML, CSS, and enough JavaScript to have things work. Building a JavaScript application or a server-side application will be a bit more complex, but the essentials are still the same as described here, just possibly using different tools.

## Caveat

The steps presented here are *all* performed in a Terminal, on the Command line. On a Mac, press `CMD-SPACE` and type `terminal` (spotlight will show you the Terminal command long before you finish typing; you just need to type enough to get it to recognize what you're doing.) On Windows, run the `Git Bash` program you installed in the "Intro to Git" class.

## If you do not have a place for your projects, make one

You might want to have all your projects organized under the same directory on your system. A directory called "Projects" or "Develoment" are good choices, but if you think of something better, use it.

For more detail on this topic, see [Organizing Your Projects](organizaing-your-projects.md).

For the purposes of this discussion, I'm assuming you have a
`Projects` directory in your home directory.

## Start in your working projects directory

Change directories to your working projects directory:

    cd ~/Projects

## Decide on a project name

Think of a good name for your project so that you'll remember where it is. Avoid using spaces, instead use dashes or underscores. See [Naming Rules](naming-rules.md).

| Bad | Good |
|:--------------:|:--------------:|
| `My Simple Project` | `my_simple_project` |
| `Hello (Can You Hear Me?)` | `hello-can-you-hear-me` |
| `$$$ PROFIT!!!` | `profit` |

Let's give your project the name of `doggie_diner_brochure_site`.

## Create the project directory **and** the Git repository at once:

    git init doggie_diner_brochure_site

## Change into the project directory:

    cd doggie_diner_brochure_site

## Create a project readme file:

    echo 'The Doggie Diner Brochure Web Site Project' > README.md

## Create a `.gitignore` file:

    touch .gitignore

## Commit the initial project:

    git add --all -v
    git commit -m "Initial Commit"
    git status

# Conclusion

If you start every project this way, you'll have a good uniform set of projects and practice using Git. Soon this will become muscle memory.

It probably feels odd to rely more heavily on the command line than to use GUI desktop tools. The more you use the command line, the more you'll find it easier to use.

# This is a log of an example using the above steps:

``` bash
$ cd
$ mkdir -p Projects
$ cd ~/Projects
$ git init doggie_diner_brochure_site
Initialized empty Git repository in /Users/tamara/Projects/doggie_diner_brochure_site/.git/
$ cd doggie_diner_brochure_site
$ echo 'The Doggie Diner Brochure Web Site Project' > README.md
$ touch .gitignore
$ git add --all -v
add '.gitignore'
add 'README.md'
$ git commit -m "Initial Commit"
[master (root-commit) de80613] Initial Commit
 2 files changed, 1 insertion(+)
 create mode 100644 .gitignore
 create mode 100644 README.md
$ git status
On branch master
nothing to commit, working directory clean
```

You may also want to look at
[setting up your remote repository](setting-up-your-remote.md).
