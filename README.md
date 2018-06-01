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
* Distance between any 2 korean patents should be calculated.
  * Similar patents should be close to each other
  * A patent and its prior art should be close to each other
  * Patents with different classifications should not be close to each other

## Process breakdown
* Scraping patents
* Extracting texts section by section and meta data for each patent
* Spliting texts sentence by sentence
* Preparing training/verification/test dataset with meta data
* Creating AI model for computing distance between any two patents

## Caveats
* Components of Korean patents are not unique.
* Korean patents in Google patents are not very consistently prepared.
  * some patents do not have classifications
  * some patents have not sectionized text for the disclosure and enbodiments.
