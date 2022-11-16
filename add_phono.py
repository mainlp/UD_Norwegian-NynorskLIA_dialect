from glob import glob


# Two of the files have different names in the LIA version and the
# treebank version.
speaker_map = {"farsund_uib_02": "lista_uib_05",
               "lierne_uio_01": "nordli_uio_01"}

# Phrases necessary to replace in the treebank version
# in order to find the corresponding entries in the
# original LIA transcripts.
replacements = {
    "aal_uio_02": {
        # Mistakes in the LIA file
        "som e ": "som ee ",
        "bar-": "bar-)",
        # Mistake in treebank file:
        "rep": "var",
    },
    "austevoll_uib_01": {
        # Typo in the LIA file (nooko), different spellings of "følg(j)er"
        "noko sånt spesielt men # du følger":
            "nooko sånt spesielt men # du følgjer",
        # Mistakes in the LIA file:
        "sånn": "sånn)",
        "meir": "meire",
        "for min del": "for min det",
        "halvtanna": "halvanna",
    },
    "austevoll_uib_04": {
        # Different analyses:
        "to-tre": "to tre",
    },
    "bardu_uit_01": {
        # Mistakes in the LIA file:
        "s- sånn": "s sånn",
        "det e ": "det ee ",
        # Mistake in the treebank file:
        "par du": "veit du",
    },
    "eidsberg_uio_03": {
        # Mistakes in the LIA file
        "Mysen": "Mysn",
        "leverandøren": "levvrandøren",
        "anna": "annaa",
        "og lass": "å lass",
        "og dei": "å dei",
        "og så": "å så",
        "knupp": "x_knupp",
        "strekar": "streker",
        "køyrt": "# køyrt",
        "så det gjekk fint": "(så det gjekk fint)",
        "langvarig": "lanngvari",
        "blei aldri": "blei ældri",
        "tyskarane": "tysskarane",
    },
    "farsund_uib_02": {
        # Anonymized names
        "farsund_uib_0201": "lista_uib_0501",
        # Mistakes in the LIA file:
        "steller med i løpet av ein sånn alminneleg dag # korleis de # får":
            "stellar med i løpet av ein sånn almindeleg dag # "
            "korleis de # for",
        # -- steller, alminneleg, får.
        #    I think 'de' should be 'du' in both versions.
        "eg har": "eg her",
    },
    "flakstad_uib_04": {
        # Mistakes in the LIA file:
        "reiskap": "reidskap",
        "kommunestyra": "komunstyra",
        "og den e": "og denn e",
        "sjøvêr": "sjøver",
        # -- Elsewhere in the same sentence,
        #    vêr is written with the circumflex.
        "betale den": "betale dedn",
        "kyrkjegarden": "kyrjkegarden",
        "forsvann": "forvann",
        "høvedsmann": "høvedsmannn",
        "oppdaga": "opdaga",
        "gjorde": "gjode",
    },
    "giske_uib_02": {
        # Mistakes in the LIA file:
        "kanskje": "kansje",
        "minne": "minnne",
        "bergensmuseet": "bergensmuseumet",
        "Ålesund": "Ålesunnd",
        "e å seie": "e) å seie",
        "nordsida": "norsida",
        "sørvest": "søvesst",
        "det har vore": "det her vore",  # (I think this is a LIA mistake)
        "er det berre å sette plogen": "er det berre og sette plogen",
        "stått": "ståt",
        "store": "storr",
        "aktuelt": "aktuellt",
        "stemde": "stemd",
        " m- ": " m ",
        "skalleseien": "skallesæien",
        "på e": "på- e",
        "driv": "idriv",
        # Mistakes in the treebank version
        # (caused by "forbidden" spaces between an avhengig tagg
        # and the parenthesis)
        "(som": "som",
        "(trur eg enn det": "trur eg enn det",
        "(at det": "at det",
        "(og tok det opp det": "og tok det opp det",
        "(frå e vest-": "frå e vest-",
        "(skjebba": "skjebba",
        "(ja": "ja",
    },
    "gol_uio_01": {
        # Mistake in the treebank file:
        "plage o- lage": "plage o- plage",
    },
    "lierne_uio_01": {
        # Anonymized names
        "lierne_uio_0101": "nordli_uio_0101",
        "lierne_uio_0103": "int",
        # Mistakes in the LIA file:
        "skurknamnet": "skurknammnet",
        "kanskje": "kankje",
        "forsøk": "førsøk",
        "skulle ha": "skulle har",
    },
    "vardoe_uio_01": {
        # Mistakes in the LIA file:
        "passasjerar": "pasasjerar",
        "til og med": "til og ned",
        "komme": "kommme",
        "eg såg lysa": "eg så lysa",
        # -- I think it's the LIA file that has the typo
    },
}

