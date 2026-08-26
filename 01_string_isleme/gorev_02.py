def domain_cikar(email : str) -> str :

    if "@" in email:
        return email.split("@")[1]

    return ""