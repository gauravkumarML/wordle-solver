# Wordle Solver

A simple Wordle-solver that:

* Loads a list of five-letter words (scraped)
* Filters candidates by Wordle-style feedback
* Recommends next guesses using a frequency-based heuristic
* Visualizes candidate scores in a bar chart

---

## Project Evolution

This solver started as a quick prototype to automate the popular Wordle puzzle.

**Initial idea:** load the official five-letter word lists and repeatedly filter them based on green/yellow/gray feedback from the game.

Considered two scoring approaches:

1. **Entropy-based** (Bayesian) scoring—compute the expected information gain for every possible guess by simulating feedback patterns and applying Shannon entropy.
2. **Frequency-heuristic**—build letter-frequency distributions (positional and overall) from the remaining candidates and score words via a closed-form formula.

**Why heuristic?:** the entropy method requires $O(G \times N\times L)$ simulations (over 100 million ops), leading to some delays.  The frequency-heuristic runs in $O(N)$ time with instant results and high accuracy.

**Final model:** each word $w = w_0w_1w_2w_3w_4$ is scored by:

* score(w) = sum_{i=0}^4 p_{i,w_i} + sum_{l ∈ unique(w)} p_any(l)

* $p_{i,\ell}$ = fraction of current candidates with letter $\ell$ in position $i$.
* $p_{\mathrm{any}}(\ell)$ = fraction of all letter-slots occupied by $\ell$.

This generates strong next-guess recommendations.

---

## Files

* `README.md` — project overview & evolution
* `wordle_solver.py` — main CLI tool with filtering, recommendation, plotting
* `scraper.py` — python script to webscrap desired words file - `five_letter_words.txt`, from wordfind.com
* `five_letter_words.txt` — generated word list
* `requirements.txt`

---

## Installation

```bash
git clone https://github.com/gauravkumarML/wordle-solver.git
cd wordle-solver
pip install -r requirements.txt
```

## Usage

1. **Generate** or update your word list:

   ```bash
   python scraper.py
   ```

2. **Run** the solver:

   ```bash
   python wordle_solver.py five_letter_words.txt
   ```

3. **Commands**:

   * `<guess> <feedback>` (e.g. `crane gybgb`)
   * `plot` → bar chart of current candidate scores
   * `quit` → exit

---
