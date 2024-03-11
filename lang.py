import requests

def get_language_stats(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    repos = response.json()

    languages = {}
    for repo in repos:
        repo_languages_url = repo['languages_url']
        languages_response = requests.get(repo_languages_url)
        repo_languages = languages_response.json()
        for lang, size in repo_languages.items():
            if lang in languages:
                languages[lang] += size
            else:
                languages[lang] = size

    return languages

username = "janeeshgithub"  # Change this to your GitHub username
language_stats = get_language_stats(username)
print(language_stats)
