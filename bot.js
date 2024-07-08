const { Client, GatewayIntentBits, ActivityType, Partials, EmbedBuilder, ActionRowBuilder, ButtonBuilder, ButtonStyle } = require('discord.js');
const config = require('./config');
const TOKEN = config.TOKEN;

const client = new Client({
    intents: [
        GatewayIntentBits.Guilds,
        GatewayIntentBits.GuildMessages,
        GatewayIntentBits.MessageContent,
        GatewayIntentBits.GuildMembers
    ],
    partials: [Partials.Channel]
});

client.once('ready', () => {
    console.log(`Logged in as ${client.user.tag}`);
    client.user.setActivity('/help_pp | PP', {
        type: ActivityType.Streaming,
        url: 'https://www.twitch.tv/powderedlamb40'
    });
});

client.on('interactionCreate', async interaction => {
    if (!interaction.isCommand()) return;

    const { commandName } = interaction;

    if (commandName === 'help_pp') {
        const button = new ButtonBuilder()
            .setStyle(ButtonStyle.Link)
            .setLabel('ขอความช่วยเหลือ')
            .setURL('https://discord.gg/yNKGyDumje');

        const row = new ActionRowBuilder().addComponents(button);

        await interaction.reply({ content: 'สวัสดี! คุณต้องการความช่วยเหลือในสิ่งใด?', components: [row], ephemeral: true });
    } else if (commandName === 'ping') {
        const latency = client.ws.ping;
        await interaction.reply(`บอทมีค่า ping เท่ากับ ${latency} มิลลิวินาที`);
    }
});

client.login(TOKEN);
