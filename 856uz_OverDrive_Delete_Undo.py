# Undo the delete of cover image 856uz subfields

import re

imageURLPattern=re.compile('^HTTPS://IMG1.OD-CDN.COM/IMAGETYPE')
imageTypePattern=re.compile('^((THUMBNAIL)|(LARGE)) COVER IMAGE')


for field in record.getFields('590'):
	if  field.get('u')!=None and field.get('z')!=None and record.getFields('029')!=None:
		ImageURL=field['u'].strip()
		ImageType=field['z'].strip()
		if imageTypePattern.match(ImageType.upper()) and imageURLPattern.match(ImageURL.upper()):
			record.addField('856','$u' + field['u'] + '$z' + field['z'])
			record.remove_field(field)
