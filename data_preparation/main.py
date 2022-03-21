from base import get_absolute_path
from create_corpus import download_corpus, corpus_to_text
import split_corpus
from postprocess_hebpipe import process_files
from tokenize_hebpipe import run_hebpipe_command

config = {
    "WIKIFILE": "hewiki-latest-pages-articles.xml.bz2",
    "CORPUS_OUTPUT": get_absolute_path("wiki.he.txt"),
    "SPLIT_CORPUS_EVERY": 100,
    "SPLIT_CORPUS_OUTPUT_FOLDER": get_absolute_path("output"),
    "TOKENIZED_CORPUS_FOLDER": get_absolute_path("tokenized_output"),
    "TOKENIZED_CORPUS": get_absolute_path("wiki_tokenized.he.txt")
}
if __name__=="__main__":
    ### download and save to file ###
    WIKIFILE = config['WIKIFILE']
    zipped_corpus_path = get_absolute_path(WIKIFILE)
    raw_corpus_path = config['CORPUS_OUTPUT']

    download_corpus(url=f"https://dumps.wikimedia.org/hewiki/latest/{WIKIFILE}", dump_path=zipped_corpus_path)
    corpus_to_text(raw_corpus_path, zipped_corpus_path)
    ##################################

    ### split corpus, so it will be easier to process with hebpipe ###
    SPLIT_EVERY = config['SPLIT_CORPUS_EVERY']
    split_corpus_folder = config["SPLIT_CORPUS_OUTPUT_FOLDER"]
    split_corpus.split(raw_corpus_path, split_corpus_folder, SPLIT_EVERY)
    ###################################################################

    ### get hebpipe tokenization command ###
    tokenized_corpus_folder = config["TOKENIZED_CORPUS_FOLDER"]
    run_hebpipe_command(split_corpus_folder, tokenized_corpus_folder)
    #############################

    ### post process tokenized hebpipe output ###
    tokenized_corpus = config["TOKENIZED_CORPUS"]
    process_files(tokenized_corpus_folder, tokenized_corpus)
    #############################################
