#!/usr/bin/env python
import sys
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords

CRAN_COLL = '/home/mscuser/Datasets/cran/cran.all.1400'
INDEX_FILE = 'cran.ind'

SYMBOLS = '!@#$%^&*()[]{};\':",.<>/?`~-_=+'


def parse_documents(cran_file=CRAN_COLL):
    """Parse the document body and title fields of the Cranfield collection.
    Arguments:
        cran_file: (str) the path to the Cranfield collection file
    Return:
        (body_kwds, title_kwds): where body_kwds and title_kwds are
        dictionaries of the form {docId: [words]}.
    """
    myfile = open(cran_file)
    running_idx = -1
    in_text = 0
    body_kwds = {}
    title_kwds = {}
    for line in myfile:
        if line.startswith('.I'):
            in_text = 0
            running_idx = int(line.split()[1])
        else:
            if line.startswith('.W'):
                in_text = 1
            elif line.startswith('.T'):
                in_text =2
            elif line.startswith('.A')|line.startswith('.B'):
                in_text = 0
        if in_text==2:
            if running_idx in title_kwds:
                title_kwds[running_idx]+= [t for t in line.split()]  
            else:
                title_kwds[running_idx]= [t for t in line.split()]
        elif in_text==1:
            if running_idx in body_kwds:
                body_kwds[running_idx]+= [t for t in line.split()]  
            else:
                body_kwds[running_idx]= [t for t in line.split()]
    print (body_kwds, title_kwds)
    return (body_kwds, title_kwds)


def pre_process(words=["aLoHa,","and","bAg","yEah,weF","initials","initialize"]):
    """Preprocess the list of words provided.
    Arguments:
        words: (list of str) A list of words or terms
    Return:
        a shorter list of pre-processed words
    """
    # Get list of stop-words and instantiate a stemmer:
    stop_words = set(stopwords.words('english'))
    stemmer = PorterStemmer()

    # Make all lower-case:
    words = [x.lower() for x in words]
    # Remove symbols:
    words = [''.join([c if c not in SYMBOLS else '' for c in x]) for x in words]
    # Remove words <= 3 characters:
    words = [x for x in words if len(x) > 3]
    # Remove stopwords:
    words = [x for x in words if x not in stop_words]
    # Stem terms:
    words = map(lambda x: stemmer.stem(x), words)
    return words

def create_inv_index(bodies, titles):
    """Create a single inverted index for the dictionaries provided. Treat
    all keywords as if they come from the same field. In the inverted index
    retail document and term frequencies per the form below.
    Arguments:
        bodies: A dictionary of the form {doc_id: [terms]} for the terms found
        in the body (.W) of a document
        titles: A dictionary of the form {doc_id: [terms]} for the terms found
        in the title (.T) of a document
    Return:
        index: a dictionary {docId: [df, postings]}, where postings is a
        dictionary {docId: tf}.
        E.g. {'word': [3, {4: 2, 7: 1, 9: 3}]}
               ^       ^   ^        ^
               term    df  docid    tf
    """
    # Create a joint dictionary with pre-processed terms


def load_inv_index(filename=INDEX_FILE):
    """Load an inverted index from the disk. The index is assummed to be stored
    in a text file with one line per keyword. Each line is expected to be
    `eval`ed into a dictionary of the form created by create_inv_index().

    Arguments:
        filename: the path of the inverted index file
    Return:
        a dictionary containing all keyworks and their posting dictionaries
    """


def write_inv_index(inv_index, outfile=INDEX_FILE):
    """Write the given inverted index in a file.
    Arguments:
        inv_index: an inverted index of the form {'term': [df, {doc_id: tf}]}
        outfile: (str) the path to the file to be created
    """


def eval_conj(inv_index, terms):
    """Evaluate the conjunction given in list of terms. In other words, the
    list of terms represent the query `term1 AND term2 AND ...`
    The documents satisfying this query will have to contain ALL terms.
    Arguments:
        inv_index: an inverted index
        terms: a list of terms of the form [str]
    Return:
        a set of (docId, score) tuples -- You can ignore `score` by
        substituting it with None
    """
    # Get the posting "lists" for each of the ANDed terms:
    
    # Basic AND - find the documents all terms appear in, setting scores to
    # None (set scores to tf.idf for ranked retrieval):


def eval_disj(conj_results):
    """Evaluate the conjunction results provided, essentially ORing the
    document IDs they contain. In other words the resulting list will have to
    contain all unique document IDs found in the partial result lists.
    Arguments:
        conj_results: results as they return from `eval_conj()`, i.e. of the
        form {(doc_id, score)}, where score can be None for non-ranked
        retrieval. 
    Return:
        a set of (docId, score) tuples - You can ignore `score` by substituting
        it with None
    """
    # Basic boolean - no scores, max(tf.idf) for ranked retrieval:


def main():
    """Load or create an inverted index. Parse user queries from stdin
    where words on each line are ANDed, while whole lines between them are
    ORed. Match the user query to the Cranfield collection and output matching
    documents as "ID: title", each on its own line, on stdout.
    """

    # If an index file exists load it; otherwise create a new inverted index
    # and write it into a file (you can use the variable INDEX_FILE):
    try:
        file = open(INDEX_FILE)
    except IOError as e:
        parse_documents()
    pre_process()
    # Get and evaluate user queries from stdin. Terms on each line should be
    # ANDed, while results between lines should be ORed.
    # The output should be a space-separated list of document IDs. In the case
    # of unranked boolean retrieval they should be sorted by document ID, in
    # the case of ranked solutions they should be reverse-sorted by score
    # (documents with higher scores should appear before documents with lower
    # scores):


if __name__ == '__main__':
    main()
