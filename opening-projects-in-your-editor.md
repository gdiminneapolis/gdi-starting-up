# Opening a project in your editor

While most of the time, you might be used to opening individual files to work on them
from the Explorer or Finder window, depending on which OS you use, doing development
on projects is different, because you need to keep the relationships between the
different files in the proper locations.

All the modern code editors we use, Atom, Sublime Text, WebStorm, Visual Code, understand
this concept and allow you to open a project as a whole, and keep track of the files 
and folders in it. They give you a folder tree view that you should use to open files,
create files, move files, and so on.

At least on the Mac, if you do start from the finder, you can drag and drop the project folder
to the editor icon in the Dock and drop it there; that will open that editor with that 
project folder.

## Sublime Text

### Mac

On the mac, from the File -> Open dialog, you will navigate to the project's *parent*
folder, select the project folder (just click on it, don't double click it), and 
click the `Open` button.

#### From Terminal

Copy or link the file ` /Applications/Sublime\ Text\ 2.app/Contents/SharedSupport/bin/subl` to
someplace on your path (`/usr/local/bin/subl` is popular). You'll probably need `sudo` to make the link
or copy work and ensure execute permissions. Then you can open a project from the command line as:

```bash
cd Path/To/myProject
subl .
```

### Windows

On windows, from the File -> Open Folder dialog, navigate to the parent folder, select
the project folder (one click), and then click the `Open` button.

#### from `cmd.exe` or `powershell.exe`

See this stackoverflow question: http://stackoverflow.com/questions/9440639/sublime-text-from-command-line-win7
for a variety of ways to do this.

Then you can open the project directly into Sublime Text with the following commands:

```bash
cd Path\To\myProject
subl.exe .
```

## Atom

Atom works the same way that Sublime Text does on both platforms.

In addition, Atom also automatically gives you a command line tool without having to do
extra installation bits.

#### From command line:

```bash
cd path/to/project
atom .
```

