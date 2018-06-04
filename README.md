# PATANA
PATent ANAlysis project 

Prior arts for a patent are searched many times during the life cycle of a patent.
It is because novelty is one of the most important factor for determining patentability.
Though it may be difficult yet for AI to determine whether a patent have novelty or not.
AI can help human by suggesting search term and screening irrelevant patents from search results.

This project is about development of AI NLP algorithm based on up-to-date ML technology for the patent analysis.
Patents are written with natural written language, not spoken language, in technology domain.
This project starts with developing technology for screening irrelevant patents for Korean patents first.
Working with other languages and suggesting search term will be followed.

## Life cycle of patents
* Preparation of an application
* Pre-grant prosecution
  * Filing an application
  * Search and examination
* Post-grant prosecution

## Software requiremants of the projects
* Develop AI-based software that calculated distance between any 2 korean patents
  * Similar patents should be close to each other
  * A patent and its prior art should be close to each other
  * Patents with different classifications should not be close to each other

## How to calculate distance between two patents
Technology for comparing random documents is not mature yet.
Patents are relatively well-formed and they have nice matadata that can be used for both verification and learning.
Experiments are needed to know which part should be compared to calculated distance efficiently and precisely.
Baseline for the calculation is the paragraph vector disclosed by Mikolov. https://cs.stanford.edu/~quocle/paragraph_vector.pdf

## Process breakdown
* Scrape patents
* Extract texts section by section and extract meta data for each patent
* Split texts sentence by sentence
* Prepare training/verification/test dataset with meta data
* Creat AI model for computing distance between any two patents

## Caveats
* Components of Korean patents are not unique.
* Korean patents in Google patents are not very consistently prepared.
  * some patents do not have classifications
  * some patents have not sectionized text for the disclosure and enbodiments.
