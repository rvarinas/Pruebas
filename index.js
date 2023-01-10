/*para cargar el modulo nativo dentro de nuestro archivo js podemos 
 usar el pauqte bindings que instalamos al principio
o especificar la ruta completa de donde esta el archivo .node generado*/
//froma 1
const mymodule = require("bindings")("mymodule");//el .node no es necesario
//forma 2
//const mymodule = require("./build/Release/mymodule");//el .node no es necesario
const sum = mymodule.suma(2,2);

console.log("El resultado de la suma es :", sum);//mostramos el resultado 

//No se programar, nueva linea
//Nueva línea que no se programar