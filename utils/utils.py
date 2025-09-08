import re

def clean_text(text):
    cleaned_text = re.sub('http\S+\s', ' ', text)
    cleaned_text = re.sub('RT|cc', ' ', cleaned_text)
    cleaned_text = re.sub('#\S+\s', '', cleaned_text)
    cleaned_text = re.sub('@\S+', ' ', cleaned_text)
    cleaned_text = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', cleaned_text)
    cleaned_text = re.sub(r'[^\x00-\x7F]', ' ', cleaned_text)
    cleaned_text = re.sub('\s+', ' ', cleaned_text)
    return cleaned_text