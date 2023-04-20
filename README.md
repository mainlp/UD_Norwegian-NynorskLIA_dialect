# UD_Norwegian-NynorskLIA_dialect

This script adds word-level phonetic transcriptions to the [UD Norwegian NynorskLIA](https://github.com/UniversalDependencies/UD_Norwegian-NynorskLIA) treebank ([CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); article: [Øvrelid ea 2018](https://aclanthology.org/L18-1710/)).

It was used for the paper *Does manipulating tokenization aid cross-lingual transfer? A study on POS tagging for non-standardized languages* (Blaschke ea, VarDial 2023, link to come).

## Usage/details

Run `run.sh` to first get the transcriptions from the [LIA norsk](http://tekstlab.uio.no/LIA/norsk/index.html) project ([CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)), and to then to copy the files and automatically add the phonetic transcriptions to the MISC entries, where available.

Before:
```
# sent_id = 000006
# text = men så blei det slutt så måtte eg overta den mjølka au da køyrde vi .
# dialect: eidsberg speakerid: eidsberg_uio_03
1   men men CCONJ   _   _   3   cc  _   _
2   så  så  ADV _   _   3   advmod  _   _
3   blei    bli VERB    _   Mood=Ind|Tense=Past|VerbForm=Fin    0   root    _   _
4   det det PRON    _   Gender=Neut|Number=Sing|Person=3|PronType=Prs   3   expl    _   _
5   slutt   slutt   NOUN    _   Definite=Ind|Gender=Masc|Number=Sing    3   xcomp   _   _
6   så  så  ADV _   _   9   advmod  _   _
7   måtte   måtte   AUX _   Mood=Ind|Tense=Past|VerbForm=Fin    9   aux _   _
8   eg  eg  PRON    _   Animacy=Hum|Case=Nom|Number=Sing|Person=1|PronType=Prs  9   nsubj   _   _
9   overta  overta  VERB    _   VerbForm=Inf    3   conj    _   _
10  den den DET _   Gender=Fem|Number=Sing|PronType=Dem 11  det _   _
11  mjølka  mjølk   NOUN    _   Definite=Def|Gender=Fem|Number=Sing 9   obj _   _
12  au  au  ADV _   _   9   advmod  _   _
13  da  da  ADV _   _   14  advmod  _   _
14  køyrde  køyre   VERB    _   Mood=Ind|Tense=Past|VerbForm=Fin    3   conj    _   _
15  vi  vi  PRON    _   Animacy=Hum|Case=Nom|Number=Plur|Person=1|PronType=Prs  14  nsubj   _   _
16  .   $.  PUNCT   _   _   3   punct   _   _
```

After:
```
# sent_id = 000006
# text = men så blei det slutt så måtte eg overta den mjølka au da køyrde vi .
# text_orig = mænn så bLæi de sjlutt så måtte jæi åverta dænn mjæLLka ævv da kjørte ve .
# dialect: eidsberg speakerid: eidsberg_uio_03
1   men men CCONJ   _   _   3   cc  _   Phono=mænn
2   så  så  ADV _   _   3   advmod  _   Phono=så
3   blei    bli VERB    _   Mood=Ind|Tense=Past|VerbForm=Fin    0   root    _   Phono=bLæi
4   det det PRON    _   Gender=Neut|Number=Sing|Person=3|PronType=Prs   3   expl    _   Phono=de
5   slutt   slutt   NOUN    _   Definite=Ind|Gender=Masc|Number=Sing    3   xcomp   _   Phono=sjlutt
6   så  så  ADV _   _   9   advmod  _   Phono=så
7   måtte   måtte   AUX _   Mood=Ind|Tense=Past|VerbForm=Fin    9   aux _   Phono=måtte
8   eg  eg  PRON    _   Animacy=Hum|Case=Nom|Number=Sing|Person=1|PronType=Prs  9   nsubj   _   Phono=jæi
9   overta  overta  VERB    _   VerbForm=Inf    3   conj    _   Phono=åverta
10  den den DET _   Gender=Fem|Number=Sing|PronType=Dem 11  det _   Phono=dænn
11  mjølka  mjølk   NOUN    _   Definite=Def|Gender=Fem|Number=Sing 9   obj _   Phono=mjæLLka
12  au  au  ADV _   _   9   advmod  _   Phono=ævv
13  da  da  ADV _   _   14  advmod  _   Phono=da
14  køyrde  køyre   VERB    _   Mood=Ind|Tense=Past|VerbForm=Fin    3   conj    _   Phono=kjørte
15  vi  vi  PRON    _   Animacy=Hum|Case=Nom|Number=Plur|Person=1|PronType=Prs  14  nsubj   _   Phono=ve
16  .   $.  PUNCT   _   _   3   punct   _   Phono=.
```

Every sentence where the phonetic transcription could be added also has an additional `text_orig` comment.
Sentences where the speaker has a different identity in the LIA transcriptions also have a `corrected_speakerid` comment.
This is the case for files that were renamed either in the LIA project or in the treebank, and the case for any utterances made by the interviewers rather than the dialect informants.
(Note that none of the interviewer utterances come with phonetic transcriptions.)
