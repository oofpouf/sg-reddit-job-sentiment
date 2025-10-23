# filter for job related keywords 
from .keywords import hiring_keywords, layoff_keywords, trend_keywords, jobseeker_keywords

job_market_keywords = (
    hiring_keywords + layoff_keywords + trend_keywords + jobseeker_keywords
)

def is_singapore_related(text):
    return any(kw.lower() in text.lower() for kw in job_market_keywords)