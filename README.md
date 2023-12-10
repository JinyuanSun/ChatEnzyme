# ChatEnzyme
Ask anything about enzymes

## Installation
1. Download the repository and install the requirements
```
git clone git@github.com:JinyuanSun/ChatEnzyme.git
cd ChatEnzyme
pip3 install torch --index-url https://download.pytorch.org/whl/cu118 # skip if you torch already installed
pip3 install sentence-transformers chromadb langchain openai streamlit
```

2. Download the BRENDA database from (here)[https://www.brenda-enzymes.org/download.php] and build chromadb

```bash
python build_chroma_db.py # this will take a while
```

## Usage
Before you start, make sure you have set the OPENAI_API_KEY environment variable. You can get your API key from (here)[https://beta.openai.com/].
```bash
streamlit run streamlit_ui.py
```