// Function to apply softmax
export function applySoftmax(tensor: number[]) {
    const expValues = tensor.map(val => Math.exp(val));
    const sumExp = expValues.reduce((acc, val) => acc + val, 0);
    return expValues.map(val => val / sumExp);
}

// Function to perform multinomial sampling
export function multinomial(probabilities: number[], numSamples: number = 1): number[] {
    const sampledIndices: number[] = [];
    
    for (let s = 0; s < numSamples; s++) {
        let cumulativeProbability = 0;
        const randomValue = Math.random();

        for (let i = 0; i < probabilities.length; i++) {
            cumulativeProbability += probabilities[i];
            
            if (randomValue <= cumulativeProbability) {
                sampledIndices.push(i);
                break;
            }
        }
    }

    return sampledIndices;
}
