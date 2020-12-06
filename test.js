const login = require('./config.json');

const Discord = require('discord.js');
const client = new Discord.Client();

// Logs messages it sees on console
// Successful!
/*
client.on('message', message => {
    console.log(message.content);
})
*/

client.once('ready', () => {
    console.log('Ready!');
});

client.login(login.token);