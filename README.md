# Investigating the Effects of Input Structure on Korean Grammar Learning

This repository accompanies the BUCLD abstract titled:  
**"Investigating the Effects of Input Structure on Korean Grammar Learning in Language Models."**

---

## 📚 Project Overview

We explore whether structured input—such as curriculum learning or translated child-directed speech—can improve the ability of language models to learn Korean grammar.  
The model used is GPT-2 (KoGPT2), fine-tuned under four training conditions:

- `original.txt`: randomly ordered input
- `curriculum.txt`: simple-to-complex grammatical ordering
- `variation.txt`: variation sets with repeated forms
- `translated.txt`: translated child-directed speech

---

## 📁 Repository Structure

```
input-structure-korean-lm/
├── data/                  # Preprocessed training data (txt)
├── scripts/               # Training scripts (.py)
├── notebooks/             # Original Jupyter notebooks (.ipynb)
├── environment.yml        # Conda environment for reproducibility
└── README.md
```

---

## 🛠️ How to Run

### 1. Create environment
```bash
conda env create -f environment.yml
conda activate korean-lm
```

### 2. Run training
```bash
python scripts/original_training.py
python scripts/curriculum_training.py
python scripts/variation_training.py
python scripts/translated_training.py
```

---

## 📊 Output

Each model was trained on 10,000 sentences for 3 epochs.  
Evaluation is done using **perplexity** as a proxy for grammar acquisition performance.

---

## 📎 Citation

- Haga et al. (2024). *BabyLM Challenge: Exploring the Effect of Variation Sets on Language Model Training Efficiency.*
- Feng et al. (2024). *Is Child-Directed Speech Effective Training Data for Language Models?*
- Kim & Koo (2024). *Evaluating the Impact of Training Conditions on the Performance of GPT-2-Small Based Korean-English Bilingual Models.*
