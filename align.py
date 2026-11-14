import json, os, unicodedata

def words_in(phrases):
    """phrases: list of (text_or_wordlist, start, end, flag) -> word list with times spread by word length"""
    out = []
    for ph, s, e, fl in phrases:
        ws = ph.split() if isinstance(ph, str) else ph
        tot = sum(len(w) + 1.5 for w in ws)
        t = s
        for w in ws:
            d = (e - s) * (len(w) + 1.5) / tot
            item = [w, round(t, 3), round(t + d * .92, 3)]
            if fl:
                item.append(fl)
            out.append(item)
            t += d
    return out

def bare(w):
    w = unicodedata.normalize('NFD', w)
    return ''.join(c for c in w if unicodedata.category(c) != 'Mn' and c not in '،."‏').strip()

def hadith(n, first, last, back=0):
    """Arabic hadith words copied from the dataset file, from the word whose bare form is `first`
    to the next word whose bare form is `last` (diacritics ignored only for matching)."""
    h = json.load(open(os.path.join(os.environ.get('HADITH_DIR', 'hadith'), f'ara{n}.json'), encoding='utf-8'))['hadiths'][0]['text']
    h = h.replace('‏', '')
    toks = [t for t in h.split() if bare(t)]
    i = next(k for k, t in enumerate(toks) if bare(t) == first)
    j = next(k for k in range(i, len(toks)) if bare(toks[k]) == last)
    return [t.strip('"').strip() for t in toks[i - back:j + 1]]
