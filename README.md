# Greetings

A tiny project that exists so you can practise contributing to it.

It prints a greeting in whatever language you ask for:

```bash
python3 greet.py fr Ada
# Bonjour, Ada !
```

## How to contribute

Two things are safe to change, and both are one line of work:

1. **Add a language** to `greetings.json`.
2. **Add your name** to `CONTRIBUTORS.md`.

The lessons that go with this repo walk you through doing that on a branch
and getting it into `main`.

## Rules of the road

- `main` is the shared branch. Nobody types code directly into it.
- Every change starts as a branch, and the branch name says what it does:
  `add-italian`, `fix-typo-readme`.
- One change per branch. Two ideas are two branches.

## Making the build fail, and making it pass

The CI job in `.github/workflows/ci.yml` runs three things, in this order, and
**stops at the first one that fails**:

| # | Step | Passes when |
|---|---|---|
| 1 | `python3 -m json.tool greetings.json` | the file is valid JSON |
| 2 | `python3 test_greet.py` | every test's `assert` is true |
| 3 | `python3 greet.py en Ada` | the program runs without crashing |

CI runs exactly the commands you can run yourself. There is no hidden step, no
secret configuration, and nothing that behaves differently on the server. So:

```bash
python3 test_greet.py
```

**Green here means green there.** Run it before every push and CI will never
surprise you.

### How to make it PASS

Add a language that satisfies all four rules the tests check:

1. The file is still valid JSON — every entry but the last ends in a comma, and
   the last one does **not**.
2. The key is a **two-letter lowercase** code: `it`, not `ITA`, not `italian`.
3. The value contains `{name}`, spelled exactly, with the braces.
4. You did not change the English line.

Before:

```json
{
  "en": "Hello, {name}!",
  "fr": "Bonjour, {name} !",
  "es": "¡Hola, {name}!",
  "de": "Hallo, {name}!"
}
```

After — note the comma that had to be added to the `de` line:

```json
{
  "en": "Hello, {name}!",
  "fr": "Bonjour, {name} !",
  "es": "¡Hola, {name}!",
  "de": "Hallo, {name}!",
  "it": "Ciao, {name}!"
}
```

Check it, and you should see five `ok` lines and `All good.`:

```bash
python3 test_greet.py
python3 greet.py it Marco      # Ciao, Marco!
```

### How to make it FAIL

Any one of these will do it. Each breaks a different step, so the log looks
different every time — which is the point of trying more than one:

| Change | Step that fails | What the log says |
|---|---|---|
| Leave a **trailing comma** after the last entry:<br>`"it": "Ciao, {name}!",` | 1 — JSON | `Illegal trailing comma before end of object`, with the line number |
| Add a greeting with **no `{name}`**:<br>`"it": "Ciao!"` | 2 — tests | `'it' is 'Ciao!' — it never says the person's name` |
| Use a **long code**:<br>`"ita": "Ciao, {name}!"` | 2 — tests | `'ita' is not a two-letter lowercase language code` |
| Use a **capital code**:<br>`"IT": "Ciao, {name}!"` | 2 — tests | `'IT' is not a two-letter lowercase language code` |
| **Change the English line** to `"Hi, {name}!"` | 2 — tests | `the English greeting changed` |
| Misspell the slot as `{Name}` or `{ name }` | 2 — tests | `it never says the person's name` — **and** a second failure, `KeyError: 'Name'`, because the program would crash |

Do it on a branch, never on `main`:

```bash
git switch -c break-it-on-purpose
# make one of the changes above
python3 test_greet.py          # fails here first, before CI ever sees it
git commit -am "Deliberately broken, to watch CI catch it"
git push -u origin break-it-on-purpose
```

### Reading the failure

Do not guess from the red X. Ask:

```bash
gh run list --limit 1              # find the run
gh run view --log-failed           # print only the part that failed
```

The last lines are the ones that matter. Every failure message in this
repository is written to tell you what to change, so read the message before
you read the traceback above it.
