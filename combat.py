import discord

class CombatView(discord.ui.View, reinforce_callback):
    
    @discord.ui.button(label="Reinforce", style=discord.ButtonStyle.primary, emoji="🛡️")
    async def reinforce_callback(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)

    @discord.ui.button(label="Prepare", style=discord.ButtonStyle.primary, emoji="👁️")
    async def prepare_callback(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)

    @discord.ui.button(label="Strike", style=discord.ButtonStyle.primary, emoji="⚔️")
    async def strike_callback(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
