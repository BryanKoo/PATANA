# PATANA
PATent ANAlysis project 

Patent or patent text is a an official document conferring the exclusive right granted by a government to an inventor to manufacture, use, or sell an invention for a certain number of years.
Prior arts for a patent are searched many times during the life cycle of a patent.
It is because novelty is one of the most important factor for determining patentability.

## Life cycle of patents
* Preparation of an application
* Pre-grant prosecution
  * Filing an application
  * Search and examination
* Post-grant prosecution

PATANA project is about development of AI NLP algorithm based on up-to-date ML technology for patents.
Patents are written with natural written language, not spoken language, in technology domain.
Though it may be difficult yet for AI to determine whether a patent have novelty or not.
AI can help human by suggesting search term and/or screening irrelevant patents from search results.

This project starts with the problem solving of screening irrelevant patents for Korean patents first.
It can be called as patana1ko sub-project of PATANA.
Working with other languages and suggesting search term will be followed.

## Problem description
Search by keyword has been the way of finding prior arts.
Elastic search, Apache solar, lucene are examples of search engine that can be used for searching by keyword.
The search engines have their own relevence ranking based on a word occurence counting called tf-idf.
This relevence ranking is not very satisfactory for checking whether a patent has similar idea to another one.
Sreening irrelevant patents is done by human after reading considerable portion of each patent from search result.
If an AI technology can screen irrelevant patents from search results, it will reduce cost for patent drafting, refining, examining.

## Software requiremants of the patana1ko
* Develop AI-based software that calculated distance between any 2 korean patents
  * Similar patents should be close to each other
  * A patent and its prior art should be close to each other
  * Patents with different topic should not be close to each other
  * Patents with different classifications should not be close to each other

## How to calculate distance between two patents
Technology for comparing generic documents is not mature yet.
Patents are relatively well-formed and they have nice meta data that can be used for validation of algorithm.
Experiments are needed to know which part should be compared to calculated distance efficiently and precisely.

Baseline for the calculation is the paragraph vector disclosed by Le & Mikolov. https://cs.stanford.edu/~quocle/paragraph_vector.pdf

Another way of the distance calculation is the word mover's distance disclosed by Kusner et. al.
http://proceedings.mlr.press/v37/kusnerb15.pdf

## Process breakdown
* Scrape patents
* Extract texts section by section and extract meta data for each patent
* Split texts sentence by sentence
* Prepare training/validation/test dataset with meta data
* Create AI models for computing distance between any two paragraphs
* Test/Tune AI models and choose the best model for patent comparison
* Creat AI model for computing distance between any two patents
* Test/Tune AI model

## How to use
1. download python files.
2. create sub directories /list, /searched_patents, /searched_patents/html
3. execute search_korean_patents.py with search command and search keywords separated by space
   * patent url list resulted by keyword search will be created as /list/searched_patents.url
4. execute search_korean_patent.py with download command
   * patent html files will be downloaded in /searched_patents/html/
5. execute extract_text.py to extract part of from html
   * with 2 arguments, the directory name where htmls are saved and the part of patent
     * abstract, description, claims, sentences are examples of the part
   * specified part of each patent will be saved in /searched_patents/part/
   * sentences are all texts that is in the form of sentence. (title, drawings, sequence, terms are not sentences)
6. execute concat_text.py to create a big concatanated file
   * with the same 2 arguments
   * concatanation result will be saved as /searched_patents/part.txt
7. execute sbd_text.py for pre-processing
   * with the same 2 arguments
   * SBD(sentence boundary detection) result will be saved as /searched_patents/part_sbd.text
     * SBD can be done by punctuation identification since patents have formality.
   * stop word filtering result will be saved as /searched_patents/part_sbd_words.text
     * stop words may not be static words and they are dependent on the language.
     * Morphological analyzer can be applied to identify postpositional subword for Korean patents.
   * each patent in /searched_patents/part/ will be processed both sentence boundary detection and stop word filtering
8. apply fasttext for word2vec model
   * if run by command-line, fasttext skipgram -input ../searched_patents/sentences_sbd_words.txt  -output sentences
9. execute embed_sentence.py to create sentence vectors for each patent
   * with the same 2 arguments
   * if run by command-line, fasttext print-sentence-vectors sentences.bin < patent_sbd_words.txt > patent_sbd_words.vec
10. execute find_nearest.py with 3 arguments
    * 1st argument is the patent number to find nearest patents
    * 2nd argument is the subdirecory name (searched_patents)
    * 3rd argument is the part name (abstract, description, claims, sentences)
    * then it will calculate distance between the given patent and all other patents in the subdirectory by
      * cosine similarity between averages of sentence vectors of two patents
      * euclidian distence between averages of sentence vectors of two patents

## Caveats
* Components of Korean patents are not unique.
* Korean patents in Google patents are not very consistently prepared.
  * some patents do not have classifications
  * some patents have not sectionized text for the disclosure and enbodiments.
