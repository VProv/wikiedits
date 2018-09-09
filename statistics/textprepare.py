import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
nltk.download('stopwords')
nltk.download('punkt')


class TextColumnPrepare:
    """
    Class for text preparation
    """
    def __init__(self, tokenizer=RegexpTokenizer(r'\w+')):
        self.tokenizer = tokenizer

    def prepare(self, df, columns):
        """
        df - Pandas Data Frame
        columns - list of strings, name
        """
        for column in columns:
            self.prepare_column(df, column)

    def prepare_column(self, df, column):
        res_list = []
        for string in df[column].values:
            if type(string) == str:
                res_list.append(self.prepare_string(string))
            else:
                res_list.append(string)
        df[column] = res_list

    def prepare_string(self, string):
        """
        Takes string, returns prepared string
        """
        if not isinstance(string, str):
            return ""

        if len(string) < 1:
            return ""

        stop_words = set(stopwords.words('english'))
        word_tokens = self.tokenizer.tokenize(string)
        filtered_sentence = [
            w.lower() for w in word_tokens if w not in stop_words
        ]
        return ' '.join(filtered_sentence)