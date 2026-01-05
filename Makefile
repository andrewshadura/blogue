DOMAIN = blog.shadura.me
UPLOAD_HOST = shadura.me
UPLOAD_PATH_ONLY = blog
UPLOAD_PATH = $(UPLOAD_HOST):$(UPLOAD_PATH_ONLY)
HUGO = hugo-0.134

COMMON_OPTIONS = --verbose

html:
	$(HUGO) $(COMMON_OPTIONS)

serve:
	$(HUGO) server $(COMMON_OPTIONS) --debug

serve-staging:
	$(HUGO) server $(COMMON_OPTIONS) --debug --environment staging

upload: html
	jdupes -1 -L -r public/
	rsync -rpHv --progress --delete-after public/ $(UPLOAD_PATH)
	ssh -t $(UPLOAD_HOST) jdupes -1 -L -r $(UPLOAD_PATH_ONLY)

upload-only: html
	jdupes -1 -L -r public/
	rsync -rpHv --progress public/ $(UPLOAD_PATH)
	ssh -t $(UPLOAD_HOST) jdupes -1 -L -r $(UPLOAD_PATH_ONLY)

quick-upload: html quick-upload-only

quick-upload-only:
	jdupes -1 -L -r public/
	rsync -rpvHz --progress -f'+ */' -f'+ *.html' -f'+ *.xml' -f'+ *.js' -f'+ *.css' -f'- *' public/ $(UPLOAD_PATH)
	rsync -rpHv --ignore-existing --progress -f'+ *.jpg' -f'+ *.png' -f'+ *.webp' public/ $(UPLOAD_PATH)

clean:
	rm -rf public/*

publish: html upload
