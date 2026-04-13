def response(hey_bob):
    s = hey_bob.strip()

    if not s:
        return "Fine. Be that way!"

    is_question = s.endswith("?")
    has_letters = any(c.isalpha() for c in s)
    is_yelling = has_letters and s.upper() == s

    if is_question and is_yelling:
        return "Calm down, I know what I'm doing!"
    if is_yelling:
        return "Whoa, chill out!"
    if is_question:
        return "Sure."

    return "Whatever."