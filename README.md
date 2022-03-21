# hebrew-w2v
a complete reproducible example of training a word2vec model for Hebrew. if you do not want to reprepare the data or train,
you can download the prepared corpus and model from [here](https://drive.google.com/drive/folders/1RDj6Gaa5t4jtd-VtsAqyZWyk6e7o2Xux?usp=sharing).
basically its the Hebrew wikipedia dump only tokenized with hebpipe, to avoid tokens like "כשכשנבוא".

## data preparation
to run data_preparation run `pip install -r requirements_data.txt` and then `python data_preparation/main.py`. 

wikipedia corpus is downloaded and then split to several files. in each file, articles are separated by a break line.
tokenization *should be done separately* with hebpipe. 
in case of issues with hebpipe, see hebpipe homepage [here](https://github.com/amir-zeldes/HebPipe).
you can then rerun `python data_preparation/main.py` to create the final corpus which will be used for training.

## model training
to train a model, run `pip install -r requirements_train.txt`. note there might be some conflicts with the hebpipe package.
you can then run `python main.py`. the code for training the model and the playground notebook were inspired by 
[this](https://github.com/liorshk/wordembedding-hebrew/blob/master/word2vec.py) repository 