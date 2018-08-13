# Solution - how to find novelty infringement accurately and efficiently

## Characteristics of patents
Patent is a well-formed document where invention is explained in several sections such as abstract, description, drawings, claims.
Usually an invention is combination of several unique ideas that are independent or dependent with each other.
Each unique idea of invention is expressed as a claim or a set of claims in the patent.
Technical field, background art, explanation of claims, industrial applicability, .. are sub-sections of description.
Abstract is a concise summary of the disclosure of the invention contained in the description, claims and drawings.

## Hypothesis
* We can find possible candidates for novelty inpringement by comparing abstract part of patent.
  * Abstract part is usually the smallest section and it can be easily embedded into a vector space.
  * The the possible candidates are nearest patents from the one of interest in the invention space.
  * Operation for finding nearest vector is a conceptually simple but the time complexity is higher than the one for the keyword search.
* We can determine the degree of novelty infringement with similarity between claims of patent.
  * The accurate similarity is not obtained by simple spatial query but head-to-head comparison.
  * The calulation should not be executed sentence by sentence but the total text of each claim at once.
  * Because independent claim is referred in dependent claims, there are 2 ways of comparing claims of two patent
    * Concatenate all dependent claims to the depending claim before the calculation. The number of claims of a patent will be reduced to the number of independent claims.
    * Concatenate independent claim to its dependent claims before the calculation. The number of claims of a patent will not be changed.
  * The degree of novelty infringement is not the accumulated distance but the mininum distance between claims of two patents.
* The distance calucation of each claim can become more accurate when explanation in description part is concaternated .
  * It is the same reason why we concatenate depending claim to dependent claim before the distance calculation.

## Experiment for verificaion

## The final architecture
