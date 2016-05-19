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
    project_files/
      .git/
      index.html
      stylesheets/
        reset.css
        styles.css
  Intro_to_JavaScript/
    ...
```

## Anatomy of a project

There are many, many ways to organize a project. Starting off, you
want to keep it pretty simple.

The real point being that you can and should organize your projects in
the best way for what you are creating.

The first structure under
"Anatomy of a project" is great for primarily content-based HTML and
CSS sites, the next two are focused on JavaScript-driven
applications and reflect the modular component-based architecture. The
last one is a specialized web site built using a tool called Jekyll.

### Typical simple web site

In a typical web site project, you'll often find a structure like
the following:

```
doggie_diner_brochure_site/
  .git/
  .gitignore
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
  package.json
  README.md
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

The structure shown above is *only* typical. There are an infinite
number of ways a project can be structured. The *key* takeaway is that
it *is* structured, and that structure should help keep your project
work organized.

There are three main divisions or types of things to organize:

* Content -- your HTML files, generally
* Assets -- non-HTML, including your CSS, JavaScript, Images, Fonts,
  and so on
* Non-published information -- READMEs, meta-project information (such
  as is `package.json`), other "dot-files" possibly.

The simple structure shown above will work really well for the
projects we're doing in GDI classes and will work really well for you
to practice the new things you're learning.

By contrast, a more involved project, that includes a bunch of
JavaScript and other Assets would have a deeper structure.

### Small Javascript site

Here's a recent small example of a completely JavaScript-driven web
site project:

```
tiny_web_app/
  .git/
  .gitignore
  README.md
  package.json
  src/
    app.js
    app.styl
    layout.js
    nav_helper.js
    pages/
      public.js
      repos.js
    router.js
  webpack.config.js
```

### An Angular 2 site

And this is a beginning Angular 2 application structure:

```
ng-static-blog/
  .git/
  .gitignore
  Gulpfile.js
  README.md
  client/
    app/
      app.directive.js
      app.html
      app.js
      app.styl
      components/
        admin/
          admin.controller.js
          admin.directive.js
          admin.html
          admin.js
          admin.spec.js
          admin.styl
        blog/
          blog.controller.js
          blog.directive.js
          blog.html
          blog.js
          blog.spec.js
          blog.styl
        blogPost/ ... same as above
        common/ ... same as above
        components.js
        home/ ... same as above
      shared/
        api.js
        posts.js
        shared.js
    images/
      cat.jpeg
    index.html
    styles/
      colors.styl
      index.styl
      mixins.styl
      sizes.styl
  db.json
  dist/ * (generated by site build)
  karma.conf.js
  node_modules/ * (generated by npm install)
  package.json
  spec.bundle.js
  templates/
    component/
      component.controller.js
      component.directive.js
      component.html
      component.js
      component.spec.js
      component.styl
  webpack.config.js
```

### A Jekyll-based static web site

[Jekyll](http://jekyllrb.com) is a static site generator that's
helpful to build a multi-page content-based web site (such as a blog
or informational site), and so has it's own structure:

```
www.tamouse.org/
  .git/
  .gitignore
  .idea/ * (editor configuration files)
  .sass-cache/ * (generated by building site)
  .setup.sh
  404.html
  _baseurl.yml
  _config.yml
  _data/
    boxes.yml
  _layouts/
    default.html
  _site/ * (generated site -- build output location)
  apple-touch-icon.png
  browserconfig.xml
  crossdomain.xml
  css/
    animate.min.css
    bootstrap-theme.css
    bootstrap-theme.min.css
    bootstrap.min.css
    my-styles.css
    style.css
  favicon.ico
  font-awesome
  fonts/
    glyphicons-halflings-regular.eot
    glyphicons-halflings-regular.svg
    glyphicons-halflings-regular.ttf
    glyphicons-halflings-regular.woff
  Gemfile
  Gemfile.lock * (generated by bundler)
  Guardfile
  humans.txt
  img/
    boxes/
      art.jpg
      blog.jpg
      recipes.jpg
      resume.jpg
      swaac.jpg
      wiki.jpg
    hero.jpg
    logo-01.jpg
    logo-01.png
    logo-01.svg
    wolrd_map.png
  index.html
  js/
    main.js
    touchable.js
    vendor/
      bootstrap.min.js
      cbpAnimatedHeader.js
      classie.js
      inspinia.js
      jquery-2.1.1.js
      modernizr-custom.js
      npm.js
      pace.min.js
      wow.min.js
  README.md
  robots.txt
```


## Conclusion

So you can see it can get rather involved, yet everything has it
place. This isn't to scare you about project structures.

Emphasizing again that starting out, keep it simple. Grow into what
you need.
