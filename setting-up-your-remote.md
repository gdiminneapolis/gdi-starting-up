# Setting up your remote repository

At the time I'm writing this, there are two really well-known web
services for people to use as a remote repository:

* [Github](https://github.com)
* [Bitbucket](https://bitbucket.com)

They are nearly identical in the service they offer, with bitbucket
offering free private repositories. With Github, you have to pay for
private repositories.

Either service you use, you'll need to follow the instructions on that
site to create a remote repository. When you've done that, you'll be
given an identifier for the remote that you'll need to make note
of. The remote identifier will look something like this:

* `git@github.com:gdiminneapolis/doggie_diner_brochure_site.git`
* `git@bitbucket.org:tamouse/small-other-project.git`

## Setting the remote origin

Back on your own computer, head back to your project's working
directory:

    cd ~/Projects/doggie_diner_brochure_site

Enter the following command to set the remote origin:

    git remote add origin git@github.com:gdiminneapolis/doggie_diner_brochure_site.git

(Assuming that's the remote repository name.)

## First push

Now you can push the current tip of your working branch out to the
remote repo:

    git push -u origin HEAD

The `-u` option tells git to link the local branch to the remote
branch. Subsequently you'll be able to just type:

    git push
