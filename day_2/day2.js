/*  A = Rock        X = Rock
    B = Paper       Y = Paper
    C = Scissors    Z = Scissors */
    
/*  A = Rock        X = Lose this game
    B = Paper       Y = Draw this game
    C = Scissors    Z = Win this game */

const {readFileSync, promises: fsPromises} = require('fs');

/* FILE NAME HERE */
const fileName = './i3.txt'

var totalScore = 0          // part 1 score
var totalScore2 = 0         // part 2 score

const winPoints = 6         // you get 6 points for winning
const drawPoints = 3        // you get 3 points for drawing
const lossPoints = 0        // you get 0 points for losing

const rockPoints = 1        // you get 1 point for playing rock
const paperPoints = 2       // you get 2 points for playing paper
const scissorPoints = 3     // you get 3 points for playing scissor


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
            totalScore += rockPoints 
            if (hisMove === 'A') // rock vs rock
                totalScore =  totalScore + drawPoints
            else if (hisMove === 'B') // rock vs paper
                totalScore =  totalScore + lossPoints
            else if (hisMove === 'C') // rock vs scissor
                totalScore =  totalScore + winPoints
            break
        case 'Y': // you played paper
            totalScore += paperPoints 
            if (hisMove === 'A') // paper vs rock
                totalScore =  totalScore + winPoints
            else if (hisMove === 'B') // paper vs paper
                totalScore =  totalScore + drawPoints
            else if (hisMove === 'C') // paper vs scissor
                totalScore =  totalScore + lossPoints
            break
        case 'Z': // you played scissors
            totalScore += scissorPoints
            if (hisMove === 'A') // scissor vs rock
                totalScore =  totalScore + lossPoints
            else if (hisMove === 'B') // scissor vs paper
                totalScore =  totalScore + winPoints
            else if (hisMove === 'C') // scissor vs scissor
                totalScore =  totalScore + drawPoints
            break
        }
        
}

function getWinnerAndScore2(arrayItem) {
    const hisMove = arrayItem[0]
    const yourMove = arrayItem[2]
    switch(yourMove){
        case 'X': // you need to LOSE
            totalScore2 += lossPoints
            if (hisMove === 'A') // LOSE vs rock (play scissor)
                totalScore2 =  totalScore2 + scissorPoints
            else if (hisMove === 'B') // LOSE vs paper (play rock)
                totalScore2 =  totalScore2 + rockPoints
            else if (hisMove === 'C') // LOSE vs scissor (play paper)
                totalScore2 =  totalScore2 + paperPoints
            break
        case 'Y': // you need to DRAW
            totalScore2 += drawPoints
            if (hisMove === 'A') // DRAW vs rock (play rock)
                totalScore2 =  totalScore2 + rockPoints
            else if (hisMove === 'B') // DRAW vs paper (play paper)
                totalScore2 =  totalScore2 + paperPoints
            else if (hisMove === 'C') // DRAW vs scissor (play scissor)
                totalScore2 =  totalScore2 + scissorPoints
            break
        case 'Z': // you need to WIN
            totalScore2 += winPoints
            if (hisMove === 'A') // WIN vs rock (play paper)
                totalScore2 =  totalScore2 + paperPoints
            else if (hisMove === 'B') // WIN vs paper (play scissor)
                totalScore2 =  totalScore2 + scissorPoints
            else if (hisMove === 'C') // WIN vs scissor (play rock)
                totalScore2 =  totalScore2 + rockPoints
            break
        }
        
}

const fileContents = syncReadFile(fileName);
console.log("PART 1")
fileContents.forEach(el => getWinnerAndScore(el))
console.log(totalScore)
console.log("PART 2")
fileContents.forEach(el => getWinnerAndScore2(el))
console.log(totalScore2)