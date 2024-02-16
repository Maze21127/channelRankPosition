from loguru import logger

logger.add("logs/error/error.log", format="{time} {level} {message}", level="ERROR", rotation='00:00')
logger.add("logs/info/info.log", format="{time} {level} {message}", level="INFO", rotation='00:00')
logger.add("logs/debug/debug.log", format="{time} {level} {message}", level="DEBUG", rotation='00:00')
