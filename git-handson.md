# Git - finally do something

You should have a linux computer - debian or ubuntu based, otherwise at least installation sdteps will differ. For the following: `Typewriter font` is a command to be typed in a terminal, the rest is most likely a comment.

## Preparation

`sudo apt install git markdown rsync python-pil` - some of these might be installed but it doesnt hurt.

```
git config --global user.email "b.simpson@springfield.com" 
git config --global user.name "Bart Simpson"
```

Should be done once, sets default email and username for commit messages, there is a `git blame` to find you! *Without the `-global` but still within a project sets a possibly different username/mail for this project* 

Visit https://github.com/softimpulse/gitintro.git

```
mkdir gitexamples  # sets up a directory for this lecture
cd gitexamples     # P.S. instead of typing gitexamples just hit Alt-.
git clone https://github.com/softimpulse/gitintro.git
```

`ls` - nothing really unexpected, i assume? Maybe you expected a `.git`, well historical bla, you can even clone without this `.git`

`git status` - well we are not in a git repo

`cd gitintro` and again: `git status` we are on master branch, the default and we are in sync with origin (the github repo, where we got this stuff) and branch master (It is not necessary that branchnames on remote and master are equal) take a look at the README with `less README.md` (quit with `q`), do an `ls -la`, all the GIT magic is in `.git` nowhere else!

Go back to gitexamples/

```
mkdir mine
cp -r gitintro/examples/first mine/
cd mine
git status
```

Remember: The files inside a git repo have no git magic, also subdirs - only .git in projects root

Create your own git- repo:

```
git init
git status
git add .
git status
git commit 'I will never forget my first commit'
git status
```

