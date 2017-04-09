# Setting up a new Website Project

Setting up a new website is usually quite easy, you really only need a
few files to get going.

Make sure you review the [general setup information](../README.md) and
[naming rules](../naming-rules.md) before embarking on this.

## Typical Website Structure

A typical website structure is shown below:

```
css/
  main.css
  reset.css
fonts/
img/
  logo.png
js/
  main.js
  vendor/
    jquery.min.js
index.html
about.html
humans.txt
404.html
```

* `index.html` - the entry point for the website, it is what a web
  server returns when you just give the bare site url. If you make
  sub-folders in your site to organize your information (a good idea),
  you should put an `index.html` file in each directory as well.

* `css` folder - this is where your CSS styles will live.

    * You may want to use Eric
      Meyer's
      [reset.css](http://meyerweb.com/eric/tools/css/reset/reset.css)
      to give a nice, clean starting point for your designs.


    * Put your styles into a `main.css` (or `styles.css` or
      `index.css` or whatever)

* `fonts` folder - if you have webfonts you want to include in your
  site, this would be the place for them.

* `img` folder - a place to store the incidental images that go along
  with your site. A caveat: don't store huge media files here or your
  project will take a long time to up and down load from Github

* `js` folder - a place to put your JavaScript files. Typical files
  would inlude:

    * `main.js` - the main collection of your JavaScript code. You
      could also call this `index.js`

    * `js/vendor` folder - if you include any javascript libraries
      with your site, such as jQuery, Bootstrap, etc, you should put
      them in this folder

* `about.html` - this is just a stand-in for any other secondary pages
  your site will have. You can have as many as you want.

* `humans.txt` - an optional file, this is the "colophon" for your
  site. This is useful as a place to give shoutouts for contributors,
  help people find you, and show the tech used on your
  site. Explanation is at [humanstxt.org](http://humanstxt.org/)

* `404.html` - another optional file, this would be the page displayed
  when someone tries to navigate to a page that does not exist.


## Using a Boilerplate

One of the best places to start a website project is to visit
the [HTML5Boilerplate](https://html5boilerplate.com/) website and
download the boilerplate and unpack it into your new project space.

You can get versions of the boilerplate with twitter bootstrap as
well, which can be very handy in getting things rolling, by visiting
the [Initializr Project](http://www.initializr.com/).

Beyond just downloading it, you may want to customize it further after
downloading it, so you don't have to make so many changes to it every
time you start a new website project.

## Leveling up: build tools

Node.js brings a lot of lovely build tools to us that help make
website development a lot easier.

Make sure you have a current version of node installed (visit
the [node.js](https://nodejs.com) website to install the latest).

You can create workflows that will automatically compile Scss/SASS,
package JavaScript, make reusable parts of your web pages, use
templates and data, and so on.

The basis for using all of these is to create "npm scripts" in a
project `package.json` file. First step is to create the file by
running:

```
npm init
```

And answering the questions. It will write out the `package.json` file
at the end. You can then modify the file in your editor, notably
looking at the `"scripts"` entry.

If you use build tools such as `grunt` or `gulp` you can easily add
the command lines to run them.

*IMPORTANT!* Modify your `.gitignore` file to include the following
two lines, if you don't already have them:

```
node_modules/
npm_debug.log
```

Then run `npm install` to initialize the project.


## Leveling up with BrowserSync

[BrowserSync](https://browsersync.io/) is a tool that makes website
development easy and fun.

You know how you have to always save your work, alt-tab to the browser
and hit refresh? Well NO MORE! With browser sync, this is done
whenever you save your work.

The installation instructions are on the home page, but you may want
to go a little bit further. Here's how I tend to set things up.

After you've built the `package.json` file in the previous step,
install `browser-sync` for the *project*. (You may already hae it
installed globally, that's okay).

```
npm install --save-dev browser-sync
```

This saves the package locally.

Now, create the browser-sync configuration file in `bs-config.js`:

```javascript
/*
 |--------------------------------------------------------------------------
 | Browser-sync config file
 |--------------------------------------------------------------------------
 */
module.exports = {
    "files": [
        '*.html',
		'*.xml',
		'*.txt',
        'css/**/*.css',
        'img/**/*',
        'js/**/*.js'
    ],
    "server": true
};
```


If you create new sub-folders, you'll need to add them as well. Of
particular note are the entries like `"js/**/*.js"`. This tells
browser-sync to watch all JavaScript files in all folders under the
`js` folder. Similarly, the `css` and `img` folders are watched
recursively.

If you organize other parts of you site in folders and
sub-folders, you may want to do the same.

Edit `package.json` and add the following to the `"scripts"` array,
before the default `"tests"` entry:

```json
  "start": "browser-sync start --config bs-config.js",
```

A full example showing the browser-sync integration is available in
the [example/package.json](example/package.json) file.

After you've updated `package.json` and `bs-config.js` and saved them,
you can now run `npm start` to see your website automatically
displayed in the default browser, and automatically refreshed when you
save changes in your files.


## Leveling up: Static Site Generators

You can go even further by using what are referred to as "static site
generators". There are many to choose from. Popular ones
include [Jekyll](https://jekyllrb.com) (which is used by Github
pages),
[Middleman](https://middlemanapp.com), [Yoeman](http://yeoman.io/)
(which is sort of a generator mixologist),
and [many many more](https://staticsitegenerators.net/).

Choosing a generator is largely a matter of comfort with the
underlying language. You can find generators in nearly every modern
language out there, including JavaScript, Ruby, Python, GOlang, PHP,
Perl, shell scripts, and more.

If you want to jump in on learning a new programming language, or even
practicing in one you already know, you could even write your own
static site generator.

### recommendations:

* If you like Ruby, [Jekyll](https://jekyllrb.com) is the most popular
  generator of all. Although configured out of the box as a blog
  engine, it doesn't have to be a blog at all. (As an aside, several
  of the GDI class slides are build using jekyll with the reveal.js
  library.)

* If you're of a JavaScript persuasion, give [Ghost](https://ghost.org)
  a look, using yoeman with
  the
  [ghost generator](https://github.com/sethvincent/generator-ghost)
