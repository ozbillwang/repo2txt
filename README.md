# repo2txt
convert the whole repo into one txt file, mainly used by AI content attachment

### Usage

* Prepare your Github personal access token

(recommend to set fine-grain PAT with expired day)
<img width="1171" alt="image" src="https://github.com/user-attachments/assets/80682a6a-428c-4452-8b52-59eeffc1990c">

* set the environment variable

```
export GITHUB_TOKEN=<GITHUB_TOKEN_PAT>
```

* get the repo url, no need .git, for example, in this repo, the url is

```
https://github.com/ozbillwang/repo2txt
```

* fetch repo contents and merge them into one file
```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt

python repo2text.py https://github.com/cyberfascinate/ISC2-CC-Study-Material
```
* review the output file `output.txt`

* create a new assistant and upload the file to OpenAI Playground, Assistant

OpenAI Playground: https://platform.openai.com/playground/assistants

**You need to be a paying user (or have made at least one payment) to access the OpenAI Assistant.**

<img width="1440" alt="image" src="https://github.com/user-attachments/assets/17487d2a-3994-4a4d-a110-1c360e28dfd3">

* give some instructions (as system promption), now you can ask questions, the AI assistant will answer your question from the content you feed. 
