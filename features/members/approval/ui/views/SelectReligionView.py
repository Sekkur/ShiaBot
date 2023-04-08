import discord
from discord.ui import View, Button

from features.members.approval.ui.ApprovalUI import ApprovalUI


class SelectReligionView(View):
    def __init__(self, ui: ApprovalUI):
        super().__init__()
        self.ui = ui
        self.sunni_button = Button(label="Sunni", custom_id="sunni_button")
        self.other_button = Button(label="Other", custom_id="other_button")
        self.add_item(self.shia_button)
        self.add_item(self.sunni_button)
        self.add_item(self.other_button)

    @discord.ui.button(label="Shia", custom_id="shia_button")
    async def on_shia_button_click(self, interaction: discord.Interaction):
        await interaction.response.send_message("Button 1 clicked!")

    @discord.ui.button(label="Shia", custom_id="shia_button")
    async def on_shia_button_click(self, interaction: discord.Interaction):
        await interaction.response.send_message("Button 1 clicked!")

    @discord.ui.button(label="Shia", custom_id="shia_button")
    async def on_shia_button_click(self, interaction: discord.Interaction):
        await interaction.response.send_message("Button 1 clicked!")
