python -m venv env
.\env\Scripts\activate.bat
pip install DeepPavlov 
python -m deeppavlov install ner_rus
from deeppavlov import configs,build_model
ner_model = build_model(configs.ner.ner_rus, download=True)
