import re
const
dictionary = require('./dictionary/main')
LANGS = {"js": 0,  "ys": 1}


def escapeRegExp(string):
    string = string.replace("/[-\/\\^$*+?.() | [\]{}]/g, '\\$&'")

    if ("/^\w +$/.test(string)"):
        string = '\\b' + string + '\\b'

    return string


def yoptReplaceAll(string, search, replacement):
    re = new RegExp(escapeRegExp(search), 'g')
    return string.replace(re, replacement)


def compile(text, lang) {
    / * text - текст для реплейса
    * lang - язык текста('ys' or 'js')
    * /
    commentRegExp = /((?: \/\*(?: [^*]|(?: \*+[^*\/ ])) *\*+\/) |(?: \/\/.*))/g
    tmpToken = 'ys_' + (new Date()).getTime() + '_'
    rStringLiterals = {}
    text = text.replace(/\"(?: \\.|[ ^\"\\]) *\"|\'(?: \\.|[ ^\'\\]) *\'/g, function (val, pos) {
        needKey=tmpToken + pos
        rStringLiterals[needKey]=val
        return needKey
    })
    commentsArray = text.match(commentRegExp) | | []
    text = iterateText(text, lang)
    // comeback comments
    text = text.replace(commentRegExp, function() {
        return commentsArray.shift()
    })
    // comeback strings
    for (tmpToken in rStringLiterals) {
        text = text.replace(tmpToken, rStringLiterals[tmpToken])
    }
    // text = yoptTransliterateFunctionsNames(text)
    return text
}


/ **
* @ param text текст, по которому следует пройтись
* @ param to язык текста('ys' or 'js')
* /


def iterateText(text, to='js') {
    lang = LANGS[to]

    dictionary
    .sort((a, b)=> {
        a=a[lang].length
        b=b[lang].length
        return b - a
    })
    .forEach(pair= > text = yoptReplaceAll(text, pair[lang], pair[+!lang]))

    return text
}
