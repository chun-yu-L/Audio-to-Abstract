# %%
#!pip install openai
#!pip install --upgrade langchain

import getpass
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import TextLoader
from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate


# %%
OPENAI_API_KEY = getpass.getpass(prompt='open api key: ')
chat = ChatOpenAI(temperature=0.0, model='gpt-3.5-turbo-1106', openai_api_key=OPENAI_API_KEY)


# %%
### Load and preprocess transcribed text
## Read trainscribe text
filename = input('輸入文字檔檔名:')
loader = TextLoader(f'{filename}.txt')
transcription = loader.load()


#%%
## Split transcribe text into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 20
)

split_texts_list = text_splitter.split_text(transcription[0].page_content)
docs = text_splitter.create_documents(split_texts_list)

# %%
### Prompt engineering
prompt_template = """Write a comprehensive summary of the following text with bullet points:\n
{text}\n
SUMMARY IN TRADITIONAL CHINESE:"""
prompt = PromptTemplate.from_template(prompt_template)

refine_template = (
    "Your job is to produce a final summary\n"
    "We have provided an existing summary up to a certain point: {existing_answer}\n"
    "We have the opportunity to refine the existing summary"
    "with some more context below.\n"
    "------------\n"
    "{text}\n"
    "------------\n"
    "Given the new context, refine the original summary\n"
    "Generate a clear and concise topic sentence that captures the main theme of the content."
    "This will be used as the title for the summary."
    "The output should include a title."
    "Additionally, generate an abstract section with a one-paragraph summary."
    "The main point section should comprehensively and clearly describe all key points in the format of bullet points."
    "\n\nSUMMARY IN TRADITIONAL CHINESE:"
)
refine_prompt = PromptTemplate.from_template(refine_template)
chain = load_summarize_chain(
    llm=chat,
    chain_type="refine",
    question_prompt=prompt,
    refine_prompt=refine_prompt,
    return_intermediate_steps=True,
    input_key="input_documents",
    output_key="output_text",
)
result = chain({"input_documents": docs}, return_only_outputs=True)

# %%
print(result['output_text'])

with open(f'{filename}_summary.txt', 'w') as file:
    file.write(result['output_text'])


