#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

# from __future__ import division, absolute_import, print_function, unicode_literals


def enum(**kwargs):
    return type('Enum', (), kwargs)


BET_TYPES = enum(
    MONEY_LINE='Money Line',
    SPREAD_LINE='Spread Line',
    OVER_UNDER='Over Under'
)

BET_AGENTS = enum(
    OVER='Over',
    UNDER='Under',
    DRAW='Draw'
)

BET_SCOPES = enum(
    GAME='Game',
)

BET_DURATIONS = enum(
    GAME='Game',

    H1='1st Half',
    H2='2nd Half',

    Q1='1st Quarter',
    Q2='2nd Quarter',
    Q3='3rd Quarter',
    Q4='4th Quarter',

    S1='1st Set',
    S2='2nd Set',
    S3='3rd Set',
    S4='4th Set',
    S5='5th Set',

    P1='1st Period',
    P2='2nd Period',
    P3='3rd Period',
    I1='1st Inning',
    I2='2nd Inning',
    I3='3rd Inning',
    I4='4th Inning',
    I5='5th Inning',
    I6='6th Inning',
    I7='7th Inning',
    I8='8th Inning',
    I9='9th Inning',

    F1='1st Frame',
    F2='2nd Frame',
    F3='3rd Frame',
    F4='4th Frame',
    F5='5th Frame',
    F6='6th Frame',
    F7='7th Frame',
    F8='8th Frame',
    F9='9th Frame',
    F10='10th Frame',
    F11='11th Frame',
)

BET_VALUE_TYPES = enum(
    RHE='R+H+E',
    SETS='Sets',
    POINTS='Points',
    ADVANCES='Advances',
    WINS='Wins',
)

SPORTS_LEAGUES = { # Kept as a partial reference and cache warmer. Sport > Sport is a catchall.
    'Australian Football': (
        'AFL',
    ),
    'Auto Racing': (
        'Formula 1',
        'MotoGP',
        'NASCAR',
    ),
    'Baseball': (
        'Japan',
        'MLB',
    ),
    'Basketball': (
        'ABA League',
        'ACB',
        'Basketball',
        'BB',
        'BBL',
        'Brazil',
        'EuroChallenge',
        'Euroleague',
        'FIBA',
        'GBL',
        'Germany',
        'KBL',
        'Lega Basket',
        'LNB',
        'LNBP',
        'NBA',
        'NCAA',
        'Philippines',
        'South America',
        'Spain',
    ),
    'Cricket': (
        'Cricket',
        'ICC',
    ),
    'Darts': (
        'BDO',
        'Darts',
        'PDC',
    ),
    'Football': (
        'CFL',
        'NCAA',
        'NFL',
    ),
    'Futsal': (
        'Spain',
        'UEFA',
    ),
    'Golf': (
        'Euro PGA',
        'LPGA',
        'PGA',
    ),
    'Handball': (
        'Austria',
        'Denmark',
        'Elitserien',
        'European Championship',
        'Handball',
        'HBL',
        'Liga Asobal',
        'LNH',
    ),
    'Hockey': (
        'AHL',
        'Champions League',
        'DEL',
        'Hockey',
        'IIHF',
        'KHL',
        'Liiga',
        'NHL',
        'NLA',
        'Russia',
        'SHL',
    ),
    'Martial Arts': (
        'Bellator',
        'Boxing',
        'Grappling',
        'Martial Arts',
        'UFC',
    ),
    'Rugby League': (
        'NRL',
        'RLIF',
        'Super League',
    ),
    'Rugby Union': (
        'England',
        'ERC',
        'Europe',
        'European Champions Cup',
        'LNR',
        'NZRU',
        'Premiership',
        'Pro12',
        'RBS',
        'Rugby Union',
        'SARU',
        'Six Nations',
    ),
    'Snooker': (
        'Snooker',
    ),
    'Soccer': (
        'AFC',
        'Africa',
        'Algeria',
        'Argentina',
        'Australia',
        'Austria',
        'Belarus',
        'Belgium',
        'Bolivia',
        'Brazil',
        'Bulgaria',
        'CAF',
        'Caribbean Cup',
        'Chile',
        'China',
        'Colombia',
        'CONCACAF',
        'CONMEBOL',
        'Croatia',
        'Cyprus',
        'Czech Republic',
        'Denmark',
        'Ecuador',
        'Egypt',
        'El Salvador',
        'England',
        'FIFA',
        'Finland',
        'France',
        'Germany',
        'Greece',
        'Guatemala',
        'Holland',
        'Honduras',
        'Hungary',
        'India',
        'Ireland',
        'Italy',
        'Jamaica',
        'Japan',
        'Jordan',
        'Lithuania',
        'Mexico',
        'MLS',
        'Morocco',
        'Netherlands',
        'New Zealand',
        'Northern Ireland',
        'Norway',
        'Panama',
        'Paraguay',
        'Peru',
        'Poland',
        'Portugal',
        'Qatar',
        'Romania',
        'Russia',
        'Saudi Arabia',
        'Scotland',
        'Slovakia',
        'Slovenia',
        'Soccer',
        'South Africa',
        'South Korea',
        'Spain',
        'Sweden',
        'Switzerland',
        'Turkey',
        'U20',
        'UEFA',
        'Ukraine',
        'United Arab Emirates',
        'Uruguay',
        'Venezuela',
        'Wales',
    ),
    'Surfing': (
        'Surfing',
    ),
    'Tennis': (
        'ATP',
        'ITF',
        'Tennis',
        'WTA',
    ),
    'Volleyball': (
        'Argentina',
        'Brazil',
        'Champions League',
        'France',
        'Germany',
        'Italy',
        'PlusLiga',
        'South Korea',
        'Spain',
        'Super League',
        'Volleyball',
    ),
}

