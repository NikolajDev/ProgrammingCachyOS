def existuje(meno_suboru):
    try:
        with open(meno_suboru):
            return True
    except (TypeError, OSError, FileNotFoundError):
        return False