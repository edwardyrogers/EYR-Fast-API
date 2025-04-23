import logging
from colorama import init, Fore, Style

# Initialize colorama for cross-platform coloring
init(autoreset=True)

class LoggingService:
    def __init__(self, name: str = "app"):
        self.logger = logging.getLogger(name)
        self.formatter = logging.Formatter(
            f"{Fore.CYAN}[%(levelname)s]{Style.RESET_ALL} %(message)s"
        )

        self._configure_logger()

    def _configure_logger(self):
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            handler.setFormatter(self.formatter)

            self.logger.addHandler(handler)
            self.logger.setLevel(logging.DEBUG)

            access_logger = logging.getLogger("uvicorn.access")
            access_logger.handlers.clear()
            access_logger.propagate = False

            error_logger = logging.getLogger("uvicorn.error")
            error_logger.handlers = [handler]
            error_logger.propagate = False

    def info(self, msg: str):
        self.logger.info(f"{Fore.BLUE}🛎️  {msg}{Style.RESET_ALL}")

    def warning(self, msg: str):
        self.logger.warning(f"{Fore.YELLOW}⚠️  {msg}{Style.RESET_ALL}")

    def error(self, msg: str):
        self.logger.error(f"{Fore.RED}🔥 {msg}{Style.RESET_ALL}")

    def debug(self, msg: str):
        self.logger.debug(f"{Fore.GREEN}🐞 {msg}{Style.RESET_ALL}")
