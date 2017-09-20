beamer: git-handson.md.html git-intro.md.html

%.md.html: %.md
	cat remark/head.html $< remark/tail.html > $@