# Mistakes in the treebank or LIA files that make
# alignment difficult, because of merged utterances,
# word substitutions or missing words.
# (Mostly treebank mistakes.)
ignore = {
    "aal_uio_02": (
        "så ville vi ha ville vi ha e ha e køyring så måtte vi vi ta det "
        "ettersom dei hadde bestemt det til # ja .",
        # -- det ettersom vs. det vi ettersom (checked audio: vi)
    ),
    "austevoll_uib_01": (
        "så eg trur det er mykje oppblåse og det er ein liten # "
        "ei lita gruppe som får .",  # og vs. __
        "men helst for du jo # ikkje det du har jo ikkje # "
        "er jo forskjellig ifrå folk # forskjellige meiningar men .",
        # -- ifrå vs. __
        "ja # båtar # teiknarbåtar og # berekning og # forskjellig sånn .",
        # -- teiknarbåtar vs. teiknar båtar
        #    (the latter makes much more sense in context)
        "om du skal # evakuere ei # ja hundre menneske da veit du "
        "så # må du ha plass til dei òg .",
        # -- om vs. __ (checked audio: utterance starts with 'du skal')
    ),
    "austevoll_uib_04": (
        "kva tid kom e snurpenota i bruk "
        "e ja den var nå vel kommen antakeleg i bruk føre mine dagar .",
        # -- Merged interviewer + interviewee.
        #    Also a typo in LIA file: snu[u]rpenota
        "det vart annan måte kanskje ?",
        # -- annan vs. ein annan
    ),
    "eidsberg_uio_03": (
        "det var tungvint? ja # det var e tungvint .",
        # -- Merged interviewer + interviewee utterance
        "og det var # så det var da bra .",  # "var da" vs. "gjekk da"
        "å den Hesselman den # kjøpte eg # den kjøpte eg fjorten tusen for .",
        # -- kjøpte vs. gav
        "% det var det var jo absolutt nå var det jo heilt noko anna nå # "
        "med dieselen i dag enn det var den tid .",  # er vs. var
        "dei # dei hadde hadde det verre liv i .",
        # -- LIA: dei # dei var det ja det var det liv i
        "dei køyrde jo var lastebilen mykje og .",  # var vs. er
        "det første # det # i femogtjue .",
        # -- LIA version is much longer (and has a typo):
        #    ja det første eg begynte # det var # i femmogtjue .
        "og det første eg # å køyre til byen # "
        "så måtte eg vere i byen når ho var fem om morgonen .",
        # -- det første eg vs. det første eg begynte (checked audio: begynte)
    ),
    "farsund_uib_02": (
        "# ja han hostar gansk- . … .",  # merged interviewee + interviewer
    ),
    "flakstad_uib_04": (
        "» # så skal du seie « han er » … .",
        # -- » vs. __ (sentence splitting mishap;
        #    also affects previous treebank entry)
        "# drått og så? dråtten i skodda ja dråtten # "
        "det kalla du for « dråtten » .",
        # -- Merged interviewer and interviewee
        "ja . … .",
        # -- Merges two interviewer utterances
        #    (arguably not a mistake)
        "på tvers ut ifrå # ? - … .",
        # -- Merged interviewer and interviewee
    ),
    "giske_uib_02": (
        "det er må ein helst e å seie er nokså dårleg etter så som e # "
        "tida krev det nå .",
        # -- det er må vs. det må; LIA version has e) instead of e
        "ja det har vore nokre nye hus nå # i det siste ikkje krigen men .",
        # -- vore nokre vs. vore bygt nokre
        "så det blir ofte til det at det at e # ungdommen han e .",
        # -- det at det at vs. det at det
        "han kan kan seie det at # einaste karane som er heime "
        "det er postopnaren og læraren # eg trur ikkje her er stort andre ."
        " # .",
        # -- Superfluous final # . (merged with following interviewer response)
        "tidlegare så har du desse øyane som nå e # omfatta Giske "
        "dei høyrde med til Borgund kommune .",
        # -- Giske vs. Giske kommune (checked audio: kommune)
        "jaha # kor lang e e tid e tek ein slik tur "
        "for eksempel til Færøyane eller til Island? "
        "e er det same e like langt eller e # er det .",
        # -- Merged interviewer + interviewee
        "jaha # men em # dette fisket her altså på e Færøyane og på Island e "
        "kor lenge held dei på med det utover hausten? "
        "ja # på Island e brukar ikkje dei å ligge så svært lenge utover "
        "hausten for det er så langt dit .",
        # -- Merged interviewer + interviewee
        "er det nokon plass spesielt her der e "
        "der e denne her fuglen e legg reir? eller har reir ?"
        # -- Merges two interviewer utterances
        #    (arguably not a mistake)
    ),
    "lierne_uio_01": (
        "men det har ikkje eg høyrt før enn veit du dei tala i det "
        "men han sa det at .",  # i vs. til
        "ja e dadet blir e # ja det blir jo .",  # dadet vs. da det
        "ein kjese ? … .",  # merged interviewee + interviewer utterance
        "men da # er vi einige om at du lagar deg ein liten lapp da "
        "og skriv opp det du kjempå .",  # kjempå vs. kjem på
        "men det vart til det al- pøyken han han heldt i hesten "
        "ja det var ikkje saka .",
        # -- al- vs. al. But I think it actually should be "at"  (phono is "t")
    ),
    "vardoe_uio_01": (
        "det var vel kanskje skal seie # ja ja eg jo .",  # eg jo vs. eg kan jo
        "det det med austavind for eksempel # nå korleis det ?",
        # -- korleis vs. korleis blei
    ),
}

