import os
import gnupg
from dotenv import load_dotenv

gpg = gnupg.GPG(gnupghome=os.getenv("PATH_GPG_KEYS"))

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
