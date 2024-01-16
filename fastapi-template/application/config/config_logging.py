import os
import yaml
import logging
import logging.config


class SensitiveInfoFilter(logging.Filter):
    """
    A filter to mask sensitive information in log messages.
    """

    def __init__(self, sensitive_words: list[str]):
        """
        Function to initialize the filter.

        :param sensitive_words: Sensitive words to mask.
        :type sensitive_words: list[str]
        """
        super().__init__()
        self.sensitive_words = sensitive_words

    def filter(self, record) -> bool:
        """
        Check if a log record contains sensitive information, and if so, mask it.

        :param record: Record to filter.
        :return: Flag to indicate if the record was filtered.
        :rtype: bool
        """
        try:
            msg = record.getMessage()
            for word in self.sensitive_words:
                msg = msg.replace(word, "*" * len(word))
            record.msg = msg
            return True
        except Exception as error:
            logging.error(f"Error filtering log message: {error}")
            return False


def replace_env_for_config(log_conf: dict) -> None:
    """
    Function to replace the environment variables in the logging configuration.

    :param log_conf: Dictionary with the logging configuration.
    :type log_conf: dict
    """
    for k, v in log_conf.items():
        if isinstance(v, dict):
            replace_env_for_config(v)
        elif isinstance(v, str) and v[0] == "$":
            log_conf[k] = os.environ.get(v[1:])


def create_log_config(log_path: str) -> dict:
    """
    Function to create the log configuration.

    :param log_path: Path to the logging configuration.
    :type log_path: str
    :return: Logging configuration.
    :rtype: dict
    """
    with open(log_path, "r") as f:
        log_config = yaml.load(f, Loader=yaml.CLoader)
        replace_env_for_config(log_config)
    return log_config


def setup_logging() -> None:
    """
    Function to setup the logging configuration. Is called first, in the main function of the application.
    """
    log_config = create_log_config("config/files/logging.yaml")
    logging.config.dictConfig(log_config)
