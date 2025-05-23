# -*- coding: utf-8 -*-
"""translated_training.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gAG3pRpFBMqPFuFpBPVJoTtuzVE_st_Z
"""

!pip install datasets

from datasets import load_dataset

# Tatoeba dataset
dataset = load_dataset("tatoeba", "en-mr", split="train")

english_sentences = [item['translation']['en'] for item in dataset]

# short and simple english sentance (단어 수 4~12개)
filtered_sentences = [s for s in english_sentences if 4 <= len(s.split()) <= 12]

# 500 sentances sampling
sampled_english = filtered_sentences[:500]

# check
for i in range(5):
    print(sampled_english[i])

# install googletrans
!pip install googletrans==4.0.0-rc1

from googletrans import Translator

translator = Translator()

# auto translated
translated_sentences = []

for sentence in sampled_english:
    try:
        translated = translator.translate(sentence, src='en', dest='ko')
        translated_sentences.append(translated.text)
    except Exception as e:
        print(f"Failure: {sentence} | error: {e}")

# check
for i in range(5):
    print(translated_sentences[i])

print(f"translated_sentences: {len(translated_sentences)}개")

import random

# Replicate 479 sentences multiple times to create 10,000 examples
multiplied_sentences = (translated_sentences * (10000 // len(translated_sentences) + 1))[:10000]
random.shuffle(multiplied_sentences)

# Save to file
with open("translated_ordered.txt", "w", encoding="utf-8") as f:
    for line in multiplied_sentences:
        f.write(line + "\n")

print("translated_ordered.txt file created successfully!")

from google.colab import files
files.download("translated_ordered.txt")

✅ Colab code to freshly create translated_ordered.txt for training

# 1. Install libraries
!pip install -U transformers datasets

# 2. Upload translated_ordered.txt
from google.colab import files
uploaded = files.upload()

# 3. Load and split the text
def load_dataset_from_txt(file_path):
    from datasets import Dataset
    import random

    with open(file_path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    random.shuffle(lines)
    split1 = int(0.9 * len(lines))
    split2 = int(0.95 * len(lines))
    train_lines = lines[:split1]
    val_lines = lines[split1:split2]
    test_lines = lines[split2:]

    train_dataset = Dataset.from_dict({"text": train_lines})
    val_dataset = Dataset.from_dict({"text": val_lines})
    test_dataset = Dataset.from_dict({"text": test_lines})

    return train_dataset, val_dataset, test_dataset

train_dataset, val_dataset, test_dataset = load_dataset_from_txt("translated_ordered.txt")

# 4. Load model and tokenizer
from transformers import GPT2LMHeadModel, GPT2TokenizerFast

tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

tokenizer.pad_token = tokenizer.eos_token
model.config.pad_token_id = tokenizer.pad_token_id

# 5. Tokenize dataset
def tokenize_function(example):
    encoding = tokenizer(
        example["text"],
        truncation=True,
        padding="max_length",
        max_length=128
    )
    encoding["labels"] = encoding["input_ids"]
    return encoding

tokenized_train = train_dataset.map(tokenize_function, remove_columns=["text"])
tokenized_val = val_dataset.map(tokenize_function, remove_columns=["text"])

# 6. Set training arguments
from transformers import TrainingArguments, Trainer

training_args = TrainingArguments(
    output_dir="./results-translated",
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    num_train_epochs=3,
    save_strategy="epoch",
    logging_dir="./logs",
    logging_steps=100,
    report_to="none",
    fp16=True
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_train,
    eval_dataset=tokenized_val,
)

# 7. Train model
trainer.train()

# 8. Save model
trainer.save_model("checkpoint-translated")

# 9. Evaluate Perplexity
import math

eval_results = trainer.evaluate()
print(f">>> Perplexity: {math.exp(eval_results['eval_loss']):.2f}")

# 10. Download model checkpoint
!zip -r checkpoint-translated.zip checkpoint-translated
files.download("checkpoint-translated.zip")