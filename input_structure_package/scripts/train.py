import argparse

def train_model(condition):
    print(f"Training GPT-2 model with condition: {condition}")
    # Training logic would go here...

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--condition", type=str, default="original",
                        help="Training condition: original, curriculum, variation, translated")
    args = parser.parse_args()
    train_model(args.condition)
