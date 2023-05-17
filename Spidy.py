import random
import json
import torch
from CentralPoint import Brain
from NeuralNetwork import bag_of_words, tokenize
from say import wish

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
with open("emotions.json", 'r') as json_data:
    emotions = json.load(json_data)


FILE = "TrainingData.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = Brain(input_size,hidden_size,output_size).to(device)
model.load_state_dict(model_state)
model.eval()

#-----------------------

NAME = "Spidy"
from Task import NonInputExe
from Task import InputExe

from Listen import takeCommand
from say import speak
#wish()
def Main():
    
    sentence = takeCommand()
    result = str(sentence)

    if "quit" in sentence:
        exit()
    sentence = tokenize(sentence)
    X = bag_of_words(sentence,all_words)
    X = X.reshape(1,X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)

    _ , predicted = torch.max(output,dim=1)

    tag = tags[predicted.item()]
    
    probs = torch.softmax(output,dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.8:
        for emotion in emotions['emotions']:
            if tag == emotion["tag"]:
                reply = random.choice(emotion["responses"])

                if "time" in reply:
                    NonInputExe(reply)
                elif "date" in reply:
                    NonInputExe(reply)
                elif "day" in reply:
                    NonInputExe(reply)
                elif "shutdown" in reply:
                    NonInputExe(reply)
                elif "restart" in reply:
                    NonInputExe(reply)
                elif "lockscreen" in reply:
                    NonInputExe(reply)
                elif "wikipedia" in reply:
                    InputExe(reply,result)              
                elif "google" in reply:
                    InputExe(reply,result)
                elif "youtube" in reply:
                    InputExe(reply,result)
                elif "maps" in reply:
                    InputExe(reply,result)
                elif "whatsappmsg" in reply:
                    InputExe(reply,result)
                elif "open" in reply:
                    InputExe(reply,result)
                elif "temperature" in reply:
                    InputExe(reply,result)
                elif "alarm" in reply:
                    InputExe(reply,result)
                elif "email" in reply:
                    InputExe(reply,result)
                elif "countdown" in reply:
                    InputExe(reply,result)

                else:
                    speak(reply)
while True:
    Main() 

