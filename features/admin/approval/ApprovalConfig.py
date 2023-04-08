from utils.config.Config import Config
import enum


class ApprovalConfig(Config):
    name = "approval"

    class RestrictedChannelType(enum.Enum):
        new_channel = "new_channel"
        dm_channel = "dm_channel"

    def __init__(self, verifyButtonChannel: str = "general",
                 channelType: RestrictedChannelType = RestrictedChannelType.dm_channel,
                 cooldown: int = 20):
        super().__init__(ApprovalConfig.name)
        self.verifyButtonChannel = verifyButtonChannel
        self.channelType = channelType
        self.cooldown = cooldown
