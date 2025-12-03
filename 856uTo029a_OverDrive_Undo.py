import re

imageURLPattern=re.compile('^HTTPS://IMG1.OD-CDN\.COM/IMAGETYPE')
imageTypeString="Thumbnail cover Image"

for field in record.getFields('029'):
	if 'a' in field:
		ImageURL=field['a'].strip()
		if imageURLPattern.match(ImageURL.upper()):
			record.addField('856','$u' + field['a'] + '$z' + imageTypeString )
			record.remove_field(field)
