# DRAFT by Alfina | Just for testing
from datasets import load_dataset

dataset = load_dataset("conll2003")
print(dataset['train'][:5])