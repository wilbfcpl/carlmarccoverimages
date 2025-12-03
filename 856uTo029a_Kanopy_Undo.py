import re

imageURLPattern=re.compile('^HTTPS://WWW.KANOPY(STREAMING)*\.COM/NODE')
imageTypeString="Cover Image"

for field in record.getFields('029'):
	if 'a' in field:
		ImageURL=field['a'].strip()
		if imageURLPattern.match(ImageURL.upper()):
			record.addField('856','$u' + field['a'] + '$z' + imageTypeString )
			record.remove_field(field)
