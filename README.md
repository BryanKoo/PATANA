# PATANA
PATent ANAlysis project 

Prior arts for a patent are searched many times during the life cycle of a patent.
It is because novelty is one of the most important factor for determining patentability.
Though it may be difficult yet for AI to determine whether a patent have novelty or not.
AI can help human by suggesting search term and screening irrelevant patents from search results.

This project is about development of AI NLP algorithm based on up-to-date ML technology for the patent analysis.
Patents are written with natural written language, not spoken language in technology domain.
This project starts with developing technology for screening irrelevant patents for Korean patents first.
Working with other languages and suggesting search term will be followed.

## Life cycle of patents
* Preparation of an application
* Pre-grant prosecution
  * Filing an application
  * Search and examination
* Post-grant prosecution

## Components of Korean patents
* drawings - not relevent to the project
* textual information
  * title
  * abstract
  * description
    * technical-field
    * background-art
    * tech-problem
    * tech-solution
    * advantageous-effects
    * industial-applicability
    * description-of-drawings
    * description-of-embodiments
    * disclosure
    * sommury-of-invention
    * sequence-list-text
    * mode-for-invention
    * reference-signs-list
  * claims  
* meta information

## Korean patent numbers
* patent numbers start with 10 and have 9 digits end with B1
* patent numbers start with year and have 11 digits and end with A

## Software requiremants of the projects

## Process breakdown
* Scraping patents
* Extracting text section by section and meta data for each patent
* 

## Caveats
* Components of patents are not unique.
* Korean patents in Google patents are not very consistent.
  * some patents do not have classifications
  * some patents have not sectionized text for the disclosure and enbodiments.

## External resources
