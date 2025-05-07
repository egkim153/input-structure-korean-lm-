# Investigating the Effects of Input Structure on Korean Grammar Learning

This repository accompanies the BUCLD 2024 abstract titled:  
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
python scripts/train.py --condition original
```

You can also run each script individually:
```bash
python scripts/original_training.py
python scripts/curriculum_training.py
```

---

## 📊 Output

| Condition        | Perplexity ↓ |
|------------------|--------------|
| Translated       | **1.03**     |
| Curriculum       | 1.05         |
| Original (random)| 1.32         |
| Variation Sets   | 1.65         |

**Findings:**  
- Structured input (especially Translated and Curriculum) improves learning.
- Variation Sets surprisingly underperformed due to repetition and low diversity.

---

## 📎 Citation

- Haga et al. (2024). *BabyLM Challenge: Exploring the Effect of Variation Sets...*
- Feng et al. (2024). *Is Child-Directed Speech Effective Training Data...*
- Kim & Koo (2024). *GPT-2-Based Korean-English Bilingual Model Study*
