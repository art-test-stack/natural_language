# natural_language

Welcome to the natural_language !

This first page is about documentation. I am starting with this project Natural Language Processing (NLP). The objective is to create a program capable of determining whether a text seems "natural" in a target language. We don't want to take into account the grammatical mistakes and the difficulty is precisely there. Indeed, a person can make mistakes when expressing himself in his native language. However, these errors will often be errors that are accepted - at least orally - in the said language. A person learning a language will make different mistakes. It is therefore amusing to try to distinguish one from the other.

At this stage I distinguish in a naive way, 4 ways of expressing oneself.

Speaking :

- The sustained oral language which is found in an official environment [1]
- Colloquial oral language which is found in a family or friendly context (perhaps the most used and not the most correct) [2]

Texting :

- Official written language [3]
- Not official written language (sms) [4]

We could also add romantic, theatrical etc. ways which can be several in some languages but it seems enough for now.

My personal goal is to determine the differences in a language between native and foreigner speaker. But it also could be to help anyone who wants to improve himself in one of those ways of speaking to sound more more "natural" to native speaker hearing. (The most funny one seams to be [2] to me)

First issues will be about reading and testing documentation about NLP. In the other hand, creating a dataset in a language targeted to test our program -it will be Japanese, even if it's not good for overfitting start with more than one language seems hard. Maybe we will go to French then-. Then have a look on this as a beginning seems fair to me.

## env

```bash
virtualenv -p python3.10 virtualenv -p python3.10 /Users/arthurtestard/envs/nlenv
````
```bash
source ${HOME}/envs/nlenv
pip3.10 install -r requirements.txt
```

### Upgrade pip version (necessary if "cannot import name 'html5lib'" error)
wget https://bootstrap.pypa.io/get-pip.py
python3.10 get-pip.py
python3.10 -m pip install --upgrade pip
rm get-pip.py

## Code Source 

http://aima.cs.berkeley.edu/
