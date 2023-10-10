/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */




for(i = 1; i < 101; i++){
    if(i % 3 == 0 && i % 5 == 0){
            numero = 'fizzBuzz'
            console.log(numero)
    } else if(i % 3 == 0 ) {  
        numero = 'fizz'
        console.log(numero)
    } else if(i % 5 == 0) {
        numero = 'buzz'
        console.log(numero)
    } else {
        console.log(i)
    }
 }


// for(i = 1; i < 101; i++){
//     switch(true){
//         case i % 3 == 0 && i % 5 == 0:
//             numero = 'fizzBuzz'
//             console.log(numero)
//             break;
//         case i % 3 == 0 :
//             numero = 'fizz'
//             console.log(numero)
//             break;
//         case i % 5 == 0:
//             numero = 'buzz'
//             console.log(numero)
//             break;
//         default:
//             console.log(i)
//  }
// }
    
        

