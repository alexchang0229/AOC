// FUCKKKKKKKKKKKKKKKKK

const fs = require('node:fs');

const data = fs.readFileSync('./Day-3/input.txt', 'utf8');

const dataLines = data.split("\n")

const checkSymbol = (char) => {
    switch (char) {
        case "@": return true
        case "*": return true
        case "#": return true
        case "$": return true
        case "-": return true
        case "=": return true
        case "+": return true
        case "&": return true
        case "%": return true
        case "/": return true
        default: return false
    }
}

const checkTopBottom = (line) => {
    if (line) {
        let lineArray = Array.from(line)
        return lineArray.some(element => checkSymbol(element))
    } else {
        // first line or bottom line
        return false
    }
}

const checkSides = (match, lineInd) => {

    let start_ind = match.index - 1 < 0 ? 0 : match.index - 1
    let end_ind = match.index + match[0].length > match.input.length ? match.input.length : match.index + match[0].length
    let leftSide = match.input[start_ind]
    let rightSide = match.input[end_ind]
    let prevLine = dataLines[lineInd - 1]?.slice(start_ind, end_ind + 1)
    let nextLine = dataLines[lineInd + 1]?.slice(start_ind, end_ind + 1)

    let allSides = [
        checkTopBottom(prevLine),
        checkTopBottom(nextLine),
        checkSymbol(leftSide),
        checkSymbol(rightSide),
    ]
    if (allSides.some(element => element)) {
        return true
    } else {
        return false
    }
}

const findPartNumberInLine = (line, lineInd) => {
    const numbersRe = line.matchAll(/\d+/g)
    const numbersArray = Array.from(numbersRe)
    const validNumbers = numbersArray.filter((match) => checkSides(match, lineInd))
    return validNumbers
}

let allValidNumbers = dataLines.map(findPartNumberInLine).flat()
let sumValidNums = allValidNumbers.reduce((a, b) => a + parseInt(b[0]), 0)
console.log(sumValidNums)

// PART 2

const resolveGearNums = (row, ind) => {
    let head = ind
    let numberArray = []
    // Seach foward
    while (row[head]?.match(/\d/) || head === ind) {
        numberArray.push(row[head])
        head++
    }
    head = ind - 1
    while (row[head]?.match(/\d/)) {
        numberArray.unshift(row[head])
        head--
    }
    let numsString = numberArray.join("")
    let multipleNums = numsString.split(".")
    let removeblank = multipleNums.filter(element => element !== "")
    if (removeblank.length === 1) {
        return removeblank[0]
    }
    if (removeblank.length === 2) {
        return removeblank
    }
}

const checkSidesGears = (match, lineInd) => {

    let start_ind = match.index - 1 < 0 ? 0 : match.index - 1
    let end_ind = match.index + match[0].length > match.input.length ? match.input.length : match.index + match[0].length
    let leftSide = match.input[start_ind]
    let rightSide = match.input[end_ind]
    let prevLine = dataLines[lineInd - 1]?.slice(start_ind, end_ind + 1)
    let nextLine = dataLines[lineInd + 1]?.slice(start_ind, end_ind + 1)

    let gear_numbers = []
    if (leftSide.match(/\d/)) {
        gear_numbers.push(resolveGearNums(match.input, start_ind))
    }
    if (rightSide.match(/\d/)) {
        gear_numbers.push(resolveGearNums(match.input, end_ind))
    }
    if (prevLine.match(/\d/)) {
        if (Array.isArray(resolveGearNums(dataLines[lineInd - 1], match.index))) {
            resolveGearNums(dataLines[lineInd - 1], match.index).map(row => gear_numbers.push(row))
        } else {
            gear_numbers.push(resolveGearNums(dataLines[lineInd - 1], match.index))
        }
    }
    if (nextLine.match(/\d/)) {
        if (Array.isArray(resolveGearNums(dataLines[lineInd + 1], match.index))) {
            resolveGearNums(dataLines[lineInd + 1], match.index).map(row => gear_numbers.push(row))
        } else {
            gear_numbers.push(resolveGearNums(dataLines[lineInd + 1], match.index))
        }
    }
    if (gear_numbers.length == 2)
        return parseInt(gear_numbers[0]) * parseInt(gear_numbers[1])
}

const findGears = (line, lineInd) => {
    const starsRe = line.matchAll(/\*/g)
    const starsArray = Array.from(starsRe)
    const starNumbers = starsArray.map((match) => checkSidesGears(match, lineInd))
    const gearPairs = starNumbers.filter(element => element)
    return gearPairs
}

let allValidgears = dataLines.map(findGears).flat()
// let sumGears = allValidgears.reduce((a, b) => a + b, 0)
console.log(allValidgears)
