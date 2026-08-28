# Lesson 1 — contribute by merging your own branch

This is the flow for a small team where everyone is trusted to push to `main`:
you do the work on a branch, you check it, you merge it yourself.

You need push access to this repository (you own it, or you were added as a
collaborator).

## The eight commands

```bash
# 1. Get your own copy of the repository.
git clone https://github.com/gopanair/git-lesson-branch-merge.git
cd git-lesson-branch-merge

# 2. Start from an up-to-date main.
git switch main
git pull

# 3. Make a branch. The name is a promise about what is on it.
git switch -c add-italian

# 4. Do the work: add "it": "Ciao, {name}!" to greetings.json,
#    and add your name to CONTRIBUTORS.md.

# 5. Check it before anyone else has to.
python3 test_greet.py
python3 greet.py it Marco

# 6. Record the change.
git add greetings.json CONTRIBUTORS.md
git commit -m "Add Italian greeting"

# 7. Merge it into main.
git switch main
git pull                     # someone else may have landed something
git merge add-italian
python3 test_greet.py        # the merged result is what ships, so test that

# 8. Publish, and clean up.
git push
git branch -d add-italian
```

## Why each step is there

- **`git pull` before you branch** — you want your work to sit on top of what
  is already true, not on top of yesterday.
- **A branch at all** — `main` stays working the whole time you are halfway
  through. If you abandon the idea, you delete the branch and nothing happened.
- **`git pull` again before the merge** — this is the step people skip. Between
  step 3 and step 7 someone else may have pushed. Pulling first means the
  conflict, if there is one, happens on your machine where you can look at it,
  rather than as a rejected push.
- **Testing after the merge, not just before** — your branch passed and their
  branch passed; that is not the same as the combination passing.

## If the merge stops with a conflict

Git will tell you which file. Open it, and you will see both versions marked:

```
<<<<<<< HEAD
  "de": "Hallo, {name}!"
=======
  "de": "Hallo, {name}!",
  "it": "Ciao, {name}!"
>>>>>>> add-italian
```

Delete the markers, leave the text you actually want, then:

```bash
git add greetings.json
git commit          # finishes the merge
```

`git merge --abort` puts everything back if you would rather start over.

## The exercise

Add a language of your own, on a branch named after it, and land it in `main`.
Then run `git log --oneline --graph` and find your commit.
