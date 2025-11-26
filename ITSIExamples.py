-- Multiple 856 Tags
import re

imageURLPattern=re.compile('^HTTPS://WWW.KANOPY(STREAMING)*\.COM/NODE')
imageTypePattern=re.compile('^COVER IMAGE')

for field in record.getFields('856'):
	if  field['u']!=None and record['029']==None:
		ImageURL=field['u'].strip()
		ImageType=field['z'].strip()
		if imageTypePattern.match(ImageType.upper()) and imageURLPattern.match(ImageURL.upper()):
			record.addField('029','$a' + ImageURL)


-- OverDrive Series 245b
-- New version
import re

stringPattern='series, book'
spaceChar=' '
slashChar='/'

if record['245']['b']!=None:
	twoFortyFiveB=record['245']['b']
	if stringPattern in twoFortyFiveB:
		fieldGroups=re.search(r'(?P<SERIES>series,)\s+(?P<BOOKNUMBER>books* [0-9]+(-[0-9]+)*)\s*/$',twoFortyFiveB)
		bookSeries=fieldGroups.group('BOOKNUMBER')
		if record['490']!=None:
			fourNinetyA=record['490']['a']
			record['490']['a']=fourNinetyA + ' ;'
			record['490'].addSubfield('v',bookSeries)

		if (record['590']==None ) :
			record.addField('590','$a' + twoFortyFiveB)
		else:
			record['590']['a']=record['245']['b']
		for field in record.getFields('245'):
			field.deleteSubfield('b')
		if record['245']['a']!=None:
			twoFortyFiveA=record['245']['a']
			aFieldGroups=re.search(r'(?P<TWOFORTYFIVEA>^.+)\s*(?P<COLON>:$)',twoFortyFiveA)
			base245a=aFieldGroups.group('TWOFORTYFIVEA')
			record['245']['a']=base245a + ' ' + slashChar

- Old version
import re

stringPattern='series, book'
spaceChar=' '
slashChar='/'

if record['245']['b']!=None:
	twoFortyFiveB=record['245']['b']
	if stringPattern in twoFortyFiveB:
		fieldGroups=re.search(r'(?P<SERIES>series,)\s+(?P<BOOKNUMBER>book.+)\s*/$',twoFortyFiveB)
		bookSeries=fieldGroups.group('BOOKNUMBER')
		if record['490']!=None:
			fourNinetyA=record['490']['a']
			record['490']['a']=fourNinetyA + ' ;'
			record['490'].addSubfield('v',bookSeries)

		if (record['590']==None ) :
			record.addField('590','$a' + twoFortyFiveB)
		else:
			record['590']['a']=record['245']['b']
		for field in record.getFields('245'):
			field.deleteSubfield('b')
		if record['245']['a']!=None:
			twoFortyFiveA=record['245']['a']
			aFieldGroups=re.search(r'(?P<TWOFORTYFIVEA>^.+)\s*(?P<COLON>:$)',twoFortyFiveA)
			base245a=aFieldGroups.group('TWOFORTYFIVEA')
			record['245']['a']=base245a + ' ' + slashChar


-- Undo 245b series changes to 490v, 490a, and 590a

import re
colonChar=':'

if record['490']['a']!=None:
	fourNinetyA=record['490']['a']
	aFieldGroups=re.search(r'(?P<FOURNINETYA>^.+)\s;$' ,fourNinetyA)
	base490a=aFieldGroups.group('FOURNINETYA')
	record['490']['a']=base490a

if record['490']['v']!=None:
	record['490'].delete_subfield('v')

	if record['245']['a']!=None:
		twoFortyFiveA=record['245']['a']
		bFieldGroups=re.search(r'(?P<TWOFORTYFIVEA>^.+)\s*(?P<SLASH>/$)',twoFortyFiveA)
		base245a=bFieldGroups.group('TWOFORTYFIVEA')
		record['245']['a']=base245a + ' ' + colonChar
	if record['590']['a']!=None and 'series' in record['590']['a']:
		twoFortyFiveB= record['590']['a']
		record.remove_field(record['590'])
		if record['245']['b']==None:
			record['245'].addSubfield('b',twoFortyFiveB)
	

import re
ISBN1=re.compile('[0-9X]{10,13}')


for field in record.getFields('020'):
	if 'a' not in field:
		for index,subfield in enumerate(field.subfields): 
			if 'z' in subfield:
				m=ISBN1.match(field.subfields[index+1])
				if m!=None:
					record.addField('590','$a')
					record['590']['a']=m.group()
				
				
				
	

import re

spacecolon=re.compile(' \s*\:\s*$')
dashforc='/' 
generic1='a novel'
generic2='a mystery'
generic3='a thriller'

if record['245']['b'] !=None:
	if any (generic.upper() in record['245']['b'].upper() for generic in (generic1, generic2,generic3) )    :
		record.addField('590','$a')
		record['590']['a']='245a)' + record['245']['a'] + ' 245b)' + record['245']['b']
		for field in record.getFields('245'):
			field.deleteSubfield('b')
		tempListA=spacecolon.split(record['245']['a'])
		twofourfivea=' '.join(tempListA)
		
		record['245']['a']= twofourfivea
		if record['245']['h'] !=None:
			record['590']['a']+= ' ' + '245h)' + record['245']['h']
			tempH=re.sub('/$','',record['245']['h'])
			tempListH=spacecolon.split(tempH)
			twofourfiveh=' '.join(tempListH)	
            
            
            import re

