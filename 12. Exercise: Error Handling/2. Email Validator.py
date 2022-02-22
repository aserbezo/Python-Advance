import re


class NametooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


def check_domain(domain_check):
    pattern = r".com|.org.|.bg|.net"
    match = re.search(pattern, domain_check)
    if match:
        return True

    return False


while True:
    email = input()
    if email == "End":
        break

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    user, domain = email.split("@")

    if len(user) <= 4:
        raise NametooShortError("Name must be more than 4 characters")

    # we are calling the function to check if the domain is correct and if is False will raise error
    if not check_domain(domain):
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org,.net")

    print("Email is valid")
