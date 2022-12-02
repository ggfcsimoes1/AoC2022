/*  A = Rock        X = Rock
    B = Paper       Y = Paper
    C = Scissors    Z = Scissors */

const {readFileSync, promises: fsPromises} = require('fs');
var totalScore = 0
const winPoints = 6
const drawPoints = 3
const lossPoints = 0

function syncReadFile(filename) {
  const contents = readFileSync(filename, 'utf-8');

  const arr = contents.split(/\r?\n/);

  return arr;
}

function getWinnerAndScore(arrayItem) {
    const hisMove = arrayItem[0]
    const yourMove = arrayItem[2]
    switch(yourMove){
        case 'X': // you played rock
            totalScore += 1 // you get 1 point for playing rock
            if (hisMove === 'A') // rock vs rock
                totalScore =  totalScore + drawPoints
            else if (hisMove === 'B') // rock vs paper
                totalScore =  totalScore + lossPoints
            else if (hisMove === 'C') // rock vs scissor
                totalScore =  totalScore + winPoints
            break
        case 'Y': // you played paper
            totalScore += 2 // you get 2 points for playing paper
            if (hisMove === 'A') // paper vs rock
                totalScore =  totalScore + winPoints
            else if (hisMove === 'B') // paper vs paper
                totalScore =  totalScore + drawPoints
            else if (hisMove === 'C') // paper vs scissor
                totalScore =  totalScore + lossPoints
            break
        case 'Z': // you played scissors
            totalScore += 3 // you get 2 points for playing scissor
            if (hisMove === 'A') // scissor vs rock
                totalScore =  totalScore + lossPoints
            else if (hisMove === 'B') // scissor vs paper
                totalScore =  totalScore + winPoints
            else if (hisMove === 'C') // scissor vs scissor
                totalScore =  totalScore + drawPoints
            break
        }
        
}

const fileContents = syncReadFile('./i3.txt');
fileContents.forEach(el => getWinnerAndScore(el))
console.log(totalScore)