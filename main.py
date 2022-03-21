from base import get_absolute_path
from train_model import train_model

if __name__ == "__main__":
    config = {
        "MODEL_PATH": get_absolute_path("model.mdl"),
        "TOKENIZED_CORPUS": get_absolute_path("wiki_tokenized.he.txt"),
        "SEED": 1984
    }
    seed = config['SEED']
    model_dump_path = config['MODEL_PATH']
    tokenized_corpus = config['TOKENIZED_CORPUS']
    model = train_model(tokenized_corpus, seed)
    model.save(str(model_dump_path))