# Changes that need to be made to the phonetic LIA
# transcriptions in order to enable a token-wise
# alignment with the treebank.
alignment_fix = {
    "austevoll_uib_04": (("to tre", "to-tre"), ),
    "eidsberg_uio_03": (("få # kjørt", "få kjørt"),
                        ("(re) ", ""))
}


def look_up_speaker(speaker):
    return speaker_map.get(speaker, speaker)


def get_speakers(glob_path):
    speakers = set()
    for in_file in glob(glob_path):
        with open(in_file) as f:
            for line in f:
                if line[0] != "#":
                    continue
                cells = line.split("speakerid: ")
                if len(cells) == 1:
                    continue
                speaker = cells[1].strip()
                speakers.add(speaker)
    return speakers


def clean_utterance(utt):
    # Based on the transcription guidelines, pp. 18--19,
    # "Generelle prinsipp for taggar" &
    # "Liste over avhengige og uavhengige taggar med tyding",
    # https://tekstlab.uio.no/LIA/pdf/transkripsjonsrettleiing_lia.pdf
    # and the transliteration guidelines, p. 3, "X-tagg",
    # https://tekstlab.uio.no/LIA/pdf/rettleiing-translitterator.pdf
    for symb in ("%u", "%u-", "%l", "%g", "%v",
                 "%y", "%k", "%s", "%q", "%o", "%p"):
        utt = utt.replace(symb, "")
    utt = utt.replace("+x_", "")
    for symb in ("+u", "+l", "+g", "+v", "+y", "+s"):
        if symb not in utt:
            continue
        while symb + "(" in utt:
            idx_start = utt.index(symb + "(")
            idx_end = utt.index(")", idx_start)
            utt = utt[:idx_start] + utt[idx_start + 3:idx_end]\
                + utt[idx_end + 1:]
        while symb + " (" in utt:
            # This is against the transcription guidelines,
            # but happens in a bunch of files.
            idx_start = utt.index(symb + " (")
            idx_end = utt.index(")", idx_start)
            utt = utt[:idx_start] + utt[idx_start + 4:idx_end]\
                + utt[idx_end + 1:]
        utt = utt.replace(symb + " ", "")
        utt = utt.replace(" " + symb, "")
    while "{" in utt:
        # comment between { }
        idx_start = utt.index("{")
        idx_end = utt.index("}", idx_start)
        utt = utt[:idx_start] + utt[idx_end + 1:]
    utt = utt.strip()
    if not utt:
        return ""
    # In most cases in the LIA files (and in all(?) cases in the UD files),
    # guillemets are surrounded by whitespace, with some (irregular)
    # exceptions in farsund_uib_02 and gol_uio_01
    utt = utt.replace("«", "« ")
    utt = utt.replace("»", " »")
    if utt[-1] not in (".", "!", "?"):
        utt += " ."
    while "  " in utt:
        utt = utt.replace("  ", " ")
    return utt


def is_interviewer(speaker):
    for name in ("int", "INT", "hh", "khs"):
        if speaker.startswith(name):
            return True
    return False


def add_utt(speaker_norm, speaker_cur, ortho, phono, speaker2ortho2phon):
    if is_interviewer(speaker_cur):
        speaker_cur = "INTERVIEWER_" + speaker_norm
    else:
        speaker_cur = speaker_norm
    ortho = clean_utterance(ortho)
    phono = clean_utterance(phono)
    if not ortho or not phono:
        return
    try:
        speaker2ortho2phon[speaker_cur][ortho] = phono
    except KeyError:
        speaker2ortho2phon[speaker_cur] = {}
        speaker2ortho2phon[speaker_cur][ortho] = phono
    # Some utterances are split along these symbol boundaries,
    # others aren't. Adding both versions here.
    for symb in ("? ", "» "):
        orthos = []
        phonos = []
        ortho_end = ortho
        phono_end = phono
        while symb in ortho_end:
            idx = ortho_end.index(symb)
            if idx == len(ortho_end) - 1:
                break
            ortho_start, ortho_end = ortho_end.split(symb, 1)
            phono_start, phono_end = phono_end.split(symb, 1)
            orthos.append(ortho_start + symb[0])
            phonos.append(phono_start + symb[0])
        orthos.append(ortho_end)
        phonos.append(phono_end)
        for ortho, phono in zip(orthos, phonos):
            speaker2ortho2phon[speaker_cur][ortho] = phono


def get_speaker2ortho2phono():
    speaker2ortho2phono = {}
    for speaker in get_speakers("UD_Norwegian-NynorskLIA/*.conllu"):
        speaker_norm = look_up_speaker(speaker)
        for in_file in glob("lia_norsk/" + look_up_speaker(speaker_norm)
                            + "*.ort.txt"):
            with open(in_file) as f:
                speaker_cur = None
                ortho = ""
                phono = ""
                for line in f:
                    if line[0] == "\n":
                        if phono and ortho:
                            add_utt(speaker_norm, speaker_cur, ortho, phono,
                                    speaker2ortho2phono)
                            ortho = ""
                            phono = ""
                        speaker_cur = None
                    elif line.startswith(speaker_norm) or is_interviewer(line):
                        # The UD version also includes the interviewers'
                        # utterances. Those aren't transcribed phonetically
                        # in the transcription files.
                        # In the UD version, the interviewers' speaker IDs are
                        # replaced with their informants' speaker IDs.
                        speaker_cur, utt = line.split(" ", 1)
                        if speaker_cur.endswith("orthography"):
                            ortho = utt.strip()
                        else:
                            phono = utt.strip()
                    elif speaker_cur and line[0] == " ":
                        if speaker_cur.endswith("orthography"):
                            ortho += " " + line.strip()
                        else:
                            phono += " " + line.strip()
            if phono and ortho:
                add_utt(speaker_norm, speaker_cur, ortho, phono,
                        speaker2ortho2phono)
    return speaker2ortho2phono


def find_phono(speaker, ortho, speaker2ortho2phono):
    actual_speaker = look_up_speaker(speaker)
    phono = None
    try:
        phono = speaker2ortho2phono[actual_speaker][ortho]
    except KeyError:
        interviewer = "INTERVIEWER_" + actual_speaker
        try:
            phono = speaker2ortho2phono[interviewer][ortho]
            actual_speaker = interviewer
        except KeyError:
            if speaker in replacements:
                repls = replacements[speaker]
                for repl in repls:
                    updated_ortho = ortho.replace(repl,
                                                  repls[repl])
                    try:
                        phono = speaker2ortho2phono[
                            actual_speaker][updated_ortho]
                    except KeyError:
                        try:
                            phono = speaker2ortho2phono[
                                interviewer][updated_ortho]
                            actual_speaker = interviewer
                            break
                        except KeyError:
                            pass
    return phono, actual_speaker


def add_dialect_to_misc(f_out, speaker, phono, word_entries):
    dialect_words = phono.split(" ")
    if len(dialect_words) != len(word_entries):
        fixed = False
        if speaker in alignment_fix:
            for fix in alignment_fix[speaker]:
                dialect_words = phono.replace(fix[0], fix[1]).split(" ")
                if len(dialect_words) == len(word_entries):
                    fixed = True
                    break
        if not fixed:
            print("/!\\ Dialect words and token entries don't match:")
            print(f"{len(dialect_words)} dialect words,"
                  f"{len(word_entries)} token entries")
            print(speaker)
            print(dialect_words)
            for dial, entry in zip(dialect_words, word_entries):
                print(dial, entry[:10])
            return False
    for dial, entry in zip(dialect_words, word_entries):
        main, _, misc = entry.rpartition("\t")
        if misc == "_":
            misc = ""
        else:
            misc += "|"
        misc += "Phono=" + dial
        f_out.write(main + "\t" + misc + "\n")
    return True


def make_dialect_file(in_file, speaker2ortho2phono):
    out_file = in_file.split("/")[-1].replace("nynorsklia-",
                                              "nynorsklia_dialect-")
    with open(in_file) as f_in:
        with open(out_file, "w+", encoding="utf8") as f_out:
            ortho = None
            phono = None
            speaker = None
            actual_speaker = None
            word_entries = []
            ignore_phono = False
            for line in f_in:
                if not line.strip():
                    if ignore_phono or\
                            actual_speaker.startswith("INTERVIEWER_"):
                        ignore_phono = False
                        for entry in word_entries:
                            f_out.write(entry + "\n")
                    else:
                        success = add_dialect_to_misc(f_out, speaker,
                                                      phono, word_entries)
                        if not success:
                            return False
                    word_entries = []
                    f_out.write(line)
                    continue
                if line[0] != "#":
                    word_entries.append(line.strip())
                    continue
                cells = line.split("text = ")
                if len(cells) == 2:
                    ortho = cells[1].strip()
                    f_out.write(line)
                    continue
                cells = line.split("speakerid: ")
                if len(cells) == 1:
                    f_out.write(line)
                    continue
                speaker = cells[1].strip()
                try:
                    if ortho in ignore[speaker]:
                        f_out.write(line)
                        ignore_phono = True
                        continue
                except KeyError:
                    pass
                phono, actual_speaker = find_phono(speaker, ortho,
                                                   speaker2ortho2phono)
                ignore_phono = False
                if not phono:
                    print("/!\\ Couldn't find the following utterance")
                    print(speaker)
                    print(ortho)
                    return False
                if not actual_speaker.startswith("INTERVIEWER_"):
                    f_out.write("# text_orig = " + phono + "\n")
                f_out.write(line)
                if actual_speaker != speaker:
                    f_out.write(f"# corrected_speakerid: {actual_speaker}\n")
        if word_entries:
            success = add_dialect_to_misc(f_out, speaker, phono, word_entries)
            return success
    return True


if __name__ == "__main__":
    speaker2ortho2phono = get_speaker2ortho2phono()
    for filename in glob("UD_Norwegian-NynorskLIA/*.conllu"):
        success = make_dialect_file(filename, speaker2ortho2phono)
        if not success:
            break
