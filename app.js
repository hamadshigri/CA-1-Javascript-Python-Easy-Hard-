//         //  Create a function that takes three parameters of equation and returns the roots of this equation: 
//  For example: 
//  2×2+4x−6
//  Find the roots of this equation: 
//  Formula and Solution: 

//  x =  −b ± √(b^2 − 4ac)
//           2a
//  x =  −4 ± √(4^2 − 4(2)(-6))
//           2(2)

//  x =  −4 ± √(16 − -48))
//            4

//  x =  −4 ± √64
//          4

//  x =  −4 ± 8
//          4

//  x =   4         x = - 12
//        4               4 

// which becomes

// x = 1
// x = -3

// Hence the roots of this equation are 1 and -3
// Paste your JavaScript code with some example results here in this assignment.


function solve(a, b, c) {
    var result = (-1 * b + Math.sqrt(Math.pow(b, 2) - (4 * a * c))) / (2 * a);
    var result2 = (-1 * b - Math.sqrt(Math.pow(b, 2) - (4 * a * c))) / (2 * a);
    return result + ", " + result2;
}
document.write(solve(1, 1, -1));

