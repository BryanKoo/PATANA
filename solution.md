# Solution - how to find novelty infringement accurately and efficiently

## Characteristics of patents
Claims are explained in description part in detail.

## Hypothesis
* We can find candidates for novelty inpringement by comparing abstract part of patent.
  * Finding candadates can be seen as text classification.
  * Efficiency is improved because abstract part is only small portion of patent.
  * All patent can be embedded into a vector space (invention space) and candidates can be found by spatial query.
* We use similarity of claims to determine the degree of novelty infringement.
  * The similarity is not obtained by simple spatial query but head-to-head calculation like WMD.
  * The calulation should not be executed sentence by sentence but the total text of each claim at once.
  * Because independent claim is referred in dependent claims, there are 2 ways of comparing claims of two patent
    * Concatenate all dependent claims to the depending claim before the calculation. The number of claims of a patent will be reduced to the number of independent claims.
    * Concatenate independent claim to its dependent claims before the calculation. The number of claims of a patent will not be changed.
  * The degree of novelty infringement is not the accumulated distance but the mininum distance between claims of two patents.
* The distance calucation of ech claim can be more accurate when explanation in description part is concaternated.
  * It is the same reason why we caoncatenate depending claim to dependent claim before the distance calculation.

## Experiment for verificaion

## The final architecture
