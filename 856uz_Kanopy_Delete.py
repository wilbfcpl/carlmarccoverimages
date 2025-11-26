#Delete the 856uz subfields that deal with cover images

import re

imageURLPattern=re.compile('^HTTPS://WWW.KANOPY(STREAMING)*\.COM/NODE')
imageTypePattern=re.compile('^COVER IMAGE')

for field in record.getFields('856'):
	if  field.get('u')!=None and field.get('z')!=None and record['029']!=None:
		ImageURL=field['u'].strip()
		ImageType=field['z'].strip()
		if imageTypePattern.match(ImageType.upper()) and imageURLPattern.match(ImageURL.upper()):
			record.addField('590','$u' + field['u'] + '$z' + field['z'])
			record.remove_field(field)

