# Organizing your project's files and folders

In development, the organization, naming, and placement of project
components is crucial to effective development. Knowing where to place
your project files, and how to name folders/directories
meaningfully will help you tremendously. See
[naming rules](naming-rules.md) for info on how to make useful names.

This page is going to talk about **folder** or **directory**
structure. You'll hear those two terms used interchangeably: they mean
the same things.

## Top-level Organization

In a typical system, there are often a few directories already
created for you, such as

```
./Desktop
./Documents
./Downloads
./Library
./Movies
./Music
./Pictures
./Public
```

(This is a set on Mac OS/X, you may have different ones depending on
the system you're using, but the points discussed here will be the
same.)

The starting "root" directory structure above can give us a clue as to
our next step. For my development stuff, I leave all that as is, and
create a few new top-level directories:

* Projects -- my personal projects, learning examples, and general
  stuff I do for development
* Sites -- web sites I'm working on. At least on the Mac, Sites is
  often also used for web sites local to the Mac. This generally
  shouldn't be a problem.
* Work -- client-associated projects

You might choose a different sorting of things, that's really up to
you. My example above is what works for me, at this writing. I've had
other folder organizations, too. It all depends. For GDI classes, a
good root folder could be `GDI_Classes` for example, with each course
below that, such as:

```
./GDI_Classes/
  Intro_to_HTML_and_CSS/
  Intro_to_JavaScript/
```

## Anatomy of a project

In a typical web site project, you'll often find a structure like
the following:

```
doggie_diner_brochure_site/
  css/
    reset.css
    styles.css
  js/
    main.js
    vendor/
      jquery.min.js
  img/
    logo.png
    doggies.jpg
  about.html
  index.html
  contact.html
```

The web site's root contains the index page, while all the other
parts of the site are in folders (aka directories). Folders can be
further broken into sub-folders, and so on.

The way you lay out your project benefits greatly from using top-down
design, modularity, and keeping components small. A balancing
factor to this is that you do not want your project structure to go
too deep, either, as this makes it harder to remember where things
are. Strike a useful balance; a good rule of thumb is never go more
than 3 levels down, e.g. `css/theme/components/`.
