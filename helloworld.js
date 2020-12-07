const login = require('./config.json');

const Discord = require('discord.js');
const client = new Discord.Client();

client.on('message', message => {
    if(message.author.bot) return;
    message.channel.send("Hello World!");
})

client.once('ready', () => {
    console.log('Ready!');
});

client.login(login.token);