spacecolon=re.compile(' \s*\:\s*$')
dashforc='/' 
generic1='a novel'
generic2='a mystery'
generic3='a thriller'

if record['245']['b'] !=None:
	if any (generic.upper() in record['245']['b'].upper() for generic in (generic1, generic2,generic3) )    :
		record.addField('590','$a')
		record['590']['a']='245a)' + record['245']['a'] + ' 245b)' + record['245']['b']
		for field in record.getFields('245'):
			field.deleteSubfield('b')
		tempListA=spacecolon.split(record['245']['a'])
		twofourfivea=' '.join(tempListA)
		
		record['245']['a']= twofourfivea
		if record['245']['h'] !=None:
			record['590']['a']+= ' ' + '245h)' + record['245']['h']
			tempH=re.sub('/$','',record['245']['h'])
			tempListH=spacecolon.split(tempH)
            
            OLD_CATEGORY='DVD CH'
NEW_PREFIX = 'J DVD'
RHS_START_INDEX=2

if OLD_CATEGORY in record['092']['a']:
	savedCallNumber=record['092']['a']
	prev_saved=record.getFields('590')
	if len(prev_saved)==0:
		record.addField('590','$a')
	
	if 'b' in record['092'].subfields:
		secondPart=record['092']['b']
	else:
		secondPart=None		
	wholeThing=record['092']['a'].split(' ')
	length =len(wholeThing)
	if length>=RHS_START_INDEX and secondPart is None:
		rhs= ' '.join(wholeThing[RHS_START_INDEX:length:1])
		record['092']['a'] = NEW_PREFIX + ' ' + rhs
	
	elif not (secondPart is None ) :
		savedCallNumber += ' ' + secondPart
		record['092']['a'] = NEW_PREFIX + ' ' + secondPart
		for field in record.getFields('092'):
			field.deleteSubfield('b')

	record['590']['a']=savedCallNumber
    
    Changes the encoding level to full
record.leader = record.leader[:17]+' '+record.leader[18:]
Notation for fiction is added in 008
record['008'].data = record['008'].data[:33]+'1'+record['008'].data[34:]
Removes the following tags
for tagnumber in ('010', '015', '016', '037', '050', '082', '092', '263', '938'):
while tagnumber in record:
record.remove_field(record[tagnumber])
fields_to_delete=[]
for field in fields_to_delete:
record.remove_field(field)
Macros: Adult Superhero Graphic Novels
Adds the 092$a
record.addField( '092', '$aGRAPHIC NOVEL$b' )
Removes bisac, fast or sears subject headings
for field in record.getFields('6xx'):
if '2' in field and (field['2'].startswith('fast') or field['2'].startswith('bisacsh') or
field['2'].startswith('sears')):
fields_to_delete.append(field)

import re


aPrefix='092a:'
bPrefix='092b:'

abSubfields=re.compile('^092a:(\w+.*)092b:(\w+.*)\s*$')


if record['590']!=None:
	if ( record['092'] != None):
		abmatch=abSubfields.match(record['590']['a'])
		if abmatch:
			record['092']['a']=abmatch.group(1).strip()
			record['092'].addSubfield('b',abmatch.group(2).strip())
			record.remove_field(record['590'])	
            
            
            
  #Subfield
  marcrecnum='650'
oldSubj='Fiction'
newSubj='Juvenile fiction'


for field in record.getFields(marcrecnum):
for index, subfield in enumerate(field.subfields):
if oldSubj in subfield:
subcatindex=field.subfields[index-1]
field.deleteSubfield(subcatindex)
field.addSubfield(subcatindex,newSubj)


Here's a replace I did to change a server name. Let me  know if you need clarification on this or help localizing it to your issue:

# Converts 029 link 'bancroft.berkeley-public.org' to 'services.berkeleypubliclibrary.org'

import re
pattern = re.compile('bancroft.berkeley-public')
for field in record.getFields():
 if field.tag[:3] == '029':
  i = 0                               # sets index position; .index() won't work because of repeating subfields
  for subf in field.subfields:  # changes fields into a list of subfields
   if i%2 == 1 and pattern.search(subf):
    field.subfields[i] = pattern.sub('services.berkeleypubliclibrary', subf)
   i += 1                           # increases index to help traversal
   
   
   strSuba='$a'
strRemove='Remove Empty Bib'
record.addField('590',strSuba+strRemove)

#add590_ForDelBids_undo


strRemove='Remove Empty Bib'

for f in record.get_fields('590'):
	for s in f.get_subfields('a'):
		if strRemove in s:
			record.remove_field(f)
            
            
            #Level4 Cleanup 590

if record['092']['a']!=None:
	line=record['092']['a']
    
if (any (regex.match(line) for regex in [HOOPLA, CDBOOK, PL]) ):
		for field in record.getFields('590'):
			record.remove_field(field)

#Level 3 
# 590 Match 
re.compile('^\s*E\s+(\w+\s*)+\-\s*VERY\s+EASY.*$')

record['092'].delete_subfield('b')
record.remove_field(record[‘938’])
trailer='Instantly available on hoopla.'
LibID='&Lid=YourHooplaLibID'

for field in record.get_fields('856'):
	if 'u' in field and trailer in field['z']:
		field['u'] += LibID
        
        LibID='&Lid=YourHooplaLibID'

for field in record.get_fields('856'):
	if 'u' in field and LibID in field['u']:
		field['u'] = field['u'][0:-12]