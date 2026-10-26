# Wanga Nègès – alphabet and sound rules (for your check)

Status: DRAFT 1, 2026-10-26. Written by the rules in `kreyol/g2p.py`, not yet checked by a native speaker.

**How to check:** go through the table and the questions. Tell me in the chat what is wrong, or write ✅ or your
correction in the last column. When you have your dictionary, use it to **check** – we never copy entries from it.

The symbols are only labels for the model: it learns how each one sounds from your recordings. What matters is that
the same sound always gets the same symbol.

## 1. The 32 letters and letter groups

| Letter | Example | Read by the rules as | Your check |
|---|---|---|---|
| **a** | papa | p a p a | |
| **an** | manman | m ã m ã | |
| **b** | bato | b a t o | |
| **ch** | chat | ʃ a t | |
| **d** | dlo | d l o | |
| **e** | bebe | b e b e | |
| **è** | fèt | f ɛ t | |
| **en** | chen | ʃ ɛ̃ | |
| **f** | fanmi | f ã m i | |
| **g** | gato | ɡ a t o | |
| **h** | hach | h a ʃ | |
| **i** | diri | d i ɣ i | |
| **j** | jaden | ʒ a d ɛ̃ | |
| **k** | kay | k a j | |
| **l** | lalin | l a l i n | |
| **m** | mache | m a ʃ e | |
| **n** | nou | n u | |
| **ng** | bilding | b i l d i ŋ | |
| **o** | zo | z o | |
| **ò** | pòt | p ɔ t | |
| **on** | bonbon | b ɔ̃ b ɔ̃ | |
| **ou** | bouch | b u ʃ | |
| **oun** | moun | m u n | |
| **p** | pen | p ɛ̃ | |
| **r** | radyo | ɣ a d j o | |
| **s** | solèy | s o l ɛ j | |
| **t** | tab | t a b | |
| **ui** | uit | ɥ i t | |
| **v** | vant | v ã t | |
| **w** | wout | w u t | |
| **y** | yo | j o | |
| **z** | zanmi | z ã m i | |

What the less common symbols mean:

| Symbol | Sound |
|---|---|
| ã ɛ̃ ɔ̃ | the nasal vowels of *an*, *en*, *on* |
| ũ | nasal *oun*, only where the exception list says so (oungan) |
| ɛ ɔ | open *è*, *ò* |
| ʃ ʒ | *ch*, *j* (French *chat*, *jour*) |
| ɣ | the Kreyòl *r* |
| j w ɥ | *y*, *w*, the *u* of *uit* |
| ŋ | *ng* at the end of *bilding* |
| ɡ | always a hard *g* |

## 2. The rules

1. **an, en, on are nasal** – *manje* → m ã ʒ e, *chen* → ʃ ɛ̃, *bonbon* → b ɔ̃ b ɔ̃.
2. **…but not when a vowel follows the n:** then the n starts the next syllable – *ane* → a n e, *fenèt* → f e n ɛ t.
3. **A grave accent keeps the vowel oral:** *chèn* → ʃ ɛ n (chain) vs *chen* → ʃ ɛ̃ (dog); *pàn* → p a n; *mòn* → m ɔ n.
4. **Double n after a nasal vowel:** *grann* → ɡ ɣ ã n, *konnen* → k ɔ̃ n ɛ̃, *bannann* → b ã n ã n, *anndan* → ã n d ã.
5. **in and oun are not nasal:** *machin* → m a ʃ i n, *moun* → m u n, *kounye* → k u n j e (see Q1, Q2).
6. **ui** = ɥ i: *uit*, *dizuit*.
7. **dj and tch** are just d + j and t + ch: *djòb* → d ʒ ɔ b, *tchala* → t ʃ a l a.
8. **Short pronouns** m, n, l, w, y, k are read as single sounds: *m ap manje* → m | a p | m ã ʒ e.
9. **No apostrophes, no hyphens** (official spelling): *m'ap* is read like *m ap*.
10. **Letters outside the alphabet** (c, q, x, u alone, é…) get a best guess and are flagged for you.
11. **Exception list** `lexicon/exceptions.tsv` wins over the rules. Today it has one word: *oungan* → ũ ɡ ã.

## 3. Questions for you

| # | Question | What the rules do now |
|---|---|---|
| Q1 | **oun:** is it *u + n* in most words (moun, kounye, youn), and nasal only in a few (oungan)? Which other words have a nasal *oun*? | u + n; nasal only via the exception list |
| Q2 | **in:** always *i + n* (machin, lalin, fin)? | always i + n |
| Q3 | **The number 1:** do you say *san en* (101) and *mil en* (1001)? One source writes *mil youn*. And before a noun – "1 liv" = *en liv* or *yon liv*? | always *en* |
| Q4 | **81–99:** we write *katrevenen, katrevende … katrevenuit, katrevennèf, katrevendis, katrevenonz … katrevendiznèf*. The rules then read *katrevenen* as "katre-ve-nen" (the *ven* loses its nasal). How do you say 81, 88 and 91? | see `lexicon/numbers_draft.tsv` |
| Q5 | **r:** always the Kreyòl *r* (radyo, rezon, diri)? | always ɣ |
| Q6 | **Abbreviations and letters:** how do you say CPU, RAM, SSD, HDD, USB, ALU and the quiz letters B and C in your videos? | read letter by letter (wrong) – flagged |
| Q7 | **ng:** only at the end of loanwords like *bilding*, *miting*; *lang* = l ã g? | yes |
| Q8 | **English words** in your script (access, cache, cores, decode, execute, explorer, ultra, script, reel): English sound, or a Kreyòl spelling? | read as Kreyòl letters – flagged |

## 4. Lists to look at

- `lexicon/words_draft.tsv` – the 291 words of your corrected script `SCRIPT_KREYOL_user.md`, most frequent first, with
  how the rules read them. Flagged words are at the end of each line (`abbr`, `foreign`).
- `lexicon/numbers_draft.tsv` – 0 to 100 and some bigger numbers, spelled out and read.

Rebuild both after a change: `python3.12 tools/build_review_sheets.py path/to/your-script.md`

Sources: Wikipedia "Haitian Creole" (orthography and phonology), languagesandnumbers.com (numbers), both read
2026-10-26.
