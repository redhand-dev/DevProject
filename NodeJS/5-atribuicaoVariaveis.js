console.log("Trabalhando com Atribuição de Variáveis");

const primeiroNome = "Islaine";
const sobrenome = "Santos";

//console.log(nome+sobrenome);
//console.log(nome+""+sobrenome);
console.log(primeiroNome, sobrenome);
console.log('Meu nome é ${primeiroNome} ${sobrenome}'); //uso de ${} não funciona na versão 17.3.0

const nomeCompleto = primeiroNome + sobrenome;
console.log(nomeCompleto);

let idade; //declarando variável
idade=26;
idade=idade+1;
console.log(idade);