from utils.config.JSONConfig import JSONConfig
from features.FeatureManager import FeatureManager
from features import FeatureRegistry
import time

_CONFIG_FILE_PATH = "resources/config.json"
_TOKEN_FILE_PATH = "resources/token.json"
config = JSONConfig(_CONFIG_FILE_PATH)
token_conf = JSONConfig(_TOKEN_FILE_PATH)

if token_conf.hasCategory("token"):
    token = token_conf.getCategory("token")
else:
    token = str(input("Token not found! Enter bot token please: "))

feature_manager = FeatureManager()
