console.log('Trabalhando com Listas');
// const salvador ='Salvador';
// const saoPaulo = 'São Paulo';
// const rioDeJaneiro = 'Rio de Janeiro';

const listaDeDestinos = new Array(
    'Salvador',
    'São Paulo',
    'Rio de Janeiro'
)

listaDeDestinos.push('Curitiba') //adicionar item na lista ja declarada
console.log("Destinos possíveis:");
//console.log(salvador, saoPaulo, rioDeJaneiro)
console.log(listaDeDestinos);

listaDeDestinos.splice(1,1); //removendo item
console.log(listaDeDestinos);


console.log(listaDeDestinos[1], listaDeDestinos[0]);