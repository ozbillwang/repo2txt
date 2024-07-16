import requests
from urllib.parse import urljoin
import sys

def fetch_repo_contents(repo_url):
    # Parse the repository URL to construct the API endpoint
    parts = repo_url.rstrip('/').split('/')
    owner = parts[-2]
    repo = parts[-1]
    api_url = f"https://api.github.com/repos/{owner}/{repo}/contents"
    
    # Initialize an empty list to store all text content
    all_texts = []
    
    # Function to recursively fetch contents from the GitHub API
    def fetch_contents(url):
        response = requests.get(url)
        if response.status_code == 200:
            contents = response.json()
            for item in contents:
                if item['type'] == 'file':
                    # Fetch file content if it's not a binary file (ignore images and other binaries)
                    if 'download_url' in item and not is_binary_file(item['download_url']):
                        file_url = item['download_url']
                        file_response = requests.get(file_url)
                        if file_response.status_code == 200:
                            try:
                                # Try to decode the content as UTF-8
                                content = file_response.content.decode('utf-8')
                                all_texts.append(f"file: {item['path']}\n")
                                all_texts.append(f"content:\n{content}\n\n")
                            except UnicodeDecodeError:
                                print(f"Failed to decode {item['path']} as UTF-8")
                elif item['type'] == 'dir':
                    # Recursively fetch contents of subdirectories
                    fetch_contents(item['url'])
        else:
            print(f"Failed to fetch contents from {url}. Status code: {response.status_code}")
    
    # Start fetching contents from the root of the repository
    fetch_contents(api_url)
    
    return all_texts

def is_binary_file(url):
    # Function to check if a file is binary (e.g., image, PDF)
    response = requests.head(url)
    content_type = response.headers.get('Content-Type', '')
    if content_type.startswith('text') or 'charset' in content_type.lower():
        return False
    return True

def main(repo_url):
    # Fetch all texts from the repository
    texts = fetch_repo_contents(repo_url)

    if texts:
        # Write all texts to a file
        with open('output.txt', 'w', encoding='utf-8') as f:
            f.writelines(texts)
        print("Texts extracted and saved to output.txt")
    else:
        print("Failed to fetch texts from the repository.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python repo2text.py <repo_url>")
    else:
        repo_url = sys.argv[1]
        main(repo_url)