SUPERFLUOUS_ACRONYMS = (
    'AA',
    'AC',
    'AFC',
    'AS',
    'BK',
    'CA',
    'CF',
    'EC',
    'FC',
    'FF',
    'FH',
    'FK',
    'FSV',
    'IFK',
    'IL',
    'SC',
    'SK',
    'SV',
    'TSV',
    'UD',
    'VFB',
    'VFL'
)

HTML_ENTITIES = {
    'Aacute': '\xc1',
    'aacute': '\xe1',
    'Acirc': '\xc2',
    'acirc': '\xe2',
    'acute': '\xb4',
    'AElig': '\xc6',
    'aelig': '\xe6',
    'Agrave': '\xc0',
    'agrave': '\xe0',
    'alefsym': '\u2135',
    'Alpha': '\u0391',
    'alpha': '\u03b1',
    'amp': '&',
    'and': '\u2227',
    'ang': '\u2220',
    'apos': "'",
    'Aring': '\xc5',
    'aring': '\xe5',
    'asymp': '\u2248',
    'Atilde': '\xc3',
    'atilde': '\xe3',
    'Auml': '\xc4',
    'auml': '\xe4',
    'bdquo': '\u201e',
    'Beta': '\u0392',
    'beta': '\u03b2',
    'brvbar': '\xa6',
    'bull': '\u2022',
    'cap': '\u2229',
    'Ccedil': '\xc7',
    'ccedil': '\xe7',
    'cedil': '\xb8',
    'cent': '\xa2',
    'Chi': '\u03a7',
    'chi': '\u03c7',
    'circ': '\u02c6',
    'clubs': '\u2663',
    'cong': '\u2245',
    'copy': '\xa9',
    'crarr': '\u21b5',
    'cup': '\u222a',
    'curren': '\xa4',
    'dagger': '\u2020',
    'Dagger': '\u2021',
    'darr': '\u2193',
    'dArr': '\u21d3',
    'deg': '\xb0',
    'Delta': '\u0394',
    'delta': '\u03b4',
    'diams': '\u2666',
    'divide': '\xf7',
    'Eacute': '\xc9',
    'eacute': '\xe9',
    'Ecirc': '\xca',
    'ecirc': '\xea',
    'Egrave': '\xc8',
    'egrave': '\xe8',
    'empty': '\u2205',
    'emsp': '\u2003',
    'ensp': '\u2002',
    'Epsilon': '\u0395',
    'epsilon': '\u03b5',
    'equiv': '\u2261',
    'Eta': '\u0397',
    'eta': '\u03b7',
    'ETH': '\xd0',
    'eth': '\xf0',
    'Euml': '\xcb',
    'euml': '\xeb',
    'euro': '\u20ac',
    'exist': '\u2203',
    'fnof': '\u0192',
    'forall': '\u2200',
    'frac12': '\xbd',
    'frac14': '\xbc',
    'frac34': '\xbe',
    'frasl': '\u2044',
    'Gamma': '\u0393',
    'gamma': '\u03b3',
    'ge': '\u2265',
    'gt': '>',
    'harr': '\u2194',
    'hArr': '\u21d4',
    'hearts': '\u2665',
    'hellip': '\u2026',
    'Iacute': '\xcd',
    'iacute': '\xed',
    'Icirc': '\xce',
    'icirc': '\xee',
    'iexcl': '\xa1',
    'Igrave': '\xcc',
    'igrave': '\xec',
    'image': '\u2111',
    'infin': '\u221e',
    'int': '\u222b',
    'Iota': '\u0399',
    'iota': '\u03b9',
    'iquest': '\xbf',
    'isin': '\u2208',
    'Iuml': '\xcf',
    'iuml': '\xef',
    'Kappa': '\u039a',
    'kappa': '\u03ba',
    'Lambda': '\u039b',
    'lambda': '\u03bb',
    'lang': '\u2329',
    'laquo': '\xab',
    'larr': '\u2190',
    'lArr': '\u21d0',
    'lceil': '\u2308',
    'ldquo': '\u201c',
    'le': '\u2264',
    'lfloor': '\u230a',
    'lowast': '\u2217',
    'loz': '\u25ca',
    'lrm': '\u200e',
    'lsaquo': '\u2039',
    'lsquo': '\u2018',
    'lt': '<',
    'macr': '\xaf',
    'mdash': '\u2014',
    'micro': '\xb5',
    'middot': '\xb7',
    'minus': '\u2212',
    'Mu': '\u039c',
    'mu': '\u03bc',
    'nabla': '\u2207',
    'nbsp': '\xa0',
    'ndash': '\u2013',
    'ne': '\u2260',
    'ni': '\u220b',
    'not': '\xac',
    'notin': '\u2209',
    'nsub': '\u2284',
    'Ntilde': '\xd1',
    'ntilde': '\xf1',
    'Nu': '\u039d',
    'nu': '\u03bd',
    'Oacute': '\xd3',
    'oacute': '\xf3',
    'Ocirc': '\xd4',
    'ocirc': '\xf4',
    'OElig': '\u0152',
    'oelig': '\u0153',
    'Ograve': '\xd2',
    'ograve': '\xf2',
    'oline': '\u203e',
    'Omega': '\u03a9',
    'omega': '\u03c9',
    'Omicron': '\u039f',
    'omicron': '\u03bf',
    'oplus': '\u2295',
    'or': '\u2228',
    'ordf': '\xaa',
    'ordm': '\xba',
    'Oslash': '\xd8',
    'oslash': '\xf8',
    'Otilde': '\xd5',
    'otilde': '\xf5',
    'otimes': '\u2297',
    'Ouml': '\xd6',
    'ouml': '\xf6',
    'para': '\xb6',
    'part': '\u2202',
    'permil': '\u2030',
    'perp': '\u22a5',
    'Phi': '\u03a6',
    'phi': '\u03c6',
    'Pi': '\u03a0',
    'pi': '\u03c0',
    'piv': '\u03d6',
    'plusmn': '\xb1',
    'pound': '\xa3',
    'prime': '\u2032',
    'Prime': '\u2033',
    'prod': '\u220f',
    'prop': '\u221d',
    'Psi': '\u03a8',
    'psi': '\u03c8',
    'quot': '"',
    'radic': '\u221a',
    'rang': '\u232a',
    'raquo': '\xbb',
    'rarr': '\u2192',
    'rArr': '\u21d2',
    'rceil': '\u2309',
    'rdquo': '\u201d',
    'real': '\u211c',
    'reg': '\xae',
    'rfloor': '\u230b',
    'Rho': '\u03a1',
    'rho': '\u03c1',
    'rlm': '\u200f',
    'rsaquo': '\u203a',
    'rsquo': '\u2019',
    'sbquo': '\u201a',
    'Scaron': '\u0160',
    'scaron': '\u0161',
    'sdot': '\u22c5',
    'sect': '\xa7',
    'shy': '\xad',
    'Sigma': '\u03a3',
    'sigma': '\u03c3',
    'sigmaf': '\u03c2',
    'sim': '\u223c',
    'spades': '\u2660',
    'sub': '\u2282',
    'sube': '\u2286',
    'sum': '\u2211',
    'sup': '\u2283',
    'sup1': '\xb9',
    'sup2': '\xb2',
    'sup3': '\xb3',
    'supe': '\u2287',
    'szlig': '\xdf',
    'Tau': '\u03a4',
    'tau': '\u03c4',
    'there4': '\u2234',
    'Theta': '\u0398',
    'theta': '\u03b8',
    'thetasym': '\u03d1',
    'thinsp': '\u2009',
    'THORN': '\xde',
    'thorn': '\xfe',
    'tilde': '\u02dc',
    'times': '\xd7',
    'trade': '\u2122',
    'Uacute': '\xda',
    'uacute': '\xfa',
    'uarr': '\u2191',
    'uArr': '\u21d1',
    'Ucirc': '\xdb',
    'ucirc': '\xfb',
    'Ugrave': '\xd9',
    'ugrave': '\xf9',
    'uml': '\xa8',
    'upsih': '\u03d2',
    'Upsilon': '\u03a5',
    'upsilon': '\u03c5',
    'Uuml': '\xdc',
    'uuml': '\xfc',
    'weierp': '\u2118',
    'Xi': '\u039e',
    'xi': '\u03be',
    'Yacute': '\xdd',
    'yacute': '\xfd',
    'yen': '\xa5',
    'Yuml': '\u0178',
    'yuml': '\xff',
    'Zeta': '\u0396',
    'zeta': '\u03b6',
    'zwj': '\u200d',
    'zwnj': '\u200c',
}
