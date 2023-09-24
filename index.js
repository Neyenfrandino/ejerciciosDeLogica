/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */




for(i = 1; i < 101; i++){
    let numeros = [i]
    for(multiplo of numeros){
        if(multiplo % 3 == 0 && multiplo % 5 == 0){
            numero = 'fizzBuzz'
            console.log(numero)
    }else{
        if(multiplo % 3 == 0 ) {  
            numero = 'fizz'
            console.log(numero)
        }else{
            if(multiplo % 5 == 0){
                numero = 'buzz'
                console.log(numero)
            }else{
                console.log(multiplo)
    } 
   }
  } 
 }  
}

