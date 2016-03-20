# Some rules for naming files

Naming is one of the two hardest problems in computer science. <small>The other hardest problem is cache invalidation, which you should not be worrying about (yet). [Two Hard Things](http://martinfowler.com/bliki/TwoHardThings.html).</small>

Working on web pages introduces some rules you'll need to follow.

* names should be as descriptive as possible
* file names should not contain spaces
* files which will be used as URL addresses should be all lower case, contain no special characters except the dash `-` and period `.`. (There are a few more one could use, but restrict your names to just these)
* files which will *NOT* be used as URL address can have mixed case, but should still contain no special characters, except you can use the underscore `_` or the dash `-`, and the period `.`. Underscore is used quite often for these sorts of files instead of dash
* the dash `-` or underscore `_` makes a good word spacer
* the period `.` is best use to set off the file extension (e.g.: `.html`, `.jpg`, `.css`)
* The file name `index.html` is reserved for the "Home" page in a directory. It is the file that the web server shows when there's a bare URL path, such as `http://mywebsite.com/`.


## Examples

These files would show up in URL addresses:

* `index.html`
* `css/style.css`
* `about-me.html`
* `project-portfolio/index.html`
* `images/blue-bird-of-happiness.jpg`
* `images/blue-bird-of-happiness.thumbnail.gif`

These files would *NOT* show up in URLs:

* `README.md`
* `LICENSE.txt`
* `node_modules/`
* `bower_components/`
