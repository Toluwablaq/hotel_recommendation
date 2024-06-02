import os
from dotenv import load_dotenv
import openai
import langchain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain, SequentialChain

#this is the .env file
load_dotenv()
#this is the openai api key
os.getenv("OPENAI_API_KEY") 
#this is the llm model
llm = OpenAI(model_name="gpt-3.5-turbo-instruct")

#this function will generate the hotel name and country name
def generate_hotel_name_and_places(country_name):
    #chain 1
    prompt_name= PromptTemplate(
    input_variables=["country_name"],
    template="I want to open a hotel for {country_name} places. Please suggest me name for this."
    )
    name_chain= LLMChain(llm=llm, prompt=prompt_name,output_key="hotel_name")


    prompt_location_name= PromptTemplate(
    input_variables=["hotel_name"],
    template="Suggest me some locations for {hotel_name} places. Return it as a numerical number list."
    )
    hotel_chain= LLMChain(llm=llm, prompt=prompt_location_name,output_key="places")

    chain= SequentialChain(chains=[name_chain,hotel_chain], 
                        input_variables=["country_name"],
                        output_variables=["hotel_name","places"]
                        
                        )

    response= chain(country_name)
    return response

#this is the main function
if __name__ == "__main__":  
    response= generate_hotel_name_and_places("Nigeria")
    print(response)