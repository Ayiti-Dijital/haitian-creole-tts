# Haitian Creole TTS – by Ayiti Dijital

Open Kreyòl (Haitian Creole) text-to-speech, built from scratch: our own alphabet and sound rules, a small VITS model
trained only on consented recordings, and a small offline runtime. The models are named after Haitian birds: the
first is **Wanga Nègès**, later ones Pipirit and Jako.

**Status:** step 1 of the roadmap – Kreyòl language foundation. No recordings and no model yet.

## Roadmap

1. **Language foundation** (now) – alphabet, sound rules, numbers, first word list, checked by a native speaker
2. **Recording script** – sentences that cover every Kreyòl sound, from our own texts only
3. **Recordings** – one consented voice; the audio stays private and never goes into this repository
4. **Training** – a small VITS model, trained from scratch
5. **Listening tests** – native speakers rate the voice, a Kreyòl speech recognizer checks the words
6. **First release: Wanga Nègès v0.1** – the code here, the model on Hugging Face

## What is here

| Path | What |
|---|---|
| `kreyol/phones.py` | the phone set and the symbol IDs the model will see |
| `kreyol/g2p.py` | spelling → phones, our own rules plus an exception list |
| `kreyol/normalize.py`, `kreyol/numbers.py` | numbers, money, percent and symbols → words |
| `kreyol/ALPHABET.md` | the alphabet, the rules and open questions – for a native speaker to check |
| `lexicon/exceptions.tsv` | words the rules read wrong (our own entries only, never copied from a dictionary) |
| `lexicon/*_draft.tsv` | generated review lists (words from our own texts, numbers) |
| `tools/build_review_sheets.py` | rebuilds the review lists |

Recordings (`data/`) and training runs (`runs/`) never go into git.

## Check

No packages needed, Python 3.12 or newer:

```bash
python3.12 -m unittest discover -s tests
```

## License

Code: Apache-2.0 (see `LICENSE`). The voice model and the recordings get their own licenses when they exist.
