# GPT from scratch

Let's build a Generative Pre-trained Transformer (GPT), a very much simplified version.</br>
Just a fun version to understand model architecture, datasets and data loaders.</br>
</br>


## Environment setup

```bash
conda create -n python-3.12 python=3.12
```

```bash
pip install --r requirements.txt
```

Install PyTorch from [here](https://pytorch.org/get-started/locally/)

```bash
conda install pytorch pytorch-cuda=12.1 -c pytorch -c nvidia
```

# Code

The main implementations are:

- ```1_bigram.ipynb```, bi-gram model
- ```2_gpt-v1.ipynb```, GTP model.

Then we have two other files:

- ```read_data.py```, it can spit a very large file into small chunks.
- ```torch_examples.ipynb```, just play notebook for torch operations.

## Datasources

- [wizard of oz](https://www.gutenberg.org/ebooks/30852), downloaded the txt and work on it. See ```1_bigram.ipynb```.
- [openwebtext](https://openwebtext2.readthedocs.io). Used in ```2_gpt-v1.ipynb``` but I downloaded it via python first.
- [allen c4](https://huggingface.co/datasets/allenai/c4)

# What's next ...

1. Look into applying ```quantization``` to reduce model size. [paper link](https://arxiv.org/pdf/2305.14314)
2. Understand fine-tune and apply it. [paper link](https://arxiv.org/pdf/2306.09782) 