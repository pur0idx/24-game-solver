def permute(elements, n=None):
    result = []
    if n is None :
        generatePermutations(elements, [], result)
    else :
        generatePermutationsWithLength(elements, [], result, n)
    return result

def permute_with_repetition(elements, n=None):
    result = []
    if n is None :
        generatePermutationsWithRepetition(elements, [], result)
    else :
        generatePermutationsWithRepetitionWithLength(elements, [], result, n)
    return result

def generatePermutations(elements, currentPermutation, result):
    if len(elements) == 0:
        result.append(currentPermutation)
        return
    
    for i in range(len(elements)):
        newElements = elements[:i] + elements[i+1:]
        generatePermutations(newElements, currentPermutation + [elements[i]], result)
        
def generatePermutationsWithLength(elements, currentPermutation, result, n):
    if len(currentPermutation) == n :
        result.append(currentPermutation)
        return
    
    for i in range(len(elements)):
        newElements = elements[:i] + elements[i+1:]
        generatePermutationsWithLength(newElements, currentPermutation + [elements[i]], result, n)

def generatePermutationsWithRepetition(elements, currentPermutation, result) :
    if len(currentPermutation) == len(elements) :
        result.append(currentPermutation)
        return
    
    for element in elements :
        generatePermutationsWithRepetition(elements, currentPermutation + [element], result)
    
def generatePermutationsWithRepetitionWithLength(elements, currentPermutation, result, n) :
    if len(currentPermutation) == n :
        result.append(currentPermutation)
        return
    
    for element in elements :
        generatePermutationsWithRepetitionWithLength(elements, currentPermutation + [element], result, n)