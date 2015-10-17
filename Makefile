build:
	. bin/activate && fab build

watch:
	. bin/activate && find source/ | entr fab build

publish:
	. bin/activate && fab publish


