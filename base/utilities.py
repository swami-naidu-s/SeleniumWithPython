from common_imports import *

def get_config_data(key: str) -> str | dict | int:
    with open("config.json", "r") as f:
        data = json.load(f)
    return data[key]

def get_logger(name: str, timestamp: str) -> Logger:
    os.makedirs(os.path.join("TestResults", f"{timestamp}_{name}"), exist_ok=True)
    log_file = os.path.join("TestResults", f"{timestamp}_{name}", f"{name}_{timestamp}.log")

    logger = logging.getLogger(name)
    if logger.handlers:
        return logger
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

def generate_random_string(length: int = 6) -> str:
    return ''.join(random.choices(string.ascii_letters, k=length))

def generate_random_lower_string(length: int = 6) -> str:
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def generate_random_upper_string(length: int = 6) -> str:
    return ''.join(random.choices(string.ascii_uppercase, k=length))

def generate_random_number(length: int = 4) -> str:
    return ''.join(random.choices(string.digits, k=length))

def generate_timestamp() -> str:
    return datetime.now().strftime("%Y%m%d %H%M%S")

def generate_timestamp_without_space() -> str:
    return datetime.now().strftime("%Y%m%d%H%M%S")