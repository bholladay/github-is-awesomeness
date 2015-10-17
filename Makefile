build:
	. bin/activate && fab build

watch:
	. bin/activate && fab build && find source/ | entr fab build

publish:
	. bin/activate && fab publish


