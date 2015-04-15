#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import string


INITIALS = (
	'AA',
	'AAA',
	'ABA',
	'ABC',
	'ABCRN',
	'AC',
	'ACB',
	'AFC',
	'AFF',
	'AFL',
	'AHL',
	'AIK',
	'AS',
	'ASA',
	'ASEAN',
	'ATP',
	'BB',
	'BBL',
	'BDO',
	'BK',
	'BXL',
	'BYU',
	'CA',
	'CAF',
	'CDC',
	'CDT',
	'CF',
	'CFL',
	'CL',
	'CNMI',
	'CONCACAF',
	'CONMEBOL',
	'CT',
	'DEL',
	'DOJ',
	'EC',
	'EFF',
	'ERC',
	'FC',
	'FCC',
	'FF',
	'FH',
	'FIBA',
	'FIFA',
	'FIU',
	'FK',
	'FSV',
	'FTC',
	'GBL',
	'HBL',
	'HJK',
	'ICC',
	'IFK',
	'IIHF',
	'IL',
	'INDY',
	'INDYCAR',
	'IPL',
	'ITF',
	'ITM',
	'JGTO',
	'KBL',
	'KBO',
	'KHL',
	'LLC',
	'LLP',
	'LNB',
	'LNBP',
	'LNH',
	'LNR',
	'LP',
	'LPGA',
	'LSU',
	'MG',
	'MK',
	'MLB',
	'MLS',
	'MMA',
	'NASCAR',
	'NBA',
	'NCAA',
	'NFL',
	'NHL',
	'NLA',
	'NRL',
	'NY',
	'NZRU',
	'ODI',
	'OH',
	'PDC',
	'PGA',
	'PS',
	'QPR',
	'RBS',
	'RJ',
	'RLIF',
	'RN',
	'RS',
	'RSS',
	'RZ',
	'SARU',
	'SC',
	'SHL',
	'SK',
	'SMU',
	'SP',
	'SV',
	'TCU',
	'TSV',
	'UAB',
	'UC',
	'UCLA',
	'UD',
	'UEFA',
	'UFC',
	'UNLV',
	'USA',
	'USC',
	'USL',
	'USPS',
	'VFB',
	'VFL',
	'VPS',
	'WAC',
	'WNBA',
	'WTA',
	'WTO',
)

SMALL = 'a|an|and|as|at|but|by|en|for|if|in|of|on|or|the|to|v\.?|via|vs\.?'
BIG = '|'.join(INITIALS)
PUNCT = r"""!"#$%&'‘()*+,\-./:;?@\[\]\\_`{|}~"""
SMALL_WORDS = re.compile(r'^(%s)$' % SMALL, re.I)
BIG_WORDS = re.compile(r'^(%s)$' % BIG) # Big words are only left capitalized if they were capitalized in the original string.
INLINE_PERIOD = re.compile(r'[a-z][.][a-z]', re.I)
UC_ELSEWHERE = re.compile(r'[%s]*?[a-zA-Z]+[A-Z]+?' % PUNCT)
CAPFIRST = re.compile(r"^[%s]*?([A-Za-z])" % PUNCT)
SMALL_FIRST = re.compile(r'^([%s]*)(%s)\b' % (PUNCT, SMALL), re.I)
SMALL_LAST = re.compile(r'\b(%s)[%s]?$' % (SMALL, PUNCT), re.I)
SUBPHRASE = re.compile(r'([:.;?!][ ])(%s)' % SMALL)
APOS_SECOND = re.compile(r"^[dol]{1}['‘]{1}.*$", re.I)
ALL_CAPS = re.compile(r'^[A-Z0-9\s%s]+$' % PUNCT)
UC_INITIALS = re.compile(r"^(?:[A-Z]{1}\.{1}|[A-Z]{1}\.{1}[A-Z]{1})+$")
MAC_MC = re.compile(r"^([Mm]a?c)([a|c|d|g|l|m|p|t]+[a|d|e|h|l|o]+\w*)")
NONGAELIC = 'macadam|macalino'
NON_MAC = re.compile(r"^[%s]+$" % NONGAELIC, re.IGNORECASE)
AMP = re.compile("^(\w+[&+]\w+'?)([%s]*\w*)" % re.escape(string.punctuation))


def titlecase(text):
	"""
	Titlecases input text
	
	This filter changes all words to Title Caps, and attempts to be clever
	about *un*capitalizing SMALL words like a/an/the in the input.
	
	The list of "SMALL words" which are not capped comes from
	the New York Times Manual of Style, plus 'vs' and 'v'.
	
	"""
	
	lines = re.split('[\r\n]+', text)
	processed = []
	for line in lines:
		words = re.split('[\t ]', line)
		tc_line = []
		for word in words:
			aps = AMP.match(word)
			if aps:
				word = aps.group(1).upper() + aps.group(2)
				tc_line.append(word)
				continue
			if BIG_WORDS.match(word):
				tc_line.append(word.upper())
				continue
			all_caps = ALL_CAPS.match(word)
			if all_caps:
				if UC_INITIALS.match(word):
					word.upper()
					tc_line.append(word)
					continue
				else:
					word = word.lower()
			if APOS_SECOND.match(word):
				word = word.replace(word[0], word[0].upper(), 1)
				word = word.replace(word[2], word[2].upper(), 1)
				tc_line.append(word)
				continue
			if INLINE_PERIOD.search(word) or UC_ELSEWHERE.match(word):
				tc_line.append(word)
				continue
			if SMALL_WORDS.match(word):
				tc_line.append(word.lower())
				continue
			
			match = False
			if not NON_MAC.match(word):
				match = MAC_MC.match(word)
			else:
				word.capitalize()
			if match:
				tc_line.append("%s%s" % (match.group(1).capitalize(), match.group(2).capitalize()))
				continue
			
			if "/" in word and not "//" in word:
				slashed = []
				for item in word.split('/'):
					slashed.append(CAPFIRST.sub(lambda m: m.group(0).upper(), item))
				tc_line.append("/".join(slashed))
				continue
			
			hyphenated = []
			for item in word.split('-'):
				hyphenated.append(CAPFIRST.sub(lambda m: m.group(0).upper(), item))
			tc_line.append("-".join(hyphenated))
		
		result = " ".join(tc_line)
		
		result = SMALL_FIRST.sub(lambda m: '%s%s' % (
			m.group(1),
			m.group(2).capitalize()
		), result)
		
		result = SMALL_LAST.sub(lambda m: m.group(0).capitalize(), result)
		
		result = SUBPHRASE.sub(lambda m: '%s%s' % (
			m.group(1),
			m.group(2).capitalize()
		), result)
		
		processed.append(result)
	
	return "\n".join(processed)